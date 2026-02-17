class Lecture:
    def __init__(self, title, teacher, price):
        self.title = title
        self.teacher = teacher
        self.price = price
        self.students = []

    def info(self):
        print(f"강의 정보: {self.title} (강사: {self.teacher})")

class Student:
    def __init__(self, name):
        self.name = name
        self.my_lectures = []

    def study(self):
        print(f"\n {self.name}님이 공부를 시작합니다")
        for lecture in self.my_lectures:
            print(f" - {lecture.title} 복습 중...")

class CourseSystem:
     def resister_course(self, student, lecture):
        print(f"\n [System] 수강 신청 처리 중... (신청자: {student.name}, 강의: {lecture.title})")

        # 개선점
        student.my_lectures.append(lecture) # 직접접근
        lecture.students.append(student) # 직접접근

        print("-> 등록이 완료되었습니다.")




my_system = CourseSystem()

python_lec = Lecture("파이썬 기초", "abcd", 50000)
java_lec = Lecture("자바의 정석", "abcd", 70000)

student1 = Student("철수")
student2 = Student("영희")

my_system.resister_course(student1, python_lec) # 철수 -> 파이썬
my_system.resister_course(student2, python_lec) # 영희 -> 파이썬
my_system.resister_course(student1, java_lec) # 철수 -> 자바

student1.study()
student2.study()

print()
for s in python_lec.students:
    print(f"- {s.name}")