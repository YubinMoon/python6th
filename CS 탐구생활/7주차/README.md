# CS 탐구생활 5주차

팀원: 황주원, 김준영, 문유빈, 임정택, 최선우

## 주제

- [인터넷](https://thecrashcourse.com/courses/the-internet-crash-course-computer-science-29/)

## INTERNET PROTOCOL

인터넷 패킷은 IP를 준수해야 한다. 

### UDP(User Datagram Protocol)

네트워크 통신에서 신뢰적인 연결방식  
흐름제어와 혼잡제어로 수신 버퍼의 오버플로우를 방지하고 안정적인 데이터 전송을 유지한다.

### TCP(Transmission Control Protocol)

비연결형, 신뢰성 없는 전송 프로토콜  
UDP의 결정적인 장점은 데이터의 신속성이다. 데이터의 처리가 TCP보다 빠르다.  
주로 실시간 방송과 온라인 게임에서 사용된다. 네트워크 환경이 안 좋을때, 끊기는 현상을 생각하면 된다.

### DNS(Domain Name System)

모든 통신은 IP를 기반으로 연결된다. 하지만 사용자에게 일일히 IP 주소를 입력하기란 UX적으로 좋지 않다  
때문에 DNS 가 등장 했으며 DNS 는 IP 주소와 도메인 주소를 매핑하는 역할을 수행한다

DNS는 UDP를 사용하는데 그 이유는 데이터의 크기가 크지 않고, 연결을 유지할 필요가 없으며, 손실은 application에서 처리 가능하다.  
다만 크기가 512를 넘어가면 TCP를 사용해야 한다.

### HTTP (HyperText Transfer Protocol)

인터넷에서 하이퍼텍스트 문서인 HTML로 만든 웹페이지를 전송하기 위해 사용되는 어플리케이션 계층 프로토콜  

웹페이지는 객체들로 구성되어 있으며 객체는 파일, 이미지 등을 의미한다.  
HTTP는 TCP를 사용하며 80번 포트에서 동작한다.  
과거에는 각각의 객체를 가져올 때마다 새로운 TCP연결을 했지만 지금은 한번의 연결로 여러개의 객체를 가져온다. 이를 지속 연결이라고 한다.  

두 종류의 HTTPS 메시지가 있다.

**request**  
클라이언트가 서버에 요청하기 위한 메시지 형식이다.  
request line에 메소드 종류, 서버의 주소, HTTP version 등이 들어간다.  
header lines에 줄바꿈을 기준으로 key: value 형식으로 헤더가 들어간다.  
헤더에서 줄바꿈을 두번 한 뒤에 body가 들어간다.  

**response**  
서버에서 클라이언트에 반환하기 위한 메시지 형식이다.  
status line에 프로토콜, 응답 코드, 응답 메시지 가 들어간다.  
header lines에 위와 같이 들어가는데 서버와 데이터의 정보가 추가되어 반환된다.  
마찬가지로 body 또한 들어간다.  