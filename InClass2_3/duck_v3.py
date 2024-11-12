"""
In Class 2: Rubber duck logistics
Author: Cheng He
Date: 2024-09-20
Version: 3
"""
import os
import sys
from datetime import date

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import util
import constant
import duck_price

NUM_ERROR = "The number must be positive"
UNIT_ERROR = "Wrong unit, either i or c"

def validate(value):
    return value > 0
def unit_validate(value):
    return value == "i" or value == "c"

reservior_area = util.get_input("Enter reservior area in square meter: ","float", validate)
duck_width = util.get_input("Enter duck width: ","float", validate)
duck_depth = util.get_input("Enter duck depth: ","float", validate)
duck_height = util.get_input("Enter duck height: ","float", validate)

unit = util.get_input(messge="Enter duck size unit(i for inch / c for centimetre): ",validate=unit_validate)
match unit:
    case "i":
        duck_width *= constant.IN_CM
        duck_depth *= constant.IN_CM
        duck_height *= constant.IN_CM
    case _:
        pass
duck_amount = round(reservior_area*10000.0 / (duck_width*duck_depth))
unit_price = duck_price.get_price(duck_amount)
duck_volumn = duck_width*duck_depth*duck_height*duck_amount/1000000

total_price = round(duck_amount * unit_price,2)
#generate output
prt = input("Do you want to print to file? Yes/No:")
if prt.find("Y")>=0 or prt.find("y")>=0 :
    sys.stdout = open('output.txt', 'w')
os.system('cls')
print("\n\n\n\n********    AI Hub Rubber Duck Logistic Report    ********")
print(f"Reservior Size is    ${reservior_area:.2f} m\u00b2")
print(f"Duck Size:           {duck_width}cm x {duck_depth}cm")
print(f"Duck amount:         {duck_amount}")
print(f"Price for one duck:  ${unit_price:.2f} CAD")
print(f"Price for all ducks: ${total_price:.2f} CAD")
print(f"Shippment package:   {duck_volumn:.2f} m\u00b3")
print(f"**********    {date.today()} Reported by Cheg He    **********\n\n\n\n")
