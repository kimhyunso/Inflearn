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
        print(f'전설의 용사 {self.name}(이)가 탄생했습니다.')

    def take_item(self, item):
        print(f'[가방]: {self.name}은(는) [{item.name}]을 획득했습니다.')
        self.inventory.append(item)

    def show_status(self):
        print(f'\n[Hero] {self.name} LV: {self.level} HP: {self.hp} / {self.max_hp}, Power: {self.power}')
    
    def show_items(self):
        item_names = [item.name for item in self.inventory]
        print(f"    [가방]:  {item_names}")

    def use_potion(self):
        found_potion = None
        for item in self.inventory:
            if item.name == "빨간포션":
                found_potion = item
                break
        if found_potion:
            heal_amount = found_potion.recovery_amount
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

            print(f"    체력이 회복되었습니다. (HP: {self.hp}/ {self.max_hp})")

            self.inventory.remove(found_potion)
            print(f"{found_potion.name}을 사용했습니다.")
            return True
        else:
            print(f"사용할 수 있는 포션이 없습니다.")
            return False

class Item:
    def __init__(self, name, recovery_amount):
        self.name = name
        self.recovery_amount = recovery_amount
    

class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

        self.drop_item = None
        print(f"몬스터 {self.name}(이)가 나타났습니다.")

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
    hero = Hero("코딩용사", 200, 30)

    slime = Slime("초록슬라임", 50, 10)
    dragon = Dragon("레드드레곤", 100, 50)

    potion1 = Item("빨간포션", 30)
    potion2 = Item("보라포션", 100)

    num = random.randint(1, 2)
    if num == 1:
        slime.drop_item = potion1
    else:
        slime.drop_item = potion2

    # 전투 1
    battle(hero, slime)

    # 전투 2
    if hero.is_alive():
        input("\n(잠시 뒤 더 강력한 적이 나타납니다...)")
        time.sleep(1)
        battle(hero, dragon)

