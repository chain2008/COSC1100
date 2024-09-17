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

#get kid cones from keyboard
kid_str = input("Enter kiddie cones sold in one week: ") #this is comment
kiddie_cones = int(kid_str)
small_cones = int(input("Enter small cones: "))
medium_cones = int(input("Enter medium cones: "))
large_cones = int(input("Enter large cones: "))
scoops = kiddie_cones * KID_SCOOP + small_cones * SMALL_SCOOP + medium_cones * MEDIUM_SCOOP \
         + large_cones * LARGE_SCOOP
cups = scoops * SCOOP_CUP
print(f"The one week ice cream sold are {cups} cups")
