"""
In Class 2: Rubber duck logistics
Author: Cheng He
Date: 2024-09-20
Version: 1
"""

NUM_ERROR = "The number must be positive"
IN_CM = 2.54

try:
    reservior_area = float(input("Enter reservior area in meter: "))
    #Responding to invalid data entry
    while reservior_area <= 0:
        reservior_area = float(input("Enter reservior area in meter: "))
    unit = input("Enter duck size unit(i for inch / c for centimetre): ")

    while unit != "i" and unit != "c":
        unit = input("Enter duck size unit(i for inch / c for centimetre): ")

    duck_width = float(input("Enter duck width: "))
    while duck_width <= 0:
        duck_width = float(input("Enter duck width: "))

    duck_depth = float(input("Enter duck depth: "))
    while duck_depth <= 0:
        duck_width = float(input("Enter duck depth: "))

    if unit == "i":
        duckAmount = reservior_area*10000 / (duck_width*duck_depth*IN_CM*IN_CM)
    else:
        duckAmount = reservior_area*10000 / (duck_width*duck_depth)

    print(f"We need {round(duckAmount)} ducks")
except ValueError as exp:
    print("Invalid input decimal number")  
except Exception as exp:
    print(f"Unknown error: {exp}")