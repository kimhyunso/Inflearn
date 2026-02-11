# 1, 2챕터
## 기계 중심 프로그래밍 -> 절차 지향 프로그래밍 -> 구조적 프로그래밍 -> 객체 지향 프로그래밍

## 객체 지향 프로그래밍
- 데이터와 기능을 분리한다
- 현실세계 모델링(데이터, 행위)

## 절차 지향 VS 객체 지향
### 절차 지향
- **데이터와 기능(함수)이 분리됨 (데이터는 함수 외부에 존재하며 여러 함수에서 접근)**
- 구조가 단순
- 실행속도 빠름
- 데이터 무결성 보장 어려움

### 객체 지향
- **데이터와 행위가 하나의 객체로 캡슐화되어 외부로부터 보호됨**
- 유지보수성 높음
- 런타임 오버헤드 약간 존재

## 절차지향 Pseudo-code
- 온라인 강의를 수강하는 예시

- **전역 변수들 - 모든 함수가 공유 (위험!)**
```python
python_title = "파이썬으로 시작하는 프로그래밍"
python_capacity = 30
python_students = []

java_title = "자바 기초부터 실전까지"
java_capacity = 25
java_students = []

function pritLectureInfo(lecture_name)
    if lecture_name == "python"
        print("파이썬 강의 - 정원: " + python_capacity + "명 (현재 " + len(python_students) + "명)")
    else if lecture_name == "java"
        print("자바 강의 - 정원: " + java_capacity + "명 (현재 " + len(java_students) + "명)")

function enroll(student_name, lecture_name)
    if lecture_name == "python"
        if len(python_students) >= python_capacity
            print("파이썬 강의 정원 마감")
            return
        python_students.append(student_name)
        print(student_name + "님이 파이썬 강의 신청 완료")
    else if lecture_name == "java"
        # 버그 실수로 python_capacity 체크함
        if len(java_students) >= python_capacity
            print("자바 강의 정원 마감")
            return
        java_students.append(student_name)
        print(student_name + "님이 자바 강의 신청 완료")

# 문제 발생!
enroll("홍길동", "python")
enroll("홍길동", "java")
printLectureInfo("python")
printLectureInfo("java")

# 자바 강의 신청 시 실수로 파이썬 정원 체크하는 버그 발생
# 만일 자바 강의 신청 시 실수로 파이썬 신청학생 목록을 업데이트 한다면?
# 전역 변수가 많아지면 이런 실수가 쉽게 일어나고 발견하기 어려움
```

## 객체 지행 Pseudo-code
```python
class Lecture
    private title
    private capacity
    private students = []

    constructor(title, capacity)
        this.title = title
        this.capacity = capacity
    
    method printInfo()
        print(this.title + " - 정원: " + this.capacity + "명 (현재 " + this.students.length + "명)")
    
    method enroll(student)
        if this.students.length >= this.capacity
            print(this.title + " 정원 마감")
            return false
        this.students.append(student)
        print(student.name + "님이 " + this.title + " 신청 완료")
        return true

class Student
    private name
    private enrolledLectures = []

    constructor(name)
        this.name = name
    
    method enrollIn(lecture)
        success = lecture.enroll(this) # 객체 간 메시지 전달
        if success
            this.enrolledLectures.append(lecture)
    
    method printMyLectures()
        print(this.name + "님의 수강 강의:")
        for each lecture in this.enrolledLectures
            print(" - " + lecture.title)

pythonLecture = new Lecture("파이썬으로 시작하는 프로그래밍", 30)
javaLecture = new Lecture("자바 기초부터 실전까지", 25)

hong = new Student("홍길동")

hong.enrollIn(pythonLecture) # 홍길동이 파이썬 강의에게 신청 메시지를 보냄
hong.enrollIn(javaLecture)

pythonLecture.printInfo()
javaLecture.printInfo()
hong.printMyLectures()
```

# 3챕터

- 절차지향 문제점: 데이터와 기능이 분리됨
- 객체지향 해결점: 데이터 + 기능(행위) = 하나의 객체(Object)

