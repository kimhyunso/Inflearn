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

## 상속과 포함의 권장 설계 원칙
- 상속 보다는 포함을 우선하라

### 상속의 문제점
1. 부모의 구현 의존
2. 유연성 부족
3. 클래스 폭발

### 포함의 장점
1. 블랙박스 재사용
2. 런타임 교체
3. 단순성

## 객체 지향의 핵심
~~거대한 상속 계층 만들기~~가 아닌 **적절한 책임을 나누고 조립하기**
- 상속은 정말 확실한 Is-a 관계일 때만 사용하기

**모든 객체가 Is-a, Has-a (구조적) 관계를 맺을 필요는 없다**

## 객체지향 4대 요소
1. 추상화
2. 캡슐화
3. 상속
4. 다형성

# 5챕터

## 추상화: 핵심만 남긴다
- 공통적이고 본질적인 특징만 추출

## 캡슐화: 감추기

```python
class Account:
    def __init__(self):
        self.__money = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__money += amount
```

## 상속: 물려받기
- 부모: 일반적 / 자식: 구체화
- 주의: Is-a 관계가 확실할 때에만 사용해야함

## 다형성: 갈아끼우기
- 동일한 메시지에서 다른 동작
- 같은 메서드를 호출해도 객체마다 다르게 동작하는 것
- 캐릭터 -> Attack() -> 전사: 칼을 휘두름, 마법사: 불을 던짐

## 문맥에 따른 추상화의 차이
- 똑같은 사람이라도 어떤 프로그램이냐에 따라 달라짐
- 병원: 몸무게, 키, 혈액형 데이터 필요 / 은행: 신용등급, 통장번호 데이터 필요

# 6챕터

## 캡슐화: 보호와 책임
- 정보 은닉
1. 데이터 보호
2. **무결성 보장**: 유효하지 않은 값 차단
* 무결성: 데이터가 결함이 없는것

```python
class Account:
    def __init__(self):
        self.__money = 0
    
    def deposit(self, amount):
        if amount < 0:
            print("마이너스 입금 불가!")
            return
        self.__money += amount
```

# 7챕터

## 다양성
- 같은 메서드 호출
- 다른 동작
- 다른 결과
- if-else 제거, 확장하기 쉬운 코드를 만듦

## **오버라이딩**
- 부모가 물려준 기능을 내 방식대로 재정의함

### 절차지향 코드 (Bad)

```python
def attack(character):
    if character.type == "Warrior":
        print("대검 베기!")
    elif character.type == "Mage":
        print("파이어볼!")
    elif character.type == "Archer":
        print("연속 화살!")
```

## 객체지향 (Good)

```python
def attack(character):
    character.attack()
```

## 다형성의 효과: 확장성
- OCP: 개방-폐쇄 원칙

## 파이썬의 다형성: 오리 타이핑 (Dock Typing)
- 파이썬은 상속 없이도 다형성이 가능함

```python
class Dog:
    def speak(self):
        print("멍멍")

class Cat:
    def speak(self):
        print("야옹~")

class Robot:
    def speak(self):
        print("삐리리~")

objs = [Dog(), Cat(), Robot()]

for o in objs:
    o.speak()
```

# 챕터8

## SOLID
- 객체지향 설계 5원칙

### 나쁜 설계
- 하나 고치면 다 고장남 (경직성)
- 어디가 문제인지 모름 (취약성)
- 재사용 불가능 (부동성)

### 좋은 설계
- 변경에 유연함 (유연성)
- 수정해도 쉽게 깨지지 않음 (안정성)
- 재사용 가능한 구조 (재사용성)

## SRP: 단일 책임원칙
- **하나는 하나만 해라**

### Bad: 맥가이버 칼 (God Class)

```
class User:
- 로그인()
- 이메일 보내기()
- 데이터베이스 저장()
- 로그 남기기()
```

### Good: 전문가 도구

```
class User(데이터만)
class EmailSender(전송만)
class UserRepository(DB만)
```

## OCP: 계방-폐쇠 원칙
- **확장에 열려있고, 변경에는 닫혀있어야함**

### 나쁜 코드

```python
if type == "Dog": 
    bark()
elif type == "Cat":
    meow()
```

### 좋은 코드

```python
animal.speak()
```

## LSP: 리스코프 치환 원칙
- 자식클래스는 부모 클래스를 **대체**할 수 있어야함

### 대표 위반 사례: 펭귄
- 펭귄은 날지 못함

```python
class Bird:
class Penguin(Bird):
```

## ISP: 인터페이스 분리 원칙
- 내가 사용하지 않는 기능에 의존하게 만들지 마라
- **인터페이스는 작고 목적에 맞게 나누는게 더 좋다**
- **안 쓰는 건 강요 말라**

### Bad: 범용 인터페이스
- 복합기 기능
1. print()
2. scan()
3. fax()

### Good: 인터페이스 분리
- 필요한 기능만 골라쓰기
- Printer.print()
- Scanner.scan()

## DIP: 의전 역전 원칙
- **구체적인 것이 아닌 추상적인 것에 의존하라**

> 로봇이 특정 건전지에 의존한다면 특정건전지가 단종되었을 때, 문제가 발생함
> 따라서, 로봇은 건전지 규격(AA 사이즈)를 의존하는 것이 좋음 - 배터리가 무엇이든 쉽게 갈아끼울 수 있음

```python
# 추상화 (Interface/Abstract Class)
class Battery:
    def use(self):
        pass

# 구체적인 구현
class Energizer(Battery):
    def use(self):
        print("에너자이저 파워")

class Robot:
    def __init__(self, battery:Battery):
        self.battery = battery
    
    def operate(self):
        self.battery.use()


robot = Robot(Energizer()) 
robot.operate()
```



