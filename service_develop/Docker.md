#### 가상화
* 개발할때 서버에 직접 개발 X (Local 환경에서 개발, Staging 서버에서 완료, Production 서버에서 배포)
* Local 환경과 Production 환경이 다를 수 O, 같아도 서버에서 올바르게 작동 X 가능
* 가상화 : 특정 소프트웨어 환경을 만들고 Local, Production 서버에서 그대로 사용
* VM(Virtual Machine) : 실제 물리적 컴퓨터위에 OS를 포함한 가상화 소프트웨어를 두는 방식
* 그러나 OS위에 OS 하나 더 실행시키면 VM은 무거워짐=> Container : VM 무거움 크게 덜어주면서 가상화를 좀더 가볍게 함

#### Docker
* Container 기술을 쉽게 사용할 수 있게 함
* Docker Image : 컨테이너 실행할 때 사용하는 '탬플릿', Read Only, 수정X (PC방에서 프로그램 깔아도 재부팅시 원상태로 복구)
* Docker Container : Docker Image 활용해 실행된 인스턴스, Write Only


#### Docker로 할 수 있는 일
* 다른 사람 소프트웨어 가져옴 (Ex. MySQL, Jupyer를 Docker 실행)
* 원격 저장소에 저장하면 어디서나 실행

#### 실습

* docker pull mysql:8 : 다운 받을 이미지 다운(여기서 이미지는 Docker Image)
* docker images : 다운 받은 이미지
* docker run --name mysql-tutorial -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:8
  * --name : 이름
  * -e : 환경변수 설정(비밀번호 등) 
  * -d : background 모드, 설정하지 않으면 현재 실행하는 셀 위에서 컨테이너 실행
  * -p : 포트 지정 : 3306으로 접근시 컨테이너 포트 3306으로 연결된다
* docker ps : 실행한 컨테이너
* docker exec -it "컨테이너 이름" /bin/bash : 컨테이너 진입
* mysql -u root -p : MySQL 프로세스로 들어감
* docker ps -a : 작동을 멈춘 컨테이너 확인
* docker rm  "컨테이너 이름"  : 컨테이너 삭제

#### docker run 공유
* 컨테이너 내부는 컨테이너 삭제할때 파일도 같이 사라짐
* Volume Mount 진행하면 Host와 Container의 폴더가 공유됨


#### Docker Image 만들기
* Dockerhub에 공개된 모든 이미지 다운받을 수 있음


## FastAPI 패키지 실행
**shell**
* python -m venv .venv : 가상환경
* source .venv/bin/activate
* pip install pip --upgrade
* pip install "fastapi[all]"
* pip freeze > requirements.txt

#### 도커파일 만들기
**도커파일**
```ptyhon
FROM 이미지 이름
COPY. /app  # 컨테이너 내 디렉토리
WORKDIR /app  #컨테이너 내 디렉토리
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1  # ENV 환경변수 이름=값
RUN pip install pip==21.24 && \
      pip install -r requirement.txt   # 실행할 리눅스 명령어, &&\는 2개를 한번에 실행하겠다.
CMD ["python", "main.py"\]             # CMD[실행할 명령어, 인자]
```

#### 그 이후
* docker build "dockerfile 위치 경로"   : 이미지 빌드
* docker run "이미지 이름:태그"         : 이미지 실행






