"""
Week5 Class: Iteration
Author: Cheng He
Date: 2024-09-16
Version: 1
"""

#https://www.w3schools.com/python/python_try_except.asp
try:
    for grp in range(1,10):
        for member in range(1,4):
            print(f"pro studt{member} at grp{grp}\t", end="\t")
            print("\nwithin member loop")
        print("within group loop")
        print("\n*************")
except ValueError as exp:
    print(f"Invalid input decimal number: {exp}")
except Exception as exp:
    print(f"Unknown error: {exp}")
