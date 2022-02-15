## MLflow
#### MLflow 없던 시절
* 실험 추적 hard (metric, history 등을 사용)
* 코드 재현 hard
* 모델을 패키징하고 배포하는 방법 hard
* 모델 관리 저장소 없음

#### MLflow 특징
* CLI, GUI 지원
* 모델 실험 관리 & 공유
  * 소스코드, 하이퍼파라미터 저장
  * 모델 Artifact, 이미지 저장  
  * 모델 생성일, 모델 성능, 모델 메타정보 저장
  * 여러 모델 운영
* Model Registry
  * 머신러닝 모델 등록 가능
  * 다른 사람들에게 쉽게 공유 가능
* Model Serving
  * Model Registry에 등록한 모델을 REST API 형태로 서버로 Serving
  * Input=Model의 input
  * Output=Model의 output
  * 직접 Dockr Image 만들지 않아도 생성할 수 있음



```python
def main():
  ~~~~
  ~~~~
  model = LinearRegresion()
  with mlflow.start_run() as run:
    model.fit(X,y)
    print("logged data and model in run {}".format(run.info.run_id))
````


### MLflow Tracking
* 머신러닝 코드 실행, 로깅을 위한 API ,UI
* 결과를 Local, Server에 기록해 여러 실행과 비교 가능
* 팀에서 협력 가능
* mlflow run  logistic_regression --experiment-name-이름 --no-conda : run으로 실행
* mlflow ui : UI 실행


### Experiment
* 하나의 Experiment 진행, 머신러닝 프로젝트 단위로 구성
* 정해진 Metric으로 모델 평가
* 하나의 Experiment에 여러개 run
* mlflow experiments create --experiment-name 실험이름 : Experiment 생성
* ls -al : 폴더 확인
* mlflow experiments  list : 리스트 확인

#### MLflow Project
* Project : 간단하게 소스 저장된 폴더, Git Repo, 의존성과 어떻게 실행해야 하는지 저장
* MLflow Tracking API 사용하면 MLflow 프로젝트 비전을 모든 파라미터와 자동 로깅

#### MLflow Model
* 모델은 모델 파일과 코드로 저장
* 다양한 플랫폼에 배포할 수 있는 여러 도구 제공
* MLflow Tracking API를 사용하면 MLflow는 자동으로 해당 프로젝트에 대한 내용 사용

#### MLflow Registry
* Model의 전체 Lifecycle에서 사용할 수 잇는 중앙 모델 저장소


```python
if __name__=="main" :
  mlflow.sklearn.autolog()  #자동으로 로그 저장, 근데 아직... 파이토치 지원X
  ~~~~
  ~~~~
  model = LinearRegresion()
  with mlflow.start_run() as run:
    model.fit(X,y)
    print("logged data and model in run {}".format(run.info.run_id))
````

#### MLflow 아키텍처
* 파이썬 코드
* Tracking Server : 파이썬 코드 실행하는 동안 Parameter, Metric 등 정보 저장
* Artifact Score : 파이썬 코드 실행되는 동안 생기는 Model file, image 등 저장


#### 외부 Storage 사용하기
* mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root $(pwd)/artifacts

=> /// 3개 붙여야함!!

![image](https://user-images.githubusercontent.com/63588046/154004565-9fccf947-ec63-4db7-82e4-e3d5a2105dc5.png)



