git cmd 용어 : https://seomal.com/map/1/30

* ls-ai : 
* git status : 현재 상황 볼 수 있음 (커맷 되어 잇는지 안되어 있는지) (수정한거는 commit하도록 정하지 X, 새로 만든 거 : commit 할 상황에 포함시켜라)
* git add work1.txt (work1을 변경사항에 추가해라)
* git commint -m "work 2" : "work 2"가 commit됨

* git add : 변경사항에 넣어라
* git commit : 커밋해라

* git add .gitignore : gitignore 추가해라
* git commit -am "work2.txt 무시" : wokr2.txt gitignor에 넣어라


* git log : log창에 들어가기
* git log --oneline : log창 요약해서 보여주기
* log창에서 키보드 위, 아래로 스크롤하기
* q 누르면 나감


#### commit 잘못 보냈을때
* git commit -ament -m "template 추가" -> 마지막 commit메세지가 template로 바뀜



* git commit -am 'work5' : work5가 변경사항 저장되고 commit한다.

#### 시간여행
* git chekout b2381(git graph에서 이동하고 싶은 상태에 commit 이름) : 과거로 이동한다. (시간여행)
* git checkout master : 현재상태로 되돌아온다. (gui상태에서는 master 클릭하고 checkout)
* git reset --hard b2381(git graph에서 이동하고 싶은 상태에 commit 이름) : 이전 상태로 돌아간다.

## 정리
* Head : working directory가 무엇이냐
* master : 가장 최근에 작업하는 위치
* checkout : 시간여행(head를 움직임)
* reset
  * A : branch가 움직임
  * D : head가 움직임 (=checkout)
  
#### 시간여행
* checkout으로 과거를 간다.
* 과거에서 다 살피거나 작업을 한다.
* checkout을 master로 간다.



* git branch exp : exp라는 새로운 branch 생성
* git check out master
* git add master.txt
* git commit -m 'master 1'

=> exp1과 master1 2개의 branch 존재, master는 master1이라는 곳에 있음

* git reset -hard exp : exp로 마스터를 보냄

![image](https://user-images.githubusercontent.com/63588046/167067145-f3668b2d-3f38-4190-af9f-36899f835d2e.png)



## 원경 저장소 올리는법
* git push --set-upstream origin master : origin이라는 원격저장소를 올림
