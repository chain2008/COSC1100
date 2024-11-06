"""
In Class 1: Ice cream shop logistics
Author: Cheng He
Date: 2024-11-16
Version: 2
"""
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import your parent module
import util

SCOOP_CUP = 0.5
cones = {"Kiddie":[0.5*SCOOP_CUP,0],"Small":[SCOOP_CUP,0],"Medium":[2*SCOOP_CUP,0],"Large":[3*SCOOP_CUP,0]}

def validate(value):
    return value > 0

for item in cones.items():
    item[1][1] = util.get_input(f"Enter {item[0]} cones sold in one week: ", 'int', validate)
cups = 0
for value in cones.values():
    cups += value[0]*value[1]
print(cups)
