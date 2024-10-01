"""
In Class 2: Rubber duck logistics
Author: Cheng He
Date: 2024-09-20
Version: 1
"""
import os
from datetime import date

NUM_ERROR = "The number must be positive"
UNIT_ERROR = "Wrong unit, either i or c"
IN_CM = 2.54
QTY1 = 150
PRICE1 = 2.95
QTY2 = 250
PRICE2 = 2.67
QTY3 = 500
PRICE3 = 2.37
QTY4 = 1000
PRICE4 = 2.07
QTY5 = 2500
PRICE5 = 1.88
QTY6 = 5000
PRICE6 = 1.71
PRICE7 = 1.51

try: #input validation
    reservior_area = float(input("Enter reservior area in square meter: "))
    #Responding to invalid data entry
    if reservior_area <= 0:
        raise ValueError(NUM_ERROR)

    duck_width = float(input("Enter duck width: "))
    if duck_width <= 0:
        raise ValueError(NUM_ERROR)

    duck_depth = float(input("Enter duck depth: "))
    if duck_depth <= 0:
        raise ValueError(NUM_ERROR)

    duck_height = float(input("Enter duck height: "))
    if duck_height <= 0:
        raise ValueError(NUM_ERROR)

    unit = input("Enter duck size unit(i for inch / c for centimetre): ")
    match unit:
        case "i":
            duck_width *= IN_CM
            duck_depth *= IN_CM
            duck_height *= IN_CM
        case "c":
            pass
        case _:
            raise TypeError(UNIT_ERROR)
    duck_amount = round(reservior_area*10000.0 / (duck_width*duck_depth))
    duck_volumn = duck_width*duck_depth*duck_height*duck_amount/1000000
    # calculate duck price here
    if duck_amount <= QTY1:
        unit_price = PRICE1
    elif duck_amount <= QTY2:
        unit_price = PRICE2
    elif duck_amount <= QTY3:
        unit_price = PRICE3
    elif duck_amount <= QTY4:
        unit_price = PRICE4
    elif duck_amount <= QTY5:
        unit_price = PRICE5
    elif duck_amount <= QTY6:
        unit_price = PRICE6
    else:
        unit_price = PRICE7
    total_price = round(duck_amount * unit_price,2)
    #generate output
    prt = input("Do you want to print to file? Yes/No:")
    if prt.find("Y")>=0 or prt.find("y")>=0 :
        with open("output.txt", "a") as f:
            print("********    AI Hub Rubber Duck Logistic Report    ********", file=f)
            #https://en.wikipedia.org/wiki/List_of_Unicode_characters        
            print(f"Reservior Size:\t\t${reservior_area:.2f} m\u00b2", file=f)
            print(f"Duck Size:\t\t\t{duck_width}cmW x {duck_height}cmH x {duck_depth}cmD", file=f)
            print(f"Duck amount:\t\t{duck_amount}", file=f)
            print(f"Price for one duck:\t${unit_price} CAD", file=f)
            print(f"Price for all ducks:${total_price} CAD", file=f)
            print(f"Shippment package:\t{duck_volumn:.2f} m\u00b3", file=f)
            print(f"**********    {date.today()} Reported by Cheng He    **********\n\n\n\n",\
                 file=f)
    else:
        os.system('cls')
        print("\n\n\n\n********    AI Hub Rubber Duck Logistic Report    ********")
        print(f"Reservior Size is\t${reservior_area:.2f} m\u00b2")
        print(f"Duck Size:\t\t{duck_width}cm x {duck_depth}cm")
        print(f"Duck amount:\t\t{duck_amount}")
        print(f"Price for one duck:\t${unit_price:.2f} CAD")
        print(f"Price for all ducks:\t${total_price:.2f} CAD")
        print(f"Shippment package:\t{duck_volumn:.2f} m\u00b3")
        print(f"**********    {date.today()} Reported by Cheg He    **********\n\n\n\n")
except ValueError as exp:
    print(exp)
except TypeError as exp:
    print(exp)
except Exception as exp:
    print(f"Unknown error: {exp}")
