"""
In Class 5: Grade
Author: Cheng He
Date: 2024-09-20
Version: 3
"""
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import your parent module
import util

CLASS_WEIGHTING = 3
TEST_WEIGHTING = 6
grades = {
    "prca1":[0, CLASS_WEIGHTING, 0],
    "prca2":[0, CLASS_WEIGHTING, 0],
    "prca3":[0, CLASS_WEIGHTING, 0],
    "prca4":[0, CLASS_WEIGHTING, 0],
    "ca1":[0, CLASS_WEIGHTING, 0],
    "ca2":[0, CLASS_WEIGHTING, 0],
    "ca3":[0, CLASS_WEIGHTING, 0],
    "ca4":[0, CLASS_WEIGHTING, 0],
    "test theory":[0, TEST_WEIGHTING, 0],
    "test practice":[0, TEST_WEIGHTING, 0]
}

def validate(value):
    return value >= 0 and value <= 100

total_weight = 0
for grade in grades.items():
    grade[1][0] = util.get_input(f"Enter {grade[0]} grade: ", 'int', validate)
    grade[1][2] = grade[1][0] * grade[1][1]
    total_weight += grade[1][1]

def score(grade):
    return grade[2]
final_grade = sum(map(score, grades.values())) / total_weight
print(final_grade)
