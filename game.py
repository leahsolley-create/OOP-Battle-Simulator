from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Clump"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Griffin")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    goblin2 = Goblin("Gribble")

    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")

    hero = Hero("Rocky")
    print(f"{hero.name} has {hero.health} health and has entered the arena to fight the goblins")

    heroDamage = hero.attack()
    goblin.take_damage(heroDamage)
    goblinDamage = goblin.attack()
    hero.take_damage(goblinDamage)
    def battle_cry():
        if hero.health == 0:
            print("WAAAAAAA")

if __name__ == "__main__":
    main()

