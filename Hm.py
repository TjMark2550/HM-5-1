import random

character1 = input("What is the name of the 1st character?: ")
hp1 = int(input("Please input his default HP:"))
character2 = input("What is the name of the 2nd character?: ")
hp2 = int(input("Please input his default HP:"))

while hp1 > 0 and hp2 > 0:
    damage1 = random.randint(1,200)
    damage2 = random.randint(1,200)
    defense1 = random.randint(1,100)
    defense2 = random.randint(1,100)
    attack = damage1 - defense2
    hp2 = hp2 - attack

        

    print(f"{character1} has {damage1} attack.")
    print(f"{character2} has {defense2} defense.")
    print(f"{character1} is attacking {character2}...")
    if defense2 >= damage1:
        print(f"{character1} attacked {character2} with no damage!!!")
    else:
        print(f"Finally....{character1} attacks {character2} with {attack}")
    if hp1 <= 0:
        hp1 = 0
    elif hp2 <= 0:
        hp2 = 0
    print(f"{character1} has HP = {hp1}")
    print(f"{character2} has HP = {hp2}\n")

    attack = damage2 - defense1
    hp1 = hp1 - attack

        

    print(f"{character2} has {damage2} attack.")
    print(f"{character1} has {defense1} defense.")
    print(f"{character2} is attacking {character1}...")
    if defense1 >= damage2:
        print(f"{character2} attacked {character1} with no damage!!!")
    else:
        print(f"Finally....{character2} attacks {character1} with {attack}")
    if hp1 <= 0:
        hp1 = 0
    elif hp2 <= 0:
        hp2 = 0
    print(f"{character1} has HP = {hp1}")
    print(f"{character2} has HP = {hp2}\n")
print(f"Complete this game!!!")
if hp2 == 0:
    print(f"{character1} win!!!")
elif hp1 == 0:
    print(f"{character2} win!!!")
    

    