class Character:
    def __init__(self, name, hp, attack_power):
        self.nmae = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power

        if target.hp < 0:
            target.hp = 0

        print(f"{self.name}가 {target.name}을 공격했습니다.")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name}가 {amount}만큼 회복했습니다.")

    def show_info(self):
        print(f"{self.name}의 남은 체력: {self.hp}")

hero = Character("용사", 100, 30)
monster = Character("슬라임", 50, 10)

hero.attack(monster)
monster.show_info()

monster.attack(hero)
hero.heal(20)
hero.show_info()