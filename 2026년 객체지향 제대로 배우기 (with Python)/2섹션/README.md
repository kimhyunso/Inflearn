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
