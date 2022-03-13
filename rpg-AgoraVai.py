from random import randint


class Char:
    def __init__(self, name, classe, attack, defence):
        self.name = name
        self.health = 10
        self.max_health = 10
        self.classe = classe
        self.force = attack
        self.defence = defence
        self.level = 3
        self.kills = 0

    def get_status(self):
        print(f" Health: {self.health}/{self.max_health}")

    def attack(self, enemy):
        damage = min(
            max(randint(0, self.level) - randint(0, enemy.defence), 0), enemy.health
            )
        if damage > 0:
            enemy.health -= damage
            print(f"{enemy.name} took {damage} damage!")
            print(f"{enemy.name} HP: {enemy.health}")
        else:
            print(f"{enemy.name} evaded the attack!")
        return enemy.health <= 0

    def defend(self):
        print("You defended i guess ? ")

    def flee(self):
        print("FLEEEEEEEE TO THE MOUTAINS")


class Enemy:
    def __init__(self, name, attack, defence, level, hero):
        self.name = name
        self.level = level
        self.health = randint(self.level, hero.health)
        self.force = attack
        self.defence = defence


def combat(hero, enemy):
    while enemy.health > 0:
        action = input("What do you want to do ? \n")
        callback_map = {
            "attack": hero.attack,
            "defend": hero.defend,
            "flee": hero.flee,
            "status": hero.get_status
        }
        callback = callback_map.get(action)
        if callback:
            if action == "attack":
                callback(enemy)
            else:
                callback()
    print(f"{hero.name} Won")


p = Char('Dee', "Warrior", 3, 2)
enem = Enemy('goblin', 3, 1, 1, p)

combat(p, enem)