## 클래스란 무엇인가
class = 개념 (설계도, 틀)
```python
class Student:
    __name
    __age
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
```

object = 실체 메모리에 존재 (실체)
```python
hong = Student("홍길동", 25)
```

## 클래스 구성요소
- 데이터 (속성)
- 행위 (메서드)
- 생성자

## 클래스를 만드는 것의 진짜의미
1. 책임단위
   1. 흩어진 데이터와 행위를 하나로 묶음(캡슐화)
2. 현실의 모델링
   1. 실세계의 문제를 추상화
3. 새로운타입
   1. 새상에 없는 자료형을 창조하는 것

## 클래스와 객체의 관계
클래스: 하나의 설계도 -> 객체: N개의 제품 (독립적)

## 메모리 구조
- 같은 클래스라도 객체로 만들어지면 다른 메모리 주소를 가짐

## 온라인 강의 시스템
```python
# 클래스 정의
class Lecture:
    def __init__(self, title):
        self.title = title
        self.teacher = "hong"
    def get_info(self):
        return f"{self.title}"

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
    def study(self):
        self.progress += 10

# 객체 생성
my_lecture = Lecture("파이썬 기초")
hong = Student("hong")
```

## 객체 간의 대화
객체지향 세계에서는 함수 호출을 `메시지를 보낸다`고 한다.
- Student가 Lecture에게 강의정보를 달라고 요청함

# 4챕터
- Is-a와 Has-a

## Is-a 관계
~은 ~의 일종이다 (상속/계층 관계)

## Has-a 관계
~은 ~을 가진다 (포함/구성 관계)

## Is-a 관계: 상속
- Student **is a** Person
- Dog **is a** Animal

1. 부모는 일반적인 개념
2. 자식은 구체적인 개념
3. 자식은 부모의 속성과 행동을 물려받음
4. 목적: 코드 재사용 및 계층 구조 표현

```python
# 일반적 개념
class Person:
    def eat(self):
        print("밥을 먹습니다.")

# 구체적 개념
class Student(Person):
    def study(self):
        print("공부를 합니다.")

s = Student()
s.eat()
s.study()
```

## 잘못된 상속 관계
현실 세계의 분류와 is a 관계가 완전 일치하지 않는다.

is a 관계는 부모타입으로 완전 대체가 가능한지 확인해야함

- 경찰 is a 총
- 펭귄 is a 새

## Has-a 관계: 포함
- Car has a Engine
- Police has a Gun

1. 전체와 부품관계
2. 상속보다 유연한 결합
3. 내 기능을 내가 직접하지 않고, 부품에게 시킴 (위임)
4. 목표: 객체를 조립하고, 역할을 분리하여 변경에 유연한 구조를 만든는 것

```python
# 부품 클래스
class Engine:
    def start(self):
        print("부릉! 엔진 가동")

# 전체 클래스
class Car:
    def __init__(self):
        self.engine = Engine()
    
    def drive(self):
        self.engine.start()
        print("출발합니다")

my_car = Car()
my_car.drive()
```

## Has-a의 두 가지 얼굴
결합강도와 생명주기에 따라 두 가지 형태를 띔

1. 합성 관계 (강한 결합)
    - 예시: 사람 & 심장
    - 사람이 죽으면 심장도 멈춤 (생명주기 동일)
    - 부품이 전체에 완전 종속된 관계

2. 집합 관계 (약한 결합)
    - 예시: 학교 & 학생
    - 학교가 사라져도 학생을 살아있다 (생명주기 독립)

> 전체가 사라지면 부품도 함께 사라져야하는가

## Is-a vs Has-a
### Is-a (상속)
- 결합도: 강함
- 수직적 (계층 구조)

```python
class Person:
    ...
class Student(Person):
    ...
```

### Has-a (포함)
- 결합도: 유연함
- 수평적 (조립 구조)

```python
class Gun:
    ...

class Police:
    # 멤버 변수로 객체 소유
    def __init__(self):
        self.gun = Gun()
    # 외부에서 전달받음
    def __init__(self, gun):
        self.gun = gun
```



