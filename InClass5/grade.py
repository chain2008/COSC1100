
CLASS_WEIGHTING = 3
TEST_WEIGHTING = 6
TOTAL = 36
pre_classes = [70,100,90,90]
in_classes = [100,100,100,100]
fist_tests = [92,88]
bonus = 100

""" pre_classes = [90,70,80,80]
in_classes = [100,100,100,100]
fist_tests = [76,99]
bonus = 0 """

for index in range(0, len(pre_classes)):
    while True:
        try:
            score = int(input(f"pre class {index}: "))
            pre_classes[index] = score
            break
        except Exception as exp:
            index = index
print(pre_classes)
pre_class_score = 0
for item in pre_classes:
    pre_class_score += item * CLASS_WEIGHTING

in_class_score = 0
for item in in_classes:
    in_class_score += item * CLASS_WEIGHTING

first_test_score = 0
for item in fist_tests:
    first_test_score += item * TEST_WEIGHTING

if bonus != 0:
    grade = (pre_class_score+in_class_score+first_test_score+100*10+100*2)/(TOTAL+12)
else:
    grade = (pre_class_score+in_class_score+first_test_score)/TOTAL    

print(grade)