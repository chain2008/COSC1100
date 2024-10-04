"""
In Class 3: Hot Dog Stand
Author: Cheng He
Date: 2024-10-04
Version: 1
"""
import os
#https://www.w3schools.com/python/python_tuples.asp

menu = "**** John's HotDog ****\n" + \
        "Enter your choice: \n"
TRADITIONAL = 0
VEGGIE = 1
CURRY_HOT = 2
DOG_TYPE_COUNT = 3

DOGS = ("Traditional","Veggie","Curry Hot")
dog_sales = [0,0,0]
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
            #add traditional dog
            pass
        case "2":
            #add veggie dog
            pass
        case "3":
            dog_sales[CURRY_HOT] += int(input("Enter Curry Hot Dog Sales: "))
        case "4":
            total = 0
            for sale in dog_sales:
                total += sale
            os.system('cls')
            #print out tally

            run = False
        case "0":
            run = False
        case _:
            print("Wrong input")
