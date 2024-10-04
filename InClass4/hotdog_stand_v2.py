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
#https://en.wikipedia.org/wiki/List_of_hot_dogs#:~:text=A%20hot%20dog%20is%20a%20type%20of%20cooked%20sausage,%20traditionally
DOGS = ("Traditional","Veggie","Curry Hot", "Spicy", "Bagel","Corn" )
dog_sales = [0,0,0,0,0,0]
run = True

item_number = 1
for item in DOGS:
    menu += f"{item_number} - {item} Dog\n"
    item_number += 1
menu += f"{item_number} - Tally\n"
menu += "0 - Exit\n->"

while run:
    os.system('cls')
    choice = int(input(menu))
    dog_choice_count = len(DOGS)
    if choice == 0:
        run = False
    elif choice == dog_choice_count+1:
        total = 0
        for sale in dog_sales:
            total += sale
        os.system('cls')
        print("**** John's HotDog ****")
        for item in DOGS:
            dog_sale = dog_sales[DOGS.index(item)]
            print(f"{item} Dog\t{dog_sale}\t{dog_sale/total:.1%}")
        print(f"Total\t\t{total}\tPercentage")
        run = False
    else:
        good_item = False
        for item_choice in range(dog_choice_count):
            if choice-1 == item_choice:
                dog_sales[item_choice] += int(input(f"Enter {DOGS[item_choice]} Dog Sales: "))
                good_item = True
                break
        if not good_item:
            print("Wrong input")
