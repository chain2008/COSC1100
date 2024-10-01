"""
Week5 Class: Iteration
Author: Cheng He
Date: 2024-09-16
Version: 1
"""
import math

#https://www.w3schools.com/python/python_try_except.asp
try:
    for grp in range(1,10):
        for member in range(1,4):
            print(f"process student{member} at group{grp}\t", end="\t")
        print("\n")
except ValueError as exp:
    print(f"Invalid input decimal number: {exp}")
except Exception as exp:
    print(f"Unknown error: {exp}")
