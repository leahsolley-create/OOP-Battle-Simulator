import random

class Hero:
    """A playable character who battles emimies in the arena."""

    def __init__(self, name):
        self.name = name
        self.health = 125
        self.attack_power = 15

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
