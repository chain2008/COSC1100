"""
Assignment1: Pizza
Author: Cheng He
Date: 2024-10-14
Version: 1
"""
import os
import math
NUM_ERROR = "The number must be positive"
ENTRY_ERROR = "ENTRY ERROR"
diameter_config = (8,12,14,16,20,24)
slice_config = (0,(6,),(6,8),(6,8,10),(6,8,10,12),(6,8,10,12,16),0)

while True:
    valid_input = False
    while not valid_input:
        try:
            diameter = float(input("Please enter the diameter of your pizza (0 to end program): "))
            if diameter == 0 :
                exit(0)
            elif diameter < 0:
                print(NUM_ERROR)
            else:
                valid_input = True
        except ValueError as exp:
            print(f"Invalid input decimal number: {exp}")
        except Exception as exp:
            print(f"Unknown error: {exp}")

    item_index = 0
    for diameter_setting in diameter_config:
        if diameter < diameter_setting:
            break
        item_index += 1
    slice_cuts = slice_config[item_index]

    if slice_cuts == 0:
        print(ENTRY_ERROR)
    else:
        print(f"Pizza Diameter: {diameter}\"")
        area =  math.pi * pow(diameter/2,2)
        for slice in slice_cuts:
            print(f"Cut in {slice} results in an area of {area/slice:.2f}\" per slice")