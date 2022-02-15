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

