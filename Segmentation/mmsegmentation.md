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
