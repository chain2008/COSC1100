
"""
https://www.w3schools.com/python/python_sets.asp
A set is a collection which is unordered, unchangeable*, and unindexed
"""

""" this_set = {"apple", "banana", "cherry", "orange"} #Sets are written with curly brackets
#this_set = set(("apple", "banana", "cherry")) # note the double round-brackets
print(f"length: {len(this_set)}") """

""" #Set items are unordered, unchangeable, and do not allow duplicate values.
for item in this_set:
    print(item, end=" ")
this_set.add("pizza")
print("\n")
for item in this_set:
    print(item, end=" ")
#at next run, the order will be changed """

#set implementation
#https://www.geeksforgeeks.org/introduction-to-set-data-structure/
#set operation
#https://www.geeksforgeeks.org/set-operations/

#We have two courses with the following students
cosc1100 = {"Joe","Mike","Randy","Mary","Stephen"}
cosc1200 = {"Keven","Mike","Julie","Mary"}
#Could you tell me those students who take both courses?
both_course = cosc1100.intersection(cosc1200) #cosc1100 & cosc1200
print(both_course)

#Could you tell me those students who only take cosc1100?
only_1100 = cosc1100 - both_course
print(only_1100)

#Could you tell me all the students?
all_students = cosc1100.union(cosc1200) #cosc1100 | cosc1200
print(all_students)