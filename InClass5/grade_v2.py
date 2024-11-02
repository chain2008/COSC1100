"""
In Class 5: Grade
Author: Cheng He
Date: 2024-09-20
Version: 2
"""
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import your parent module
import util

CLASS_WEIGHTING = 3
TEST_WEIGHTING = 6

pre_classes = [0] * 4
in_classes = [0] * 4
first_tests = [0] * 2

for index in range(0, len(pre_classes)):
    pre_classes[index] = util.get_input(f"input pre class {index}: ", "int")

for index in range(0, len(in_classes)):
    in_classes[index] = util.get_input(f"input int class {index}: ", "int")

for index in range(0, len(first_tests)):
    first_tests[index] = util.get_input(f"input middle term test {index}: ", "int")

print(pre_classes)
print(in_classes)
print(first_tests)

pre_class_score = sum(pre_classes) * CLASS_WEIGHTING
in_class_score = sum(in_classes) * CLASS_WEIGHTING
first_test_score = sum(first_tests) * TEST_WEIGHTING

total = CLASS_WEIGHTING * (len(pre_classes)+len(in_classes)) + TEST_WEIGHTING * len(first_tests)
grade = (pre_class_score+in_class_score+first_test_score)/total

print(grade)