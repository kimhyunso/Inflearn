# 1챕터
## 전역변수와 함수 (절차지향의 한계)
- 치명적 단점: 외부에서 직접 hp 수정 가능

```python
hero_name = "용사"
hero_hp = 100
hero_power = 10

monster_name = "슬라임"
monster_hp = 30
monster_power = 5

def attack(attacker_name, attacker_power, target_name, target_hp):
    print(f"{attacker_name}가 {target_name}을 공격! (데미지: {attacker_power})")
    target_hp -= attacker_power
    print(f"{target_name}의 남은 체력: {target_hp}")
    return target_hp

print("=== Step 1. 전역번수를 사용해서 실행 ===")
monster_hp = attack(hero_name, hero_power, monster_name, monster_hp)

print("=== 버그 발생: 마이너스 공격력으로 공격 ===")
monster_hp = attack(hero_name, -50, monster_name, monster_hp)
```

## 딕셔너리 구조체 (데이터 묶기)
- 문제점: 여전희 데이터와 함수가 분리되어있음 (데이터보호 약함)

```python
hero = {"name": "용사", "hp": 100, "power": 10}
monster = {"name": "슬라임", "hp": 30, "power": 5}

def attack_dict(attacker, target):
    print(f"{attacker['name']}가 {target['name']}을 공격! (데미지: {attacker['power']})")
    target['hp'] -= attacker['power']
    print(f"{target['name']}의 남은 체력: {target['hp']}")


print("=== Step 2. 딕셔너리를 사용해서 실행 ===")
attack_dict(hero, monster)
```

## 클래스 (객체지향 완성)
- 데이터와 행위를 한 단위로 만듦

```python
class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, target):
        print(f"{self.name}가 {target.name}을 공격! (데미지: {self.power})")
        # target.hp -= self.power <- 남의 데이터를 직접 수정하면 안 됨(캡슐화 위반)
        target.take_demage(self.power)

    def take_demage(self, power):
        if power < 0:
            print(f"오류: 잘못된 데미지 값입니다. ({power}) 데이터 보호됨!")
            return

        self.hp -= power
        print(f"{self.name}의 남은 체력: {self.hp}")

print("=== step3. 객체로 실행 ===")

p1 = Character("용사", 100, 10)
m1 = Character("슬라임", 30, 5)

p1.attack(m1)

p1.power = -50 # 누군가 실수로 공격력을 마이너스로 바꿈
print("[Test] 잘못된 공격력으로 시도")
p1.attack(m1) # take_damege 내부의 로직이 힐링 공격을 막아냄
```

# 2챕터

## self의 개념과 동작 원리

```python
class Lecture:
    def enroll(self, student):
        pass

# 우리가 쓰는 코드
lec.enroll("철수")

# 실제 실행되는 모습
Lecutre.enroll(lec, "철수")
```

## self가 없으면 오류가 나는 이유
- Type Error

```python
class Lecture:
    def __init__(self, title):
        self.title = title

    def print_into(self):
        print(f"정상 호출: 이 강의는 {self.title} 입니다.")

    def no_self_method():
        print("이 메시지는 객체로 호출하면 볼 수 없습니다.")

my_lec = Lecture("파이썬 기초")
my_lec.print_into()

# my_lec.no_self_method() 에러

Lecture.no_self_method()
```

## 클래스를 만든다는 것의 의미
1. 책임의 단위
2. 현실의 모델링
3. 새로운 타입

# 12챕터
## `__init__`과 `super()`
### `__init__`
- 객체가 메모리에 생성될 때 가장 먼저 호출되는 함수
- 데이터 세팅 필수 단계

### 오버라이딩 (Overriding)
- 부모의 생성자를 오버라이딩하면 자식의 생성자로 덮어씌어진다.

```python
class Parent:
    def __init__(self):
        self.money = 10000

class Child(Parent):
    def __init__(self):
        self.hobby = "게임"
```

### `super()`

```python
class Parent:
    def __init__(self):
        self.money = 10000

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.hobby = "게임"
```

# 13챕터
## Name Manglling (네임 맹글링)
- __변수명

```python
class Student:
    def __init__(self):
        self.__gpa = 4

s = Student()
# s.__gpa = 10 # 에러
```


## `@property`
- getter, setter

```python
class Student:
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, val):
        self.__gpa = val

s = Student()
# 변수처럼 실행하지만 메소드가 실행됨
s.gpa = 4.0
val = s.gpa
```

# 14챕터
## 다형성
- 같은 메시지, 다른 동작

## 다형성이 필요한 순간
- OCP 원칙 위반

```python
def pay(method):
    if methd == "CARD":
        print("카드 결제")
    elif methd == "BANK":
        print("계좌 이체")
    elif methd == "PAYPAL":
        print("페이팔")
    # 새로운 결제 추가 시 여기 또 수정 ...
```

## 1. 오버라이딩
- 부모 객체를 물려받아 자식의 방식대로 **재정의**

```python
class Payment:
    def pay():
        pass

class CreditCard(Payment):
    def pay():
        print("카드 긁기")

class BankTransfer(Payment):
    def pay():
        print("이체 하기")
```

## 2. Duck Typing
- 상속 없이도 메서드 이름만 같으면 됨
