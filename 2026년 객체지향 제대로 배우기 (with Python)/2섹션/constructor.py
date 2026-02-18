class Parent:
    def __init__(self):
        self.money = 10000

parent = Parent()
print(f"{parent.money}")

# 오류: 부모의 생성자를 오버라이딩해서 money라는 데이터를 없앰
# class Child(Parent):
#     def __init__(self):
#         self.hobby = "게임"
        
# child = Child()
# print(f"{child.money}")


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.hobby = "게임"
        
child = Child()
print(f"{child.money}")



