""" https://www.w3schools.com/python/python_dictionaries.asp
Dictionaries are used to store data values in key:value pairs. """

cosc1100_grade = {"Joe":80,"Mike":60,"Randy":70,"Mary":90}
cosc1200_grade = {"Keven":70,"Mike":80,"Julie":90,"Mary":80}
for item in cosc1100_grade:
    print(item, end=" ")
    print(cosc1100_grade[item])

cosc1100 = set(cosc1100_grade.keys())
cosc1200 = set(cosc1200_grade.keys())
both_course = cosc1100 & cosc1200
print(both_course)
for item in both_course:
    print(item, end=" ")
    print(f"{cosc1100_grade[item]}/COSC1100 {cosc1200_grade[item]}/COSC1200")

only_1200 = cosc1200 - both_course
print(only_1200)
only_1100 = cosc1100 - both_course
print(only_1100)
all_students = cosc1100 | cosc1200
print(all_students)