class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


s = Student("철수", 4.0)
print(f"[변경 전] 이름: {s.name}, 학점: {s.gpa}")

s.gpa = 99
print(f"[변경 후] 이름: {s.name}, 학점: {s.gpa}")

class StudentCapsule:
    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa

    @property
    def name(self):
        return self.__name
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if value < 0.0 or value > 4.5:
            print(f"오류: 학점은 0.0 ~ 4.5 사이여야 합니다. (입력값: {value})")
            return

        self.__gpa = value
        print(f"학점이 {value}로 안전하게 수정되었습니다.")


sc = StudentCapsule("철수", 4.0)
print(f"[변경 전] 이름: {sc.name}, 학점: {sc.gpa}")

sc.gpa = 99 # 오류
print(f"[변경 후] 이름: {sc.name}, 학점: {sc.gpa}")

sc.gpa = 3.5
print(f"[변경 후] 이름: {sc.name}, 학점: {sc.gpa}")
