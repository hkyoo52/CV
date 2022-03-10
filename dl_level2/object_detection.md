## Objective detection
* classification + bounding localization
* 1 stage : ROI X, 모든 부분 고려
* 2 stage : ROI O, sampling 된 지점만 rhfugka

![image](https://user-images.githubusercontent.com/63588046/157170808-31313122-1e10-49c5-a524-ab557c76b016.png)

## 1 stage

#### selective search
* Over-segmentation : 색깔이 비슷한 것으로 나눔
* 색이 비슷한 것, 특징이 비슷한 것끼리 합침

#### IOU
* 높을수록 예측력 높음

![image](https://user-images.githubusercontent.com/63588046/157169601-f448947e-e35e-4504-ad49-43c771da8bfd.png)

#### Anchor boxes
* 정답이 있을것 같은 후보 값
* 0.7 이상 => positive
* 0.3 이하 => negative

![image](https://user-images.githubusercontent.com/63588046/157169711-b396e968-ec32-4704-ac87-3c1012824e8c.png)

#### Region proposal network (RPN)
* sliding window로 각 지점을 다 분석
* objectiveness score : 그 지점에 물체가 있는지 없는지 socre 냄 (anchor box 당 2개씩)
* 그 지점에서 x, y, w, h 미세 조정

![image](https://user-images.githubusercontent.com/63588046/157170141-ed6d156d-6c33-4b17-8f8e-d021367d120a.png)

#### Non-Maximum Suppression (NMS)
* objectiveness score 가장 높은 box 선택
* 다른 box와 IOU 비교 -> 50% 이상인것 삭제
* 다음번 가장 높은 objectiveness score 높은 것 찾음


#### R-CNN
* selective search로 2000개 조각 얻음
* wraped region : 224 크기로 resize
* CNN feature
* SVM으로 분류

#### Fast R-CNN
* region proposal -> selective search
* CNN으로 feature map 추출
* ROI projection : 물체의 후보를 결정
* FC layer -> softmax, bbox regressor

#### Faster R-CNN
* 최초의 End to end 
* RPN : selective search도 뉴런으로 진행


![image](https://user-images.githubusercontent.com/63588046/157170423-10583e32-4509-4e35-aa33-dd76162de13c.png)



## 2 stage

#### Yolo
* p 개의 grid로 나눔
* 각 grid마다 박스, object 유무, class가 뭔지 파악 (RPN과 유사)

* 7 * 7의 (5B+C) channel (B는 anchor의 개수, C는 분석할 class 개수)

![image](https://user-images.githubusercontent.com/63588046/157171145-39f40aeb-e031-4639-8a97-cdb7a4c751ce.png)


#### SSD
* grid의 크기에 따라 다른 크기의 anchor box가 나옴 
* 각 레이마다 사용되는 anchor box 개수 다 더해서 마지막에 계산
* 매우 빠르고 높은 성능

![image](https://user-images.githubusercontent.com/63588046/157173592-1d7f186f-f2c8-4d78-ab7e-500824652474.png)

![image](https://user-images.githubusercontent.com/63588046/157173736-b525b880-b06c-47f2-9cb6-a7b226c14126.png)



## 문제점 & 개선점
#### 1 stage 문제점
* 모든 grid를 다 고려함
* 실제로 positive한 grid는 거의 존재X -> imbalance한 문제

#### Focal loss
* cross entropy : 맞으면 작은 loss, 틀리면 큰 loss 
* Focal loss : cross entropy보다 더 심하게 분할시킨다. (잘맞추면 loss는 거의 0)

![image](https://user-images.githubusercontent.com/63588046/157174425-e886efa6-9c58-460f-9792-06195fbac6d4.png)


#### RetinaNet
* Focal loss 사용
* Unet과 비슷한 구조
* concat 대신에 더하기 사용
* 각 레이어에 class subset과 box subset 존재

* Feature Pyramid Network 구조
  - low-level feature의 detail한 local 정보와 high-level feature의 global 정보를 모두 활용
![image](https://user-images.githubusercontent.com/63588046/157175024-595e5514-ced7-434d-a4ca-413cbba5ade2.png)


#### DETR
* 이미지를 조각내서 transformer encoder에 넣음
* decoder에 나온 부분에서 class와 boundbox 구함

![image](https://user-images.githubusercontent.com/63588046/157216698-3260d632-6a8d-41b2-9076-f8faf2a289ec.png)





## 심화 - DETR
* anchor 방식은 heuristic(매우 비효율적임, 최적의 값을 못찾아서 사용하는 방식) & 중복된 예측을 제거할때 성능 bad

![image](https://user-images.githubusercontent.com/63588046/157575944-d40101ac-0dac-48f7-825c-c42442033f6d.png)




#### 장점
* 한번에 모든 객체를 찾음 -> 매우 빠르다
* object가 클 때 성능이 좋다(anchor를 사용X) ... 근데 작아질때는 ㅠㅠ


#### DETR 모델
* N개의 고정된 숫자의 예측 object 추출, 만약 없을 경우 no object를 채워서 N개 맞춤
* 각각을 매칭함
* 
![image](https://user-images.githubusercontent.com/63588046/157592247-83796240-1d1a-4261-a095-3bd2ac7c70c5.png)


* loss 값은 헝가리안 loss 사용
* 만약 no object인 경우 backward할때 전달되는 값을 /10을 함 

![image](https://user-images.githubusercontent.com/63588046/157578822-fff01aa4-8852-4cd7-98bf-b50bbab75f50.png)

![image](https://user-images.githubusercontent.com/63588046/157590325-4963f5c8-d5a5-4c30-b763-cfa844316b77.png)

#### 코드
```python
def box_cxcywh_to_xyxy(x):
    x_c, y_c, w, h = x.unbind(1)
    b = [(x_c - 0.5 * w), (y_c - 0.5 * h),
         (x_c + 0.5 * w), (y_c + 0.5 * h)]
    
    return torch.stack(b, dim=1)

def rescale_bboxes(out_bbox, size):
    img_w, img_h = size
    b = box_cxcywh_to_xyxy(out_bbox)
    b = b * torch.tensor([img_w, img_h, img_w, img_h], dtype=torch.float32)
    return b
    
    
    
    
class DETRdemo(nn.Module):
    
    def __init__(self, num_classes, hidden_dim=256, nheads=8,
                num_encoder_layers=6, num_decoder_layers=6):
        super().__init__()
        
        
        # Resnet-50 backbone 모델 할당, backbone은 마지막 fc layer 사용 X
        self.backbone = resnet50()
        del self.backbone.fc 
        
        
        self.conv = nn.Conv2d(2048, hidden_dim, 1)    # 7,7,2048 -> 7,7,256 (transformer input token)
        
        # pytorch 내 기본 transformer 추가
        self.transformer = nn.Transformer(hidden_dim, nheads, 
                                        num_encoder_layers, num_decoder_layers)
        
        # 예측을 위한 prediction heads에 background detection을 위한 1 extra class를 추가해줍니다.
        self.linear_class = nn.Linear(hidden_dim, num_classes + 1)
        self.linear_bbox = nn.Linear(hidden_dim, 4)
        
        # output positional encodings(object queries) 추가 
        # 100 x 256 차원의 가우시안분포(default)
        # 이 때, 100은 transformer decoder의 sequence입니다. 
        self.query_pos = nn.Parameter(torch.rand(100, hidden_dim))
        
        # spatial positional embeddings
        # 역시, original DETR에서는 sine positional encodings을 사용합니다(demo 버전에선 학습용).
        # 이 때 demo 버전에서는 input의 size를 800 x n 으로 맞춥니다(800<=n<=1600).
        # backbone인 resnet을 통과시키고 나면 size가 32분의 1로 줄기 때문에 
        # feature map의 width(또는 height)는 50을 넘지 않습니다. 
        # forward 단계에서 각 feature map의 size에 맞게 slicing해 사용하게 됩니다. 
        # hidden dimension의 
        
        self.row_embed = nn.Parameter(torch.rand(50, hidden_dim//2))
        self.col_embed = nn.Parameter(torch.rand(50, hidden_dim//2))
        
    def forward(self, inputs):
        
        # Resnet-50에서 average pooling layer 전까지 순전파시킵니다. 
        # resnet은 최초의 convolution - batch norm - relu - maxpool을 거친 후, 
        # conv-batch norm을 주 구성요소로 하는 Bottleneck layer을 굉장히 많이 통과시킵니다.
        x = self.backbone.conv1(inputs)
        x = self.backbone.bn1(x)
        x = self.backbone.relu(x)
        x = self.backbone.maxpool(x)
        
        x = self.backbone.layer1(x) # layer1은 downsampling을 진행하지 않습니다.
        x = self.backbone.layer2(x)
        x = self.backbone.layer3(x)
        x = self.backbone.layer4(x)
        # 여기서 tensor x의 shape은 [None, 2048, input_height//32, input_width//32] 입니다.
        
        # 2048차원의 channel을 가진 feature map(planes)을 256차원의 channle의 feature map으로 축소시킵니다.
        h = self.conv(x)
        # 여기서 tensor h의 shape은 [None, 256, input_height//32, input_width//32] 입니다.
        
        
        # positional encoding을 구성합니다.
        H, W = h.shape[-2:] # backbone + conv를 통해 생성된 feature map의 높이와 너비입니다. 
        
        # 아래의 positional embeddings을 transformer의 input tokens(1d flattened feature map, 즉 tensor h)와 concat함으로써
        # 위치 정보가 없는 input tokens에 위치 정보가 담기게 됩니다.
        
        # 높이, 너비 각각 feature map의 size에 해당하는 positional embeddings을 slicing합니다.
        # column 정보를 담은 positional embeddings (H x W x 128)과 --> H는 그저 차원을 맞추기 위함입니다.
        # row 정보를 담은 positional embeddings (H x W x 128)를 생성한 후 --> W는 그저 차원을 맞추기 위함입니다.
        # concat을 시켜 transformer의 input tokens의 차원인 256과 일치시킨 후 
        # (H x W x 256)의 2d positional embeddings을 (HW x 256)의 1d positional embeddings으로 flatten 해줍니다.
        
        # 이는 2d feature map이 transformer의 input tokens으로 쓰이기 전에 1d feature sequence로 flatten 하는 것과 일치합니다.
        pos=torch.cat([
            self.col_embed[:W].unsqueeze(0).repeat(H, 1, 1),
            self.row_embed[:H].unsqueeze(1).repeat(1, W, 1),
        ], dim=-1).flatten(0, 1).unsqueeze(1)

        # transformer를 순전파시킵니다.
        # 1d feature sequence와 positional embeddings가 concat되어 transformer의 input tokens으로 쓰이고, 
        # object queries의 길이에 해당하는 output token을 반환합니다.  
        h = self.transformer(pos+0.1*h.flatten(2).permute(2, 0, 1),
                            self.query_pos.unsqueeze(1)).transpose(0,1)
        
        # 최종적으로, transformer output을 class label과 bounding boxes로 사영시킵니다.
        # 결과의 차원은 (1, len of object queries, # of classes (or 4 in bboxes))입니다. 
        return {'pred_logits': self.linear_class(h),
                'pred_boxes': self.linear_bbox(h).sigmoid()}

```
