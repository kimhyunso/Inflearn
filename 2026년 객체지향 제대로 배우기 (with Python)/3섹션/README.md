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