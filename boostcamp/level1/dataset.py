
import os
import random
from collections import defaultdict
from enum import Enum
from typing import Tuple, List, Dict

import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset, Subset, random_split
from torchvision import transforms
from torchvision.transforms import *

IMG_EXTENSIONS = [
    ".jpg", ".JPG", ".jpeg", ".JPEG", ".png",
    ".PNG", ".ppm", ".PPM", ".bmp", ".BMP",
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)


class BaseAugmentation:
    def __init__(self, resize, mean, std, **args):
        self.transform = transforms.Compose([
            Resize(resize, Image.BILINEAR),
            ToTensor(),
            Normalize(mean=mean, std=std),
        ])

    def __call__(self, image):
        return self.transform(image)


class AddGaussianNoise(object):
    """
        transform 에 없는 기능들은 이런식으로 __init__, __call__, __repr__ 부분을
        직접 구현하여 사용할 수 있습니다.
    """

    def __init__(self, mean=0., std=1.):
        self.std = std
        self.mean = mean

    def __call__(self, tensor):
        return tensor + torch.randn(tensor.size()) * self.std + self.mean

    def __repr__(self):
        return self.__class__.__name__ + '(mean={0}, std={1})'.format(self.mean, self.std)


class CustomAugmentation:
    def __init__(self, resize, mean, std, **args):
        self.transform = transforms.Compose([
            CenterCrop((320, 256)),
            Resize(resize, Image.BILINEAR),
            ColorJitter(0.1, 0.1, 0.1, 0.1),
            ToTensor(),
            Normalize(mean=mean, std=std),
            AddGaussianNoise()
        ])

    def __call__(self, image):
        return self.transform(image)

    

class MaskLabels(int, Enum):
    MASK = 0
    INCORRECT = 1
    NORMAL = 2
    

    @classmethod
    def from_str(cls, value: str) -> int:
        if value == 'mask1' or value == 'mask2' or value == 'mask3' or value == 'mask4' or value == 'mask5':
            return cls.MASK
        elif value == 'incorrect_mask':
            return cls.INCORRECT
        elif value == 'normal':
            return cls.NORMAL
        else:
            raise ValueError(f"Mask value is {value}, which is errorneous")


class GenderLabels(int, Enum):
    MALE = 0
    FEMALE = 1

    @classmethod
    def from_str(cls, value: str) -> int:
        if value == 'male':
            return cls.MALE
        elif value == 'female':
            return cls.FEMALE
        else:
            raise ValueError(f"Gender value should be either 'male' or 'female', but is {value}")


class AgeLabels(int, Enum):
    YOUNG = 0
    MIDDLE = 1
    OLD = 2

    @classmethod
    def from_number(cls, value: str) -> int:
        try:
            value = int(value)
        except Exception:
            raise ValueError(f"Age value should be numeric, but is {value}")

        if value < 30:
            return cls.YOUNG
        elif value < 60:
            return cls.MIDDLE
        else:
            return cls.OLD

