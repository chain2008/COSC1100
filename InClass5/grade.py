
CLASS_WEIGHTING = 3
TEST_WEIGHTING = 6

pre_classes = [0] * 4
in_classes = [0] * 4
first_tests = [0] * 2

for index in range(0, len(pre_classes)):
    while True:
        try:
            pre_classes[index] = int(input(f"input pre class {index}: "))
            break
        except Exception as exp:
            index = index

for index in range(0, len(in_classes)):
    while True:
        try:
            in_classes[index] = int(input(f"input in class {index}: "))
            break
        except Exception as exp:
            index = index

for index in range(0, len(first_tests)):
    while True:
        try:
            first_tests[index] = int(input(f"input first test {index}: "))
            break
        except Exception as exp:
            index = index

print(pre_classes)
print(in_classes)
print(first_tests)

pre_class_score = 0
for item in pre_classes:
    pre_class_score += item * CLASS_WEIGHTING

in_class_score = 0
for item in in_classes:
    in_class_score += item * CLASS_WEIGHTING

first_test_score = 0
for item in first_tests:
    first_test_score += item * TEST_WEIGHTING

total = CLASS_WEIGHTING * (len(pre_classes)+len(in_classes)) + TEST_WEIGHTING * len(first_tests)
grade = (pre_class_score+in_class_score+first_test_score)/total

print(grade)