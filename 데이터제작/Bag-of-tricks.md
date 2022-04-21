## 데이터를 사용해서 성능을 올리는 방법
1. Synthetic Data
2. Data Augmentaion
3. Others

## Synthetic Data
* 성능 향상 -> 양질의 Data 확보
* Data 확보 = Public Data + 직접 만들기

#### 데이터 직접 만들기
1. 사진을 찍고 annotation 생성
2. Synthetic Data 
  * 비용이 적음
  * 개인정보나 라이센스에서 자유로움
  * 더 세밀한 수준의 annotation 얻을 수 있다.

#### SynthText
* 원본 이미지는 글자를 포함하지 않는 사진 선택(수작업)
* 적절한 위치에 글자를 합성
* 현실적인 위치에 보이게 하도록 Depth & gPb-UCM Segmentation으로 Text Regions 고름
* Text Region에서 같은 영역에 속하도록 글자를 넣음

![image](https://user-images.githubusercontent.com/63588046/164357398-27c2f8ee-ecb6-40d7-ac86-2e4176d84ba9.png)

#### SynthText3D & UnrealText 
* 가상 이미지는 unreal engine market에서 얻어옴
* 글자를 넣을 영역 결정
* 글자를 생성해서 이미지에 넣음

![image](https://user-images.githubusercontent.com/63588046/164357744-6a26f4db-0727-447c-bf68-8dc9415eec4c.png)


## 어떻게 synthetic data 사용할까
![image](https://user-images.githubusercontent.com/63588046/164357919-fd6c01c4-ff85-4e76-bf76-2e71340eb726.png)



## Image Augmentation
* 어떤 것이 우리가 원하는 데이터가 적절한지 그리고 안좋게 변화되는 것이 무엇인지 파악!!
![image](https://user-images.githubusercontent.com/63588046/164361580-acc82212-e0c9-4f90-82b7-7f9c1b60cb31.png)

#### Geometric Transform
* Global-level의 변화를 줌
* Random crop, resize, rotate, flip, shear
![image](https://user-images.githubusercontent.com/63588046/164361696-6b08f849-986a-48dc-ac34-357e43a72c09.png)


#### Style transform
* local-level 변화
* color jitter, channel shuffle, noise filter
![image](https://user-images.githubusercontent.com/63588046/164361783-1b967315-9b9b-4384-92ed-94af82bef037.png)

#### OCR에서 augmentation
* positive ratio : 1개 이상 개체 포함 -> hard negative mining 도입해서 해결
* 개체 잘림 방지 -> 밀집된 곳은 자르지 않게됨... -> 1개 이상의 개체는 잘리지 않는다로 조건 완화 가능


## Others
#### Large Scale Variation
* 이미지의 크기가 매우 다양한 것이 객체 검출을 어렵게함
* Crop & resize, image pyramid는 글자의 크기를 너무 작게 혹은 크게 만듬...
* SNIP : Crop, resize, image pyramid 사용하되 영역이 너무 크거나 너무 작은것은 학습을 하지 않음

#### Canonical KnapSack
* 글자가 있을법한 위치를 구해서 그 부분의 글자를 적정 크기로 바꿔서 학습
* 배경 계산 X -> 효율적
* scale variation 문제 발생 X
