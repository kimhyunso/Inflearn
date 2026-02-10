기초 탄탄! 독하게 시작하는 Java - Part1

## 절차적 프로그래밍 - 배운 내용 정리
1. Lookup 배열
2. Event Loop
3. Call by Value, Call by Reference
4. Recursive Call
5. Bubble Sort, Selection Sort
6. Shallow Copy, Deep Copy
7. 항 -> 식 -> 구문 -> 메소드
8. Call Stack

## Lookup 배열
경우의 수가 많아 질 경우 배열을 선언하여 하나의 값을 찾도록 만드는 것

## Event Loop
사용자가 입력한 Event를 상시 Listener가 listen하여 특정 함수를 실행하는 것(callback함수 실행) 

## Call by Value, Call by Reference
primitive type을 함수의 파라미터로 전달 후, 파라미터의 값을 변경하면 해당 인스턴스가 다르기 때문에 변경되지 않음

참조형 자료(ex 배열, ArrayList)를 함수의 파라미터로 전달 후, 파라미터의 값을 변경한다면 원본 자료가 바뀜

## Recursive Call
자기 자신을 호출하는 함수

## Bubble Sort, Selection Sort
데이터들을 정렬하는 기법 `O(N^2)`

## Shallow Copy, Deep Copy
참조형 자료들을 대입연산자(=)로 copy 했을 시에 copy한 자료를 변경하면 origin의 자료도 같이 변경됨 - Shallow Copy

이유는 heap 메모리의 같은 주소를 참조하기 때문

Deep Copy는 참조자들이 해당 인스턴스를 참조할 때, 다른 힙 영역을 참조하게 만듬

## 항, 식, 구문
항들이 모여 식이되고 식이 모여 구문이됨 구문이 모여 함수가 됨

x, y (항들) x + y (식) {x + y, x - y}

func() -> {x + y, x - y}

## Call Stack
함수를 호출할 때 stack의 구조를 따라 먼저 들어간 함수가 나중에 호출된다(FILO)

