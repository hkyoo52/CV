#### 가상화
* 개발할때 서버에 직접 개발 X (Local 환경에서 개발, Staging 서버에서 완료, Production 서버에서 배포)
* Local 환경과 Production 환경이 다를 수 O, 같아도 서버에서 올바르게 작동 X 가능
* 가상화 : 특정 소프트웨어 환경을 만들고 Local, Production 서버에서 그대로 사용
* VM(Virtual Machine) : 실제 물리적 컴퓨터위에 OS를 포함한 가상화 소프트웨어를 두는 방식
* 그러나 OS위에 OS 하나 더 실행시키면 VM은 무거워짐=> Container : VM 무거움 크게 덜어주면서 가상화를 좀더 가볍게 함

#### Docker
* Container 기술을 쉽게 사용할 수 있게 함
* Docker Image : 컨테이너 실행할 때 사용하는 '탬플릿', Read Only, 수정X (PC방에서 프로그램 깔아도 재부팅시 원상태로 복구)
* Docker Container : Docker Image 활용해 실행된 인스턴스, 




