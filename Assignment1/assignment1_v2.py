"""
Assignment1: Pizza
Author: Cheng He
Date: 2024-10-14
Version: 2
"""
import os
import math
NUM_ERROR = "The number must be positive"
ENTRY_ERROR = "Error input, number should be between 8 - 24"
diameter_config = {
    8:0,
    12:(6,),
    14:(6,8),
    16:(6,8,10),
    20:(6,8,10,12),
    24:(6,8,10,12,16)}

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

    slice_cuts = 0
    for diameter_setting in diameter_config.items():
        if diameter < diameter_setting[0]:
            slice_cuts = diameter_setting[1]
            break
#this is for the case of 24 needed to be included
    if diameter == diameter_setting[0]:
        slice_cuts = diameter_setting[1]

    if slice_cuts == 0:
        print(ENTRY_ERROR)
    else:
        print(f"Pizza Diameter: {diameter}\"")
        area =  math.pi * pow(diameter/2,2)
        for slice_cut in slice_cuts:
            print(f"Cut in {slice_cut} results in an area of {area/slice_cut:.2f}\" per slice")