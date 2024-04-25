class Pokemon:
    name = "name"
    power = 1
    speed = 1
    hp = 1

    def __init__(self, name, power, speed, hp):
        self.name = name
        self.power = power
        self.speed = speed
        self.hp = hp

        print(f"Pokemon: {self.name}\n"
              f"Power: {power}\n"
              f"Speed {speed}\n"
              f"Hp {hp}")

    def attack(self):
        print(f"{self.name} нановить {self.power} урону")

    def run(self):
        print(f"{self.name} біжить з швидкістю {self.speed}km/h")


class Fire(Pokemon):
    def fire(self):
        attack = self.power * 2
        print(f"{self.name} має урон {attack}")


class Water(Pokemon):
    def water(self):
        attack = self.power * 2
        hp = self.hp * 1.5
        speed = self.speed * 1.5
        print(f"{self.name} має урон {attack} та {hp}Hp а також бігає з швидкістю {speed}")


class Earth(Pokemon):
    def earth(self):
        hp = self.hp * 2
        print(f"{self.name} має {hp}Hp")


class Air(Pokemon):
    def air(self):
        speed = self.speed * 2
        print(f"{self.name} бігає з швидкістю {speed}")


charizard = Fire("Charizard", 20, 18, 75)
charizard.fire()


water_elementsl = Water("water elementsl", 15, 15, 50)
water_elementsl.water()

earth_elementsl=Earth("Earth elementsl", 18, 10, 100)
earth_elementsl.earth()

air_elementsl=Air("air elementsl", 10, 40, 50)
air_elementsl.air()
