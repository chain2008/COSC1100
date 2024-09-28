"""
In Class 3: Hot Dog Stand
Author: Cheng He
Date: 2024-10-04
Version: 1
"""
import os

traditional_dog = 0
veggie_dog = 0
curry_dog = 0
run = True

while run:
    os.system('cls')
    menu = "**** John's HotDog ****\n" + \
            "Enter your choice: \n" + \
            "1 - Sell Traditional Dog\n" + \
            "2 - Sell Veggie Dog\n" + \
            "3 - Sell Curry Hot Dog\n" + \
            "4 - Tally\n" + \
            "0 - Exit\n->"
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
            print(f"Traditional Dog\t{traditional_dog}")
            print(f"Veggie Dog\t{veggie_dog}")
            print(f"Curry Hot Dog\t{curry_dog}")
            print(f"Total\t\t{total}")                        
            run = False
        case "0":
            run = False
        case _:
            print("Wrong input")
