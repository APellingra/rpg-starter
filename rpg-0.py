"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero:
    def __init__(self,health,power):
        self.health = health
        self.power = power

class Goblin:
    def __init__(self,health,power):
        self.health = health
        self.power = power

MyHero = Hero(10,5)
Gob = Goblin(6,2)
def main():
    MyHero.health = 10
    MyHero.power = 5
    Gob.health = 6
    Gob.power = 2

    while Gob.health > 0 and MyHero.health > 0:
        print("You have %d health and %d power." % (MyHero.health, MyHero.power))
        print("The goblin has %d health and %d power." % (Gob.health, Gob.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            Gob.health -= MyHero.power
            print("You do %d damage to the goblin." % MyHero.power)
            if Gob.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if Gob.health > 0:
            # Goblin attacks hero
            MyHero.health -= Gob.power
            print("The goblin does %d damage to you." % Gob.power)
            if MyHero.health <= 0:
                print("You are dead.")

main()
