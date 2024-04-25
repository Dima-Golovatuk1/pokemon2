class Pokemon:
    name = "pokemon"
    attack = 0
    speed = 0
    hp = 0

    def __init__(self, name, attack, speed, hp, ):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.hp = hp
        print(f"Pokemon:\nname: {name}\nattack power: {attack}\nspeed: {speed}\nHP: {hp}\n")


    def take_damage(self, damage):
        self.hp -= damage
        print(f"Покемон {self.name} оримав {damage} пошкоджень")
        print(f"Залишилося{self.hp}% здоров'я")

    def attack(self, enemy):
        print(f"{self.name} hit {enemy} for {self.attack} damage\n")
        enemy.take_damage(self.attack)


class Fire(Pokemon):
    def fireball(self):
        print(f"{self.name}'s fireball hits for\n"
        f"{self.attack * 2} damage\n"
        f"({self.attack * 2} damage)\n")


charmeleon = Fire("Charmeleon", 25, 15, 70)
bulboZaur = Fire("bulboZaur", 15, 5, 250)
charmeleon.attack(bulboZaur)