class MaskBaseDataset(Dataset):
    #############################################################################################
    num_classes=18
    mask_num_classes = 3 
    gender_num_classes=2 
    age_num_classes=3

    _file_names = {
        "mask1": MaskLabels.MASK,
        "mask2": MaskLabels.MASK,
        "mask3": MaskLabels.MASK,
        "mask4": MaskLabels.MASK,
        "mask5": MaskLabels.MASK,
        "incorrect_mask": MaskLabels.INCORRECT,
        "normal": MaskLabels.NORMAL
    }

    image_paths = []
    mask_labels = []
    gender_labels = []
    age_labels = []
    
    def __init__(self, data_dir, mean=(0.548, 0.504, 0.479), std=(0.237, 0.247, 0.246), val_ratio=0.2):
        self.data_dir = data_dir
        self.mean = mean
        self.std = std
        self.val_ratio = val_ratio

        self.transform = None
        self.setup()
        self.calc_statistics()
        self.indices = {
            'train': [],
            'val': []
        }

        
    def setup(self):
        profiles = os.listdir(self.data_dir)     # 이미지 리스트
        for profile in profiles:                
            if profile.startswith("."):  # "." 로 시작하는 파일은 무시합니다
                continue

            img_folder = os.path.join(self.data_dir, profile)            #input/data/eval/images or input/data/train/images/각각 이미지 폴더
            for file_name in os.listdir(img_folder):
                _file_name, ext = os.path.splitext(file_name)
                if _file_name not in self._file_names:  # "." 로 시작하는 파일 및 invalid 한 파일들은 무시합니다
                    continue

                img_path = os.path.join(self.data_dir, profile, file_name)  # (resized_data, 000004_male_Asian_54, mask1.jpg)   # 각 이미지 파일
                mask_label = self._file_names[_file_name]

                id, gender, race, age = profile.split("_")
                gender_label = GenderLabels.from_str(gender)
                age_label = AgeLabels.from_number(age)

                self.image_paths.append(img_path)
                self.mask_labels.append(mask_label)
                self.gender_labels.append(gender_label)
                self.age_labels.append(age_label)

    def calc_statistics(self):
        has_statistics = self.mean is not None and self.std is not None
        if not has_statistics:
            print("[Warning] Calculating statistics... It can take a long time depending on your CPU machine")
            sums = []
            squared = []
            for image_path in self.image_paths[:3000]:
                image = np.array(Image.open(image_path)).astype(np.int32)
                sums.append(image.mean(axis=(0, 1)))
                squared.append((image ** 2).mean(axis=(0, 1)))

            self.mean = np.mean(sums, axis=0) / 255
            self.std = (np.mean(squared, axis=0) - self.mean ** 2) ** 0.5 / 255

    def set_transform(self, transform):
        self.transform = transform

    def __getitem__(self, index):
        assert self.transform is not None, ".set_tranform 메소드를 이용하여 transform 을 주입해주세요"

        image = self.read_image(index)
        mask_label = self.get_mask_label(index)
        gender_label = self.get_gender_label(index)
        age_label = self.get_age_label(index)
        multi_class_label = self.encode_multi_class(mask_label, gender_label, age_label)

        image_transform = self.transform(image)
        
        #########################
        return image_transform, mask_label, gender_label, age_label

    def __len__(self):
        return len(self.image_paths)
                               
    def get_mask_label(self, index) -> MaskLabels:
        return self.mask_labels[index]

    def get_gender_label(self, index) -> GenderLabels:
        return self.gender_labels[index]

    def get_age_label(self, index) -> AgeLabels:
        return self.age_labels[index]

    def read_image(self, index):
        image_path = self.image_paths[index]
        return Image.open(image_path)

    @staticmethod
    def encode_multi_class(mask_label, gender_label, age_label) -> int:
        return mask_label * 6 + gender_label * 3 + age_label

    @staticmethod
    def decode_multi_class(multi_class_label) -> Tuple[MaskLabels, GenderLabels, AgeLabels]:
        mask_label = (multi_class_label // 6) % 3
        gender_label = (multi_class_label // 3) % 2
        age_label = multi_class_label % 3
        return mask_label, gender_label, age_label

    @staticmethod
    def denormalize_image(image, mean, std):
        img_cp = image.copy()
        img_cp *= std
        img_cp += mean
        img_cp *= 255.0
        img_cp = np.clip(img_cp, 0, 255).astype(np.uint8)
        return img_cp

    def split_dataset(self) -> Tuple[Subset, Subset]:
        
        ###데이터셋을 train 과 val 로 나눕니다,
        ###pytorch 내부의 torch.utils.data.random_split 함수를 사용하여
        ###torch.utils.data.Subset 클래스 둘로 나눕니다.
        ###구현이 어렵지 않으니 구글링 혹은 IDE (e.g. pycharm) 의 navigation 기능을 통해 코드를 한 번 읽어보는 것을 추천드립니다^^
        
        
        n_val = int(len(self) * self.val_ratio)
        n_train = len(self) - n_val
        train_set, val_set = random_split(self, [n_train, n_val])
        return train_set, val_set
        
        
        whole_len=int(len(self))//7
        n_val = int(whole_len * self.val_ratio)
        val_indices = []
        [val_indices.extend([range(i,i+7)]) for i in  random.sample(range(whole_len), k=n_val)]
        print(1)
        val_indices=set(val_indices)
        print(2)
        train_indices=set(range(len(self)))-val_indices
        print(3)
        return Subset(self,train_indices), Subset(self,val_indices)
        
####################################################################################################################
                                                  
class MaskSplitByProfileDataset(MaskBaseDataset):
    
        #train / val 나누는 기준을 이미지에 대해서 random 이 아닌
        #사람(profile)을 기준으로 나눕니다.
        #구현은 val_ratio 에 맞게 train / val 나누는 것을 이미지 전체가 아닌 사람(profile)에 대해서 진행하여 indexing 을 합니다
        #이후 `split_dataset` 에서 index 에 맞게 Subset 으로 dataset 을 분기합니다.
    

    def __init__(self, data_dir, mean=(0.548, 0.504, 0.479), std=(0.237, 0.247, 0.246), val_ratio=0.2):
        self.indices = defaultdict(list)
        super().__init__(data_dir, mean, std, val_ratio)

    @staticmethod
    def _split_profile(profiles, val_ratio):
        length = len(profiles)
        n_val = int(length * val_ratio)

        val_indices = set(random.choices(range(length), k=n_val))
        train_indices = set(range(length)) - val_indices
        return {
            "train": train_indices,
            "val": val_indices
        }

    def setup(self):
        profiles = os.listdir(self.data_dir)
        profiles = [profile for profile in profiles if not profile.startswith(".")]
        split_profiles = self._split_profile(profiles, self.val_ratio)

        cnt = 0
        for phase, indices in split_profiles.items():
            for _idx in indices:
                profile = profiles[_idx]
                img_folder = os.path.join(self.data_dir, profile)
                for file_name in os.listdir(img_folder):
                    _file_name, ext = os.path.splitext(file_name)
                    if _file_name not in self._file_names:  # "." 로 시작하는 파일 및 invalid 한 파일들은 무시합니다
                        continue

                    img_path = os.path.join(self.data_dir, profile, file_name)  # (resized_data, 000004_male_Asian_54, mask1.jpg)
                    mask_label = self._file_names[_file_name]

                    id, gender, race, age = profile.split("_")
                    gender_label = GenderLabels.from_str(gender)
                    age_label = AgeLabels.from_number(age)

                    self.image_paths.append(img_path)
                    self.mask_labels.append(mask_label)
                    self.gender_labels.append(gender_label)
                    self.age_labels.append(age_label)

                    self.indices[phase].append(cnt)
                    cnt += 1

    def split_dataset(self) -> List[Subset]:
        return [Subset(self, indices) for phase, indices in self.indices.items()]


class TestDataset(Dataset):
    def __init__(self, img_paths, resize, mean=(0.548, 0.504, 0.479), std=(0.237, 0.247, 0.246)):
        self.img_paths = img_paths
        self.transform = transforms.Compose([
            Resize(resize, Image.BILINEAR),
            ToTensor(),
            Normalize(mean=mean, std=std),
        ])

    def __getitem__(self, index):
        image = Image.open(self.img_paths[index])

        if self.transform:
            image = self.transform(image)
        return image

    def __len__(self):
        return len(self.img_paths)
    
    
    
"""    
##################################################################################################################################

class CycleDataset(Dataset):
    num_classes=18
    mask_num_classes = 3 
    gender_num_classes=2 
    age_num_classes=3

    _file_names = {
        "mask1": MaskLabels.MASK,
        "mask2": MaskLabels.MASK,
        "mask3": MaskLabels.MASK,
        "mask4": MaskLabels.MASK,
        "mask5": MaskLabels.MASK,
        "incorrect_mask": MaskLabels.INCORRECT,
        "normal": MaskLabels.NORMAL
    }
    
    #image_paths = []
    #mask_labels = []
    #gender_labels = []
    #age_labels = []
    
    
    mask_image_paths=[]
    no_mask_image_paths=[]
    
    
    def __init__(self, data_dir, mean=(0.548, 0.504, 0.479), std=(0.237, 0.247, 0.246), val_ratio=0.2):
        self.data_dir = data_dir
        self.mean = mean
        self.std = std
        self.val_ratio = val_ratio

        self.transform = None
        self.setup()

        self.indices = {
            'train': [],
            'val': []
        }

        
    def setup(self):
        profiles = os.listdir(self.data_dir)     # 이미지 리스트
        for profile in profiles:                
            if profile.startswith("."):  # "." 로 시작하는 파일은 무시합니다
                continue

            img_folder = os.path.join(self.data_dir, profile)            #input/data/eval/images or input/data/train/images/각각 이미지 폴더
            for file_name in os.listdir(img_folder):
                _file_name, ext = os.path.splitext(file_name)
                if _file_name not in self._file_names:  # "." 로 시작하는 파일 및 invalid 한 파일들은 무시합니다
                    continue

                img_path = os.path.join(self.data_dir, profile, file_name)  # (resized_data, 000004_male_Asian_54, mask1.jpg)   # 각 이미지 파일
                mask_label = self._file_names[_file_name]
                
                #id, gender, race, age = profile.split("_")
                #gender_label = GenderLabels.from_str(gender)
                #age_label = AgeLabels.from_number(age)

                #self.image_paths.append(img_path)
                #self.mask_labels.append(mask_label)
                #self.gender_labels.append(gender_label)
                #self.age_labels.append(age_label)
                
                
                if mask_label==0 or mask_label==1:
                    self.mask_image_paths.append(img_path)
                else:
                    for i in range(6):
                        self.no_mask_image_paths.append(img_path)
                    
            

    def set_transform(self, transform):
        self.transform = transform

    def __getitem__(self, index):
        assert self.transform is not None, ".set_tranform 메소드를 이용하여 transform 을 주입해주세요"

        mask_image = self.mask_read_image(index)
        no_mask_image = self.no_mask_read_image(index)
        
        #mask_label = self.get_mask_label(index)
        #gender_label = self.get_gender_label(index)
        #age_label = self.get_age_label(index)
        #multi_class_label = self.encode_multi_class(mask_label, gender_label, age_label)
        
        
        mask_image_transform = self.transform(mask_image)
        no_mask_image_transform = self.transform(no_mask_image)
        
        return mask_image_transform, no_mask_image_transform
        
        ###########################################################################
    def __len__(self):
        return len(self.mask_image_paths)
                               
    def get_mask_label(self, index) -> MaskLabels:
        return self.mask_labels[index]

    def get_gender_label(self, index) -> GenderLabels:
        return self.gender_labels[index]

    def get_age_label(self, index) -> AgeLabels:
        return self.age_labels[index]
    
    def mask_read_image(self, index):
        image_path = self.mask_image_paths[index]
        return Image.open(image_path)
    
    def no_mask_read_image(self, index):
        image_path = self.no_mask_image_paths[index]
        return Image.open(image_path)

    @staticmethod
    def encode_multi_class(mask_label, gender_label, age_label) -> int:
        return mask_label * 6 + gender_label * 3 + age_label

    @staticmethod
    def decode_multi_class(multi_class_label) -> Tuple[MaskLabels, GenderLabels, AgeLabels]:
        mask_label = (multi_class_label // 6) % 3
        gender_label = (multi_class_label // 3) % 2
        age_label = multi_class_label % 3
        return mask_label, gender_label, age_label

    @staticmethod
    def denormalize_image(image, mean, std):
        img_cp = image.copy()
        img_cp *= std
        img_cp += mean
        img_cp *= 255.0
        img_cp = np.clip(img_cp, 0, 255).astype(np.uint8)
        return img_cp

    def split_dataset(self) -> Tuple[Subset, Subset]:
        
        #데이터셋을 train 과 val 로 나눕니다,
        #pytorch 내부의 torch.utils.data.random_split 함수를 사용하여
        #torch.utils.data.Subset 클래스 둘로 나눕니다.
        #구현이 어렵지 않으니 구글링 혹은 IDE (e.g. pycharm) 의 navigation 기능을 통해 코드를 한 번 읽어보는 것을 추천드립니다^^
        
        whole_len=int(len(self))//7
        n_val = int(whole_len * self.val_ratio)
        val_indices = []
        [val_indices.extend([range(i,i+7)]) for i in  random.sample(range(whole_len), k=n_val)]
        print(1)
        val_indices=set(val_indices)
        print(2)
        train_indices=set(range(len(self)))-val_indices
        print(3)
        return Subset(self,train_indices), Subset(self,val_indices)
        
 """       
        
        
        
########################################################################################################################




class ProfileClassEqualSplitTrainMaskDataset(Dataset):
    
    num_classes=18
    mask_num_classes=3
    gender_num_classes=2
    age_num_classes=3
    
    image_paths=[]
    image_labels=[]
    
    
    def __init__(self, data_dir: str = '/',
                 mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225),
                 transform = None, val_ratio: float = 0.2, classes: int = 18) -> None:
        super().__init__()

        self.mean = mean
        self.std = std
        self.transform = transform
        self.indices = {
            'train': [],
            'val': []
        }

        self.setup(os.path.join(data_dir, 'train/images'), val_ratio, classes)
        self.calc_statistics()

    @staticmethod
    def split_profile(profiles_len: int, val_ratio: float) -> Dict:
        assert profiles_len % 5 == 0, ValueError(f"Each profile should have five mask wearing images")
        profiles_len = profiles_len // 5

        val_len = int(profiles_len * val_ratio)

        val_indices = set(random.sample(range(profiles_len), k=val_len))
        train_indices = set(range(profiles_len)) - val_indices

        return {
            'train': train_indices,
            'val': val_indices
        }

    def setup(self, root: str, val_ratio: float, classes: int) -> None:
        for _ in range(classes):
            self.image_paths.append([])

        profiles = os.listdir(root)
        for profile in profiles:
            if profile.startswith('.'):
                continue

            _, gender, _, age = profile.split('_')
            gender_label = GenderLabels.from_str(gender)
            age_label = AgeLabels.from_number(age)

            img_folder = os.path.join(root, profile)
            for file_name_ext in os.listdir(img_folder):
                file_name, _ = os.path.splitext(file_name_ext)
                if file_name not in ['incorrect_mask', 'mask1', 'mask2', 'mask3', 'mask4', 'mask5', 'normal']:
                    continue

                mask_label = MaskLabels.from_str(file_name)
                label = self.encode_multi_class(mask_label, gender_label, age_label)

                img_path = os.path.join(root, profile, file_name_ext)
                self.image_paths[label].append(img_path)

        # Number of image paths of images with class label [None, 0, 0 ~ 1, 0 ~ 2, ..., 0 ~ 16]
        label_len_sum = [0]
        for label in range(1, classes):
            label_len_sum.append(label_len_sum[label - 1] + len(self.image_paths[label - 1]))

        for label in range(classes // 3):
            split_profiles = self.split_profile(len(self.image_paths[label]), val_ratio)
            for phase, profile_indices in split_profiles.items():
                for profile_index in profile_indices:
                    for i in range(5):
                        self.indices[phase].append(label_len_sum[label] + profile_index * 5 + i) # Label 0 ~ 5
                    self.indices[phase].append(label_len_sum[label + 6] + profile_index) # Label 6 ~ 11
                    self.indices[phase].append(label_len_sum[label + 12] + profile_index) # Label 12 ~ 17

        for label in range(classes):
            self.image_labels.extend([label] * len(self.image_paths[label]))

        self.image_paths = [path for path_label in self.image_paths for path in path_label] # Flatten

    # For baseline compatibility
    def calc_statistics(self):
        has_statistics = self.mean is not None and self.std is not None
        if not has_statistics:
            print("[Warning] Calculating statistics... It can take a long time depending on your CPU machine")
            sums = []
            squared = []
            for image_path in self.image_paths[:3000]:
                image = np.array(Image.open(image_path)).astype(np.int32)
                sums.append(image.mean(axis=(0, 1)))
                squared.append((image ** 2).mean(axis=(0, 1)))

            self.mean = np.mean(sums, axis=0) / 255
            self.std = (np.mean(squared, axis=0) - self.mean ** 2) ** 0.5 / 255

    # For baseline compatibility
    def set_transform(self, transform) -> None:
        self.transform = transform

    def __getitem__(self, index: int) -> Tuple[Image.Image, int]:
        image = self.read_image(index)
        label = self.get_label(index)

        if self.transform:
            return self.transform(image), label
        else:
            return image, label

    def __len__(self) -> int:
        return len(self.image_paths)

    def get_label(self, index: int) -> int:
        return self.image_labels[index]

    def read_image(self, index: int) -> Image.Image:
        return Image.open(self.image_paths[index])

    @staticmethod
    def encode_multi_class(mask_label: int, gender_label: int, age_label: int) -> int:
        return mask_label * 6 + gender_label * 3 + age_label

    # For baseline compatibility
    @staticmethod
    def decode_multi_class(multi_class_label) -> Tuple[MaskLabels, GenderLabels, AgeLabels]:
        mask_label = (multi_class_label // 6) % 3
        gender_label = (multi_class_label // 3) % 2
        age_label = multi_class_label % 3
        return mask_label, gender_label, age_label

    # For baseline compatibility
    @staticmethod
    def denormalize_image(image, mean, std):
        img_cp = image.copy()
        img_cp *= std
        img_cp += mean
        img_cp *= 255.0
        img_cp = np.clip(img_cp, 0, 255).astype(np.uint8)
        return img_cp

    def split_dataset(self) -> List[Subset]:
        return [Subset(self, indices) for _, indices in self.indices.items()]


class EvalMaskDataset(Dataset):
    def __init__(self, data_dir: str = '/', transform = None) -> None:
        super().__init__()

        img_list = pd.read_csv(os.path.join(data_dir, 'eval/info.csv'))
        self.image_paths = [os.path.join(data_dir, 'eval/images', img_id) for img_id in img_list.ImageID]
        self.transform = transform

    # For baseline compatibility
    def set_transform(self, transform) -> None:
        self.transform = transform

    def __getitem__(self, index: int) -> Image.Image:
        image = self.read_image(index)

        if self.transform:
            return self.transform(image)
        else:
            return image

    def __len__(self) -> int:
        return len(self.image_paths)

    def read_image(self, index: int) -> Image.Image:
        return Image.open(self.image_paths[index])

class TestDataset(Dataset):
    '''
    For baseline compatibility
    '''
    def __init__(self, img_paths, resize, mean=(0.548, 0.504, 0.479), std=(0.237, 0.247, 0.246)) -> None:
        self.img_paths = img_paths
        self.transform = transforms.Compose([
            transforms.Resize(resize, Image.BILINEAR),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std),
        ])

    def __getitem__(self, index: int) -> Image.Image:
        image = self.read_image(index)

        if self.transform:
            return self.transform(image)
        else:
            return image

    def __len__(self) -> int:
        return len(self.img_paths)

    def read_image(self, index: int) -> Image.Image:
        return Image.open(self.img_paths[index])