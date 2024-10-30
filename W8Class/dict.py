""" https://www.w3schools.com/python/python_dictionaries.asp
Dictionaries are used to store data values in key:value pairs. """

cosc1100_grade = {
    "Joe":80,
    "Mike":60,
    "Randy":70,
    "Mary":90
}
cosc1200_grade = {
    "Keven":70,
    "Mike":80,
    "Julie":90,
    "Mary":80
}
#to find out Julie's grade in cosc1200
#print(cosc1200_grade["Julie"])

for item in cosc1100_grade:
    #print(item, end=" ")
    print(item)
    #print(cosc1100_grade[item])
print(cosc1100_grade.items())
for item in cosc1100_grade.items():
    #print(item, end=" ")
    print(f"key: {item[0]} value: {item[1]}")
 
print(cosc1100_grade.keys())

cosc1100 = set(cosc1100_grade.keys())
cosc1200 = set(cosc1200_grade.keys())
both_course = cosc1100 & cosc1200
print(both_course)
print("Grades for students taking both courses")
for item in both_course:
    print(item, end=" ")
    print(f"{cosc1100_grade[item]}/COSC1100 {cosc1200_grade[item]}/COSC1200")
print("Grades for students taking only cosc1200")
only_1200 = cosc1200 - both_course
for item in only_1200:
    print(f"{item} {cosc1200_grade[item]}")
