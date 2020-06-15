from random import choice
import sys
print("WELCOME TO OUR GAME")
input("Enter your name: ")
age = int(input("Enter your age: "))
if age > 18:
    print("You are eligible to play this game")
    op = input("do you want to continue(Y/N) ")
    if op.lower() == "y":
        print("ok so lets begin")
        health=10
        drag_health = 10
        drag_act = ["attack", "defend", "fly"]
        print(f"your health: {health}")
        print("So you begin your journey towards the rescue of love of your life from a fearsome dragon.")
        w1= input("which path would you take (left/right) ")
        if w1.lower()=="left":
            print("great! you are on your way.")
        else:
            print("You take a path under terrors of robbers and assasins.\nyou loose 5hp in the attempt to get through")
            health -= 5
            print(f"your health: {health}")

        print("Now you come across a vast lake")
        w2 = input("How would you like to cross it (swim through/go around) ")
        if w2.lower() == "swim through":
            print("You got bit by a poisonous fish and lost 5hp")
            health -= 5
            if health == 0:
                print("YOU LOST\n GAME OVER!")
                sys.exit(0)
            else:
                print(f"your health: {health}")
        else:
            print("You safely cross the lake tired out and exhausted.")
        print("you see a house nearby.")
        w3 = input("would you like to rest (yes/no): ")
        if w3.lower() == "yes":
            print("the owner was the member of society of assasins and kills you at your sleep.\n YOU LOST!")
        else:
            print("you continue your journey at darkness of night to reach a mighty mountain.\n You see a dark labyrinth leading into.")
            w4 = input("What would you do (go ahead/climb through)")
            if w4.lower() == "climb through":
                print("Little did you notice, the fearsome dragon swoops through the dark night sky and kills you!\n YOU LOST")
            else:
                print("Your path is dark and never-ending.\non your way you are bit by some deadly insects and lost 5hp.")
                health -= 5
                if health == 0:
                    print("YOU LOST")
                else:
                    print(f"your health: {health}")
                    print("through the darkness you finally reach the adobe of the dragon.\nthe gaint beast swoops down from the sky.")
                    print("You draw your bow and arrow and get yourself steady!")
                    while (True):
                        a = input("What would you choose do(attack/defend) ")
                        b = choice(drag_act)
                        print(f"dragon chooses to {b}")
                        if a.lower() == "attack" and b == "fly":
                            drag_health -= 5
                        elif a.lower() == "attack" and b == "attack":
                            health -= 5
                        else:
                            pass
                        print(f"dragon health: {drag_health}\nyour health: {health}")

                        if health == 0:
                            print("YOU LOST")
                            break
                        elif drag_health == 0:
                            print("CONGRATULATIONS!!YOU WIN")
                            print("You went up the stairs to greet your beautiful princess awaiting for you to rescue her.\nTHE END")
                            break

    else:
        print("okay see ya!")
print("GAME QUIT SUCCESSFULLY")