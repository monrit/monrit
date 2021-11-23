import random
import time


class Warrior:
    health = 0


war1 = Warrior()
war2 = Warrior()
war1.health = 100
war2.health = 100
stavka_name = input("Tell me your name: ")
stavka_name2 = input("Tell me a name of a second guesser: ")
stavka = int(input(stavka_name + ", Make your bet!: "))
stavka2 = int(input(stavka_name2 + ", Make your bet!: "))
while war1.health != 0 or war2.health != 0:
    time.sleep(0.8)
    if random.randint(1, 2) == 1:
        war2health = 20
        if war2.health - war2health <= 0:
            print("DAMAGE IS:", war2health)
            war2.health = 0
            print("First warrior attacked second warrior!\nSecond warrior's health is equal to:", war2.health, "\n")
            print("\nFIRST WARRIOR WON!")
            zminna = 1
            break
        war2.health -= war2health
        print("First warrior attacked second warrior!\nSecond warrior's health is equal to:", war2.health, "\n")
    else:
        war1health = 20
        if war1.health - war1health <= 0:
            print("DAMAGE IS:", war1health)
            war1.health = 0
            print("Second warrior attacked first warrior!\nFirst warrior's health is equal to:", war1.health, "\n")
            print("\nSECOND WARRIOR WON!")
            zminna = 2
            break
        war1.health -= war1health
        print("Second warrior attacked first warrior!\nFirst warrior's health is equal to:", war1.health, "\n")
if zminna == stavka:
    print(stavka_name + ", Your bet won!")
elif zminna == stavka2:
    print(stavka_name2 + ", Your bet won!")
