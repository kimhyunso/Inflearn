import time, random

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power

    def attack(self, target):
        print(f'{self.name}의 공격!')
        damage = self.power
        target.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f'{self.name}은(는) {damage}의 데미지를 입었습니다. (HP: {self.hp} / {self.max_hp})')

    def is_alive(self):
        return self.hp > 0
    
    def show_status(self):
        print(f'{self.name} HP: {self.hp} / {self.max_hp}, Power: {self.power}')
    
class Hero(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

        self.level = 1
        self.inventory = []
        # print(f'전설의 용사 {self.name}(이)가 탄생했습니다.')

    def take_item(self, item):
        print(f'[가방]: {self.name}은(는) [{item.name}]을 획득했습니다.')
        self.inventory.append(item)

    def show_status(self):
        print(f'\n[Hero] {self.name} LV: {self.level} HP: {self.hp} / {self.max_hp}, Power: {self.power}')
    
    def show_items(self):
        item_names = [item.name for item in self.inventory]
        print(f"    [가방]:  {item_names}")

    def use_potion(self, selct_potion):
        found_potion = None
        for item in self.inventory:
            if item.name == selct_potion:
                found_potion = item
                break
            
        if found_potion:
            self.inventory.remove(found_potion)
            print(f"{found_potion.name}을 사용했습니다.")

            heal_amount = found_potion.recovery_amount
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

            print(f"    체력이 회복되었습니다. (HP: {self.hp}/ {self.max_hp})")
            return True
        else:
            print(f"사용할 수 있는 포션이 없습니다.")
            return False

class Item:
    def __init__(self, name, recovery_amount):
        self.name = name
        self.recovery_amount = recovery_amount

class GameManager:
    def __init__(self):
        self.hero = None
    
    def start_game(self):
        print("\n 텍스트 RPG: 전설의 시작")
        name = input("영웅의 이름을 입력하세요: ")
        self.hero = Hero(name, 100, 20)

        # 메인 루프
        while True:
            print("\n" + "=" * 30)
            print("[메인 메뉴]")
            print("1. 모험을 떠난다. (랜덤 이벤트)")
            print("2. 상태 확인")
            print("3. 종료")
            print("=" * 30)

            choice = input("선택 >>>")

            if choice == "1":
                self.explore()
            elif choice == "2":
                self.hero.show_status()
            elif choice == "3":
                print("게임을 종료합니다. 안녕히 가세요!")
                break
            else:
                print("잘 못된 입력값입니다.")
            
            # 게임 오버 체크
            if not self.hero.is_alive():
                print("당신은 사망하셨습니다. Game Over")
                retry = input("다시 하시겠습니까? 1. Yes 2. No")
                
                if retry == "1":
                    continue
                break

    def explore(self):
        print("숲속을 탐험하는 중...")
        time.sleep(1)

        dice = random.randint(1, 10)
        if dice <= 3: # 30%
            print("평화로운 바람이 붑니다. 아무 일도 일어나지 않았습니다!")
        elif dice <= 8: # 50%
            print("덤불 속에서 무언가 튀어나왔습니다.")
            if random.random() < 0.8: # 80% 확률
                monster = Slime("슬라임", 30, 5)
                drop_item = None
                if random.randint(1, 2) == 1:
                    drop_item = Item("빨간포션", 30)
                else:
                    drop_item = Item("보라포션", 100)
            else: # 20% 확률
                monster = Dragon("레드드레곤", 80, 15)
                drop_item = Item("보라포션", 100)
            monster.drop_item = drop_item

            self.battle(monster)
        else: # 20%
            print("길가에서 반짝이는 것을 발견했습니다.")
            drop_item = None
            if random.random() < 0.8:
                drop_item = Item("빨간포션", 30)
            else:
                drop_item = Item("보라포션", 100)
            self.hero.take_item(drop_item)

    def battle(self, monster):
        print(f"\n 야생의 '{monster.name}'(이)가 나타났다!")
        print(f"  (HP: {monster.hp}, 공격력: {monster.power})")

        # 전투 루프
        while self.hero.is_alive() and monster.is_alive():
            print("-" * 30)
            self.hero.show_status()

            print("\n[선택하세요]")
            print("1. 공격 2. 아이템 확인 3 아이템 사용 4. 도망치기")
            choice = input(">>> ")

            turn_ended = False # 턴 소모 여부 체크

            if choice == "1":
                self.hero.attack(monster)
                turn_ended = True
            elif choice == "2":
                self.hero.show_items()
                continue
            elif choice == "3":
                self.hero.show_items()
                select_potion = input("포션이름을 입력해주세요: ")
                if self.hero.use_potion(select_potion):
                    turn_ended = True
                else:
                    turn_ended = False
            elif choice == "4":
                print(f" 무사히 도망쳤습니다.")
                break
            else:
                print("잘못된 입력입니다.")
                continue

            if not monster.is_alive():
                print(f"\n {monster.name}을(를) 물리쳤습니다!")
                if monster.drop_item:
                    self.hero.take_item(monster.drop_item)
                    print(f"{monster.drop_item.name}을 획득했습니다.")
                break
        
            if turn_ended:
                time.sleep(1)
                print("\n 몬스터의 반격!")
                monster.attack(self.hero)

class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

        self.drop_item = None
        # print(f"몬스터 {self.name}(이)가 나타났습니다.")

class Slime(Monster):
    def attack(self, target):
        print(f'{self.name}의 몸통박치기! (물컹)')
        damage = self.power
        target.take_damage(damage)

class Dragon(Monster):
    def attack(self, target):
        print(f'{self.name}이(가) 불을 뿜습니다! (크리티컬)')
        damage = int(self.power * 1.5)
        target.take_damage(damage)


# 전투 시스템(메인 로직)
def battle(hero, monster):
    print(f"\n 야생의 '{monster.name}'(이)가 나타났다!")
    print(f"  (HP: {monster.hp}, 공격력: {monster.power})")

    # 전투 루프
    while hero.is_alive() and monster.is_alive():
        print("-" * 30)
        hero.show_status()

        print("\n[선택하세요]")
        print("1. 공격하기")
        print("2. 아이템 확인하기")
        print("3. 아이템 사용하기")
        print("4. 도망치기")
        choice = input(">>> ")

        turn_ended = False # 턴 소모 여부 체크

        if choice == "1":
            hero.attack(monster)
            turn_ended = True
        elif choice == "2":
            hero.show_items()
            continue
        elif choice == "3":
            if hero.use_potion():
                turn_ended = True
            else:
                turn_ended = False
        elif choice == "4":
            print(f" 무사히 도망쳤습니다.")
            break
        else:
            print("잘못된 입력입니다.")
            continue

        if not monster.is_alive():
            print(f"\n {monster.name}을(를) 물리쳤습니다! 승리")
            if monster.drop_item:
                hero.take_item(monster.drop_item)
                print(f"{monster.drop_item.name}을 획득했습니다.")
            break
    
        if turn_ended and monster.is_alive():
            time.sleep(1)
            print("\n 몬스터의 반격!")
            monster.attack(hero)

            if not hero.is_alive():
                print(f"\n 당신은 죽었습니다... 게임 오버.")
                break


if __name__ == "__main__" :
    # hero = Hero("코딩용사", 200, 30)

    # slime = Slime("초록슬라임", 50, 10)
    # dragon = Dragon("레드드레곤", 100, 50)

    # potion1 = Item("빨간포션", 30)
    # potion2 = Item("보라포션", 100)

    # num = random.randint(1, 2)
    # if num == 1:
    #     slime.drop_item = potion1
    # else:
    #     slime.drop_item = potion2

    # # 전투 1
    # battle(hero, slime)

    # # 전투 2
    # if hero.is_alive():
    #     input("\n(잠시 뒤 더 강력한 적이 나타납니다...)")
    #     time.sleep(1)
    #     battle(hero, dragon)
    game = GameManager()
    game.start_game()

