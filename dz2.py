class SuperHero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def increase_health(self):
        self.health **= 2
        self.fly = True

    def display_true_phrase(self):
        print("True in the True_phrase")


class AirHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage


class EarthHero(SuperHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage


class Villain(AirHero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.people = "monster"

    def crit(self):
        self.damage **= 2


if __name__ == "__main__":
    air_hero = AirHero("AirMan", 100, 10)
    earth_hero = EarthHero("EarthMan", 120, 15)
    villain = Villain("EvilGuy", 150, 20)

    air_hero.increase_health()
    earth_hero.increase_health()
    villain.increase_health()

    air_hero.display_true_phrase()
    earth_hero.display_true_phrase()
    villain.display_true_phrase()

    villain.crit()
    print(villain.damage)
