# 기계 중심 프로그래밍 -> 절차 지향 프로그래밍 -> 구조적 프로그래밍 -> 객체 지향 프로그래밍

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






