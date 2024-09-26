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
except ValueError as exp:
    print(exp)
except TypeError as exp:
    print(exp)
except Exception as exp:
    print(f"Unknown error: {exp}")
else:
    duckAmount = round(reservior_area*10000.0 / (duck_width*duck_depth))
    duckVolumn = duck_width*duck_depth*duck_height*duckAmount/1000000
    # calculate duck price here
    duckPrice = 1.71
    totalPrice = round(duckAmount * duckPrice,2)
    os.system('cls')
    print("********    AI Hub Rubber Duck Logistic Report    ********")
    #https://en.wikipedia.org/wiki/List_of_Unicode_characters
    print(f"Reservior Size is\t${reservior_area:.2f} m\u00b2")
    print(f"Duck Size:\t\t{duck_width}cmW x {duck_height}cmH x {duck_depth}cmD")
    print(f"Duck amount:\t\t{duckAmount}")
    print(f"Price for one duck:\t${duckPrice} CAD")
    print(f"Price for all ducks:\t${totalPrice} CAD")
    print(f"Shippment package:\t{duckVolumn:.2f} m\u00b3")
    print(f"**********    {date.today()} Reported by Cheg He    **********")
