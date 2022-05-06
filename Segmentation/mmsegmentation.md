## smp
![image](https://user-images.githubusercontent.com/63588046/166614636-42b8aeb4-e6c1-45b1-bac2-863dd1f170a1.png)

![image](https://user-images.githubusercontent.com/63588046/166614646-08543026-867f-407c-9d7b-7ef86787f9b1.png)

![image](https://user-images.githubusercontent.com/63588046/166614663-bb728f4d-c12a-4c3e-9f1c-cb8c012fac7e.png)

![image](https://user-images.githubusercontent.com/63588046/166615029-d5c85dcc-4b93-45d8-8bef-93b38e19ad42.png)

![image](https://user-images.githubusercontent.com/63588046/166615067-836a5def-9dce-4071-82cd-5fccea443093.png)



# mmsegmentation

## train.py
* 주어진 파일을 가지고 config object 생성
* 생성한 config 가지고 모델 생성
* 생성한 config 가지고 dataset 생성
* 학습

## config
* model, dataset, 학습 방법 등 모든 정보 가지고 있음
* openMMLab의 모든 프로젝트에서 공통적으로 사용되기 때문에 mmcv 안에 위치
* fromfile 메서드를 통해서 .py 파일로 정의한 config들을 가져온다.
* 이후 터미널에서 --cfg-options를 통해서 정의한 config를 덮어 씌운다.

#### fromfile 메서드가 .py 파일을 파싱하는 순서
* 주어진 .py 파일 안에 정의되어 있는 부분을 읽는다.
* __base__라는 키워드가 있는지 확인한다.
    * 존재한다면 __base__ 안의 .py 파일들을 읽는다.
    * __base__ 안의 .py 파일에는 있고 주어진 .py 파일에는 없는 부분을 채워 넣는다.
    * 양쪽에 전부 있다면 주어진 .py파일의 내용을 사용한다.
    * __base__ 안의 .py 파일 사이에 중복되는 내용이 있어서는 안된다.

![image](https://user-images.githubusercontent.com/63588046/167047832-f6b99cf9-420f-42f9-aa58-382e99e4a70f.png)

![image](https://user-images.githubusercontent.com/63588046/167047865-ca0fede9-ba9a-43c3-a5be-8ca31656ed94.png)
-> 에러

![image](https://user-images.githubusercontent.com/63588046/167048002-b9c598d9-20d5-41f9-841f-5bda0b3285b8.png)

![image](https://user-images.githubusercontent.com/63588046/167048069-16f1f70f-f0da-477c-bff5-36b4ac5a152e.png)

#### config 파일 작성 팁
* builder function에섯 꼭 있어야 하는 내용 존재
    * model, data, workflow
* 있어도 되고 없어도 되는 내용 존재
    * fp 16
* configs/__base__ 폴더 안에 대부분 필요한 것이 있으니 모델의 num_classes만 바꿔보는 것으로 첫 실험이 가능하다.



## Registry
#### mmseg 안에 정의된 class들을 가지고 있는 object
* 생성한 config를 가지고 model을 생성하려고 보니, model은:
    * train.py 안에 보이는 build_segmentor 함수를 통해 생성한다.
    * build_segmentor 함수를 살펴보면 SEGMENTORS.build라는 함수를 호출한다.
    * 






