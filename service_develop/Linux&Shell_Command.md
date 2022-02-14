
#### Linux 알아야 하는 이유
* 서버에서 자주 사용하는 OS (Window, Mac용 서버는 유료)
* 오픈소스 많음
* 안전성, 신뢰성 보증
* shell command, shell script

#### CLI 
* Terminal

#### GUI
* Desktop

#### Linux 베포판
* Debian
* Ubuntu
* Redhat
* CentOS

#### Linux 사용 방법
* VirtualBox에 Linux 설치, Docker 설치
* WSL 사용
* Notebook에 터미널 실행


#### 쉘의 종류
* 쉘 : 사용자가 문자를 입력해 컴퓨터에 명령할 수 있도록 하는 프로그램
* 터미널/콘솔 : 쉘을 실행하기 위해 문자, 입력을 받아 컴퓨터에 전달, 프로그램 출력을 화면에 작성
* sh : 최초의 셀
* bash : Linux 표준 쉘
* zsh : OS 기본 쉘

#### 쉘을 사용하는 경우
* 서버에서 접속해서 사용하는 경우
* crontab 등 Linux의 내장 기능 솰용
* 데이터 전처리 하기 위해 쉘 커맨드 사용
* Docker 사용하는 경우
* 수백대의 서버 관리
* jupyter, 터미널 모두 쉘 커맨드
* 배포 파이프라인 실행(Github Action 등)


### 기본 쉘 커맨드 
* man : 쉘 커맨드 메뉴
* q : 종료
* mkdir : 폴더 생성하기(make directory)
* ls : 현재 접근한 폴더의 폴더, 파일 확인
* pwd : 현재 폴더 경로를 절대 경로로 보여줌
* cd : 폴더 변경하기, 폴더 이동하기(change directory)
* echo : 출력하기(echo "hi" )
#### vi : 파일 생성함(Ex. vi vi-test.sh)
  * ESC wq : 저장하고 나가기
  * ESC wq! : 강제로 저장하고 나오기
  * ESC q : 그냥 나가기
  * dd : 현재 위치한 한줄 삭제
  * i : Insert 모드로 변경
  * x : 커서가 위치한 곳의 글자 1개 삭제
  * yy : 현재 줄을 복사
  * p : 현재 커서가 있는 줄 바로 아래에 붙여넣기
  * k : 커서 위로
  * j : 커서 아래로
  * l : 커서 위로
  * h : 커서 왼쪽으로
#### Insert Mode
  * 파일을 수정
  * 다시 command 돌아가려면 ESC 클릭
#### Last Line Mode
  * ESC 누른 후 콜론(:) 누르면 나오는 Mode
  * w : 현재 파일명 저장
  * q : vi 종료(저장 X)
  * q! : vi rkdwpwhdfy
  * wq : 저장 후 종료
  * set nu : vi 라인 번호 출력

#### bash
  * 쉘 스크립트 실행(Ex. bash vi-test.sh)
  * 앞에서 작성한 'hi'가 출력
  * 터미널에서 Tab 누르면 자동완성

#### sudo
  * 관리자 권한으로 실행

#### cp 
  * 파일 저장(Ex. cp vi-test.sh vi-test2.sh)
  * r : 디렉토리 복사할 때 디렉토리 안에 파일 있으면 recursive로 모두 복사
  * f : 복사할 때 강제로 실행
  
#### mv
  * 파일, 폴더 이동(Ex. mv vi-test.sh vi-test3.sh)

#### cat
  * 특정 파일 내용 출력(cat vi-test.sh)
  * 여러 파일 인자로 주면 합쳐서 출력(cat vi-test2.sh vi-test3.sh)
  * 파일 저장(cat vi-test2.sh vi-test3.sh > new_test.sh)
  * 파일 추가(cat vi-test2.sh vi-test3.sh >> new_test.sh)

#### clear
  * 터미널 창을 깨끗하게 해줌

#### history
  * 최근에 입력한 쉘 커맨드 History 출력(Ex. !30)

#### find 
  * 파일 및 디렉토리 검색(find .-name"파일이름"  <= 현재 폴더에서 파일이름이 같은 파일 찾아줌 )

#### alias
  * 별칭을 붙임(파이썬에서 as 같은 것)(alias ll2='ls-l' => ll이라고 치면 ls-l로 바뀜)

#### head, tail
  * head -n 3 vi-test.sh : test.sh에 앞에 3줄 출력

#### sort
  * 행 단위 정렬(r : 정렬을 내림차순, n : Numeric Sort)
  * cat fruits.txt|sort => fruits 파일이 내림차순으로 나옴
  * cat fruits.txt|sort-r => fruits 파일이 오름차순으로 나옴

#### grep
  * i : 대소문자 구분 없이 출력
  * w : 정확히 그 단어만 찾기
  * v : 특정 패턴 제외한 결과 출력
  * E : 정규 표현식 사용(^단어 : 단어로 시작하는 것 찾기, 단어$ : 단어로 끝나는 것 찾기)

#### cut
  * 파일에서 특정 필드 추출(vi cut_file | cut-d : -f 1,7)
  * f : 잘라낼 필드 지정
  * d : 필드를 구분하는 구분자

#### stream
  * stdin : 0으로 표현, 입력
  * stdout : 1로 표현, 출력 값
  * stderr : 2로 표현, 디버깅 정보나 에러 출력

#### Redirection & Pipe
  * > 덮어쓰기  (echo "hi">vi-test3.sh)
  * >> 맨 아래에 추가하기 (echo "hello">>vi-test3.sh)

#### ps
  * e : 모든 프로세스
  * f : Full Format으로 자세히 보여줌

#### curl 
  * Request 테스트 할 수 있는 명령어
  * 웹 서버를 작성한 후 요청이 제대로 실행되는지 확인

#### df
  * 현재 사용중인 디스크 욜량
  * h : 사람이 읽기 쉬운 형태로 출력

#### scp
  * r : 재귀적 복사
  * P : ssh 포트 지정
  * i : SSH 설정을 활용해 실행

#### nohup
  * 터미널 종료 후에도 계속 작업이 유지하도록 실행
  * nohup python3 app.py &
  * nohup 실행 파일은 Permission이 755여야함
  * 종료는 ps ef|grep app.py 한 후 pid(Process ID) 찾은 후 kill -9 pid로 프로세스 Kill
  * 로그는 nohup.out에 저장

#### chmod
  * r : 읽기
  * w : 쓰기
  * X : 실행하기
  * 







