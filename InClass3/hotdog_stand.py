"""
In Class 3: Hot Dog Stand
Author: Cheng He
Date: 2024-10-04
Version: 1
"""
import os
#https://www.w3schools.com/python/python_tuples.asp
DOGS = ("Traditional","Veggie","Curry Hot")
menu = "**** John's HotDog ****\n" + \
        "Enter your choice: \n"
traditional_dog = 0
veggie_dog = 0
curry_dog = 0
run = True

item_number = 1
for item in DOGS:
    menu += f"{item_number} - {item} Dog\n"
    item_number += 1
menu += f"{item_number} - Tally\n"
menu += "0 - Exit\n->"

while run:
    os.system('cls')

    choice = input(menu)
    match choice:
        case "1":
            traditional_dog += int(input("Enter Traditional Dog Number: "))
        case "2":
            veggie_dog += int(input("Enter Veggie Dog Number: "))
        case "3":
            curry_dog += int(input("Enter Curry Hot Dog Number: "))
        case "4":
            total = traditional_dog + veggie_dog + curry_dog
            os.system('cls')
            print("**** John's HotDog ****")
            print(f"Traditional Dog\t{traditional_dog}\t{traditional_dog/total:.1%}")
            print(f"Veggie Dog\t{veggie_dog}\t{veggie_dog/total:.1%}")
            print(f"Curry Hot Dog\t{curry_dog}\t{curry_dog/total:.1%}")
            print(f"Total\t\t{total}\tPercentage")
            run = False
        case "0":
            run = False
        case _:
            print("Wrong input")
