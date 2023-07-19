# CS 탐구생활 4주차

팀원: 이진호, 문유빈, 김민혁, 한민호

## 주제

- [CPU](https://thecrashcourse.com/courses/the-central-processing-unit-cpu-crash-course-computer-science-7/)

## CPU

### 용어

RAM: 실행할 프로그램의 기계어나 데이터가 저장되어 있다.  
REGISTER: CPU 내부에 있는 메모리로 연산에 필요한 데이터를 임시로 저장한다.

`INSTRUCTION ADDRESS REGISTER`또는 `PC(Program Counter)`는 REM에서 가져올 다음 명령의 주소를 저장한다. 이를 통해 CPU는 명령을 순서대로 실행할 수 있다.  
`INSTRUCTION REGISTER`는 메모리에서 가져온 현재 실행중인 명령을 저장한다.

기계어는 CPU가 직접 실행할 수 있는 2진수로 된 명령이며 `INSTRUCTION`이라고도 한다.

CPU 아키텍처마다 사용하는 `INSTRUCTION`이 다르지만 보통 OPCODE와 ADDRESS로 구성된다.  
아래는 MIPS 아키텍처의 `INSTRUCTION`이 어떻게 구성되어 있는지 보여준다.  
[MIPS_GREEN_SHEET.pdf](https://inst.eecs.berkeley.edu/~cs61c/resources/MIPS_Green_Sheet.pdf)

### 동작 순서

1. FETCH  
  `INSTRUCTION ADDRESS REGISTER`에 저장된 주소로 메모리에서 명령을 가져와 `INSTRUCTION REGISTER`에 저장한다.

2. DECODE  
  가져온 `INSTRUCTION`을 해석한다.
  `INSTRUCTION`에서 OPCODE나 ADDRESS는 사용하는 비트 수가 정해져 있기에 비트 연산을 통해 해석할 수 있다.  

3. EXECUTE  
  해석된 `INSTRUCTION`을 실행한다.  
  `OPCODE`에 따라 RAM에서 값을 읽거나 쓸 수 있다. 이때 `INSTRUCTION`에 메모리의 위치와 `REGISTER`의 위치가 저장되어 있어 가능하다.  
  또 `ALU`를 사용해 `REGISTER`에 저장된 값을 연산할 수 있다. 이때 `INSTRUCTION`에 피 연산자인 두 `REGISTER`의 위치와 `ALU`가 수행할 연산의 종류가 저장되어 있다.  
  연산의 결과는 보통 첫 번째 `REGISTER`에 저장된다.  
  마지막으로 다음 명령어를 실행하기 위해 `INSTRUCTION ADDRESS REGISTER`에 저장된 주소를 1 증가시킨다.

4. WRITE BACK
  영상에선 설명하지 않지만 명령어대로 처리 완료된 데이터를 메모리에 기록하는 단계도 따로 있다. 

## CLOCK

CPU는 각 단계를 수행하는데 시간이 걸린다.  
그래서 cpu가 각 단계를 순서대로 실행할 수 있도록 `CLOCK`이 추가됐다.  
cpu가 각 단계를 수행하는 속도를 `clock speed` 라고 한다. 
단위는 Hz를 사용한다. 요즘 CPU는 N GHz 단위로 동작한다.  
이번에 인텔 6 GHz가 가장 빠른 CPU로 알고있다. 

오버클럭을 통해 CPU의 실행 속도를 높일 수 있지만 CPU의 발열이 더 심해지고 연산에 걸리는 시간보다 clock이 빨라지면 오동작할 수 있다.

언더클럭으로 CPU의 실행 속도를 낮춰 발열과 전련 소모를 줄일 수 있다.

요즘 프로세서들은 `clock speed`를 조절할 수 있는데 이를 `dynamic frequency scaling(동적 주파수 스케일링)`이라고 한다.


