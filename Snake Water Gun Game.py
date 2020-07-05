import random
from time import sleep

"""
Please Note That
 
print("*****")
print("~~~~~")
print("-----")

These Were Used Only For Basic Design To Make Program Beautiful
"""

print("___________Welcome To Coding World___________")
print("\t~~~~~~~~~Version - 1.0~~~~~~~~~~~")
print("\n  \t \t \t Snake Water Gun ")

no_of_chances = 0
chance = 10
computer_points = 0
your_points = 0

while no_of_chances < chance:

    modle = ["Snake", "Water", "Gun"]
    a = random.choice(modle)
    print("")
    print("******************************************")
    user_choice = input("Enter Your One Choice - Snake - Water - Gun- :-").capitalize()
    print()

    if user_choice == a:
        print("Tie!!  0 Poinst")

    elif user_choice == "Gun" and a == "Snake":
        your_points = your_points + 1
        print(f"Computer Choice- {a} \nYour Choice- {user_choice} \nYou Get 1 Point\n")

    elif user_choice == "Water" and a == "Gun":
        your_points = your_points + 1
        print(f"Computer Choice- {a} \nYour Choice- {user_choice} \nYou Get 1 Point\n")

    elif user_choice == "Snake" and a == "Water":
        print(f"Computer Choice- {a}\nYour Choice- {user_choice}\nYou Get 1 Point\n")
        your_points = your_points + 1

    elif user_choice == "Snake" and a == "Gun":
        computer_points = computer_points + 1
        print(f"Computer Choice- {a} \nYour Choice- {user_choice} \nComputer Get 1 Point\n")

    elif user_choice == "Water" and a == "Snake":
        computer_points = computer_points + 1
        print(f"Computer Choice- {a} \nYour Choice- {user_choice} \nComputer Get 1 Point\n")

    elif user_choice == "Gun" and "Water":
        computer_points = computer_points + 1
        print(f"Computer Choice- {a} \nYour Choice- {user_choice} \nComputer Get 1 Point\n")

    else:
        print("Your Input Wrong")

    no_of_chances = no_of_chances+1
    print(f"Your Score - {your_points} And Computer Points - {computer_points}")
    print(f"{chance - no_of_chances} Left out of {chance}")

if computer_points > your_points:
    print("\n---------Computer Wins------------")
elif computer_points < your_points:
    print("-----------You Wins-----------------")


sleep(3)
