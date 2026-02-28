# 게임의 컨셉
- 사용자가 영웅, 몬스터를 물리치며 성장하는 게임

1. 전투 (공격, 방어, 스킬 - 다형성 활용)
2. 아이템 (포션 획득 및 사용 - 포함관계)
3. 성장 (경험치 획득 및 레벨업 - 데이터캡슐화)

```
Character(부모)
- name: str
- hp: int
- power: int
---
+ attack(target)
+ take_demage(amount)

Hero(자식)
- inventory: int
---
+ attack() [재정의]
+ eat(item)
+ show_status()

Monster(자식)
- drop_item: Item
---
+ attack() [재정의]
```

## 핵심 로직 흐름
- GameManager

1. 게임 시작: 영웅 이름 입력받기
2. 메인 루프 (`While True`):
   1. 몬스터가 랜덤하게 등장
   2. 전투 루프: (공격/도망) 선택
   3. 몬스터 처치 시 보상 획득
   4. 영웅 사망 시 게임 종료 (`Break`)

## 객체지향 핵심
1. Class & Object - 영웅, 몬스터 객체 생성
2. 상속 - Character 상속 구현
3. 다형성 - `attack()` 메서드 재정의
4. 캡슐화 - HP 등 데이터 보호

## 아이템 흐름 flow
1. 몬스터 처치 (드랍 아이템 확인)
2. 아이템 획득
3. 아이템 사용

## 문제: 오버힐 방지
- 체력은 최대 체력을 넘을 수 없습니다.
- 캡슐화로 방지

### 잘못된 로직

```python
def use_potion(self):
   self.hp += 30
```

### 올바른 로직

```python
def use_potion(self, amount):
   self.hp += amount
   if self.hp > self.max_hp:
      self.hp = self.max_hp
```

## 아이템 시스템 구현하기
1. Item 클래스: 이름과 회복량을 가진 객체 생성
2. 인벤토리: 영웅이 아이템을 획득하고 관리하는 리스트 구현
3. 안전한 회복: max_hp를 넘지 않도록 체력 회복 로직 구현

## 게임의 완성
### GameManager와 메인루프 만들기
- GameManager: 오케스트라의 지휘자
1. Hero 생성: 이름 입력받기
2. 전투 관리: `battle()` 호출
3. 종료 처리: 게임 오버 판정

### 게임루프
1. 게임 시작 (영웅 생성)
2. Loop
3. 메뉴 선택 (탐험 / 상태 / 종료)
4. 랜텀 이벤트 발생 (전투 or 아이템)
5. 결과 처리 (경험치, 체력 확인)
6. 게임 종료

### 랜덤 인카운터
- `random.randint(1, 10)`
- 1 ~ 3: 아무 일도 없음
- 4 ~ 8: 몬스터 출현
- 9 ~ 10: 보물상자 발견