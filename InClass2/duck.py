"""
In Class 2: Rubber duck logistics
Author: Cheng He
Date: 2024-09-20
Version: 1
"""

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

    unit = input("Enter duck size unit(i for inch / c for centimetre): ")
    match unit:
        case "i":
            duck_width *= IN_CM
            duck_depth *= IN_CM
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
    print(f"We need {duckAmount} ducks")
