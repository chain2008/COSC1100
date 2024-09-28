"""
Week3 Class: Sales Commission
Author: Cheng He
Date: 2024-09-16
Version: 1
"""
import math

LOW_RATE = 0.04
MID_RATE = 0.065
HIGHT_RATE = 0.09
LOW_SALE = 10000
MEDIUM_SALE = 15000
NUM_ERROR = "The number must be positive"

#https://www.w3schools.com/python/python_try_except.asp
try:
    gross_sales = float(input("Enter input gross sales: "))
    #Responding to invalid data entry
    if gross_sales <= 0:
        raise ValueError(NUM_ERROR)
    else:

        if gross_sales < LOW_SALE:
            rate = LOW_RATE
        elif gross_sales < MEDIUM_SALE:
            rate = MID_RATE
        else:
            rate = HIGHT_RATE

    commission = gross_sales * rate
    print(f"The commission is ${commission:9.4f}")  # value:{width}.{precision}
except ValueError as exp:
    print(f"Invalid input decimal number: {exp}")    
except Exception as exp:
    print(f"Unknown error: {exp}")
