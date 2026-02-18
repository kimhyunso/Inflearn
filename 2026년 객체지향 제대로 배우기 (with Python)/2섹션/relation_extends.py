# Is-a 관계
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def login(self):
        print(f"[Member] {self.name}님이 로그인했습니다.")

class Student(Member):
    def study(self):
        print(f"[Study] {self.name}님이 공부를 합니다.")

class Instructor(Member):
    def teach(self):
        print(f"[Instructor] {self.name}님이 강의를 합니다.")

# Has-a 관계
class Material:
    def __init__(self, content):
        self.content = content
    
    def download(self):
        print(f"다운로드 중: {self.content}")

class Lecture:
    # def __init__(self, title):
    #     self.title = title
    #     # 강의는 자료를 가짐 (Lectrue has a Material)
    #     # 생성자에서 부품 객체를 생성하여 소유
    #     self.material = Material(title + "_강의자료.pdf")

    # 외부에서 주입받는 경우 (DI)
    def __init__(self, title, material):
        self.title = title
        # 강의는 자료를 가짐 (Lectrue has a Material)
        # 생성자에서 부품 객체를 생성하여 소유
        self.material = material

    def show_material(self):
        print(f"[{self.title}] 자료 확인:")
        self.material.download() # 내 기능이 아닌 부품에게 위임

s = Student("철수", "s001")
s.login()
s.study()

i = Instructor("hong", "h002")
i.login()
i.teach()

# python_lec = Lecture("파이썬기초")
# python_lec.show_material()

# java_lec = Lecture("자바기초")
# java_lec.show_material()

# 외부에서 주입받는 경우
python_lec = Lecture("파이썬기초", Material("파이썬기초_강의자료.pdf"))
python_lec.show_material()

java_lec = Lecture("자바기초", Material("자바기초_강의자료.pdf"))
java_lec.show_material()