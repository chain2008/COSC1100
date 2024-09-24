"""
In Class 1: Ice cream shop logistics
Author: Cheng He
Date: 2024-09-16
Version: 1
"""
SCOOP_CUP = 0.5
KID_SCOOP = 0.5
SMALL_SCOOP = 1
MEDIUM_SCOOP = 2
LARGE_SCOOP = 3
NUM_ERROR = "The number must be positive"

while True:
    try:
        #get kid cones from keyboard
        kiddie_cones = int(input("Enter kiddie cones sold in one week: "))
        #Responding to invalid data entry
        if kiddie_cones <= 0:
            raise ValueError(NUM_ERROR)
        break
    except ValueError as exp:
        print(f"Invalid input decimal number: {exp}")

try:
    small_cones = int(input("Enter small cones: "))
    medium_cones = int(input("Enter medium cones: "))
    large_cones = int(input("Enter large cones: "))
    scoops = kiddie_cones * KID_SCOOP + small_cones * SMALL_SCOOP + medium_cones * MEDIUM_SCOOP \
            + large_cones * LARGE_SCOOP
    cups = scoops * SCOOP_CUP
    print(f"The one week ice cream sold are ${cups:9.4f} cups")
except ValueError as exp:
    print(f"Invalid input decimal number: {exp}")
except TypeError:
    print("Invalid input decimal number")
except Exception as exp:
    print(f"Unknown error: {exp}")
