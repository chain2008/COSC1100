"""
https://www.w3schools.com/python/python_lists.asp
Built-in: Lists are a built-in data structure in Python.
Flexible: They can store elements of different data types (e.g., integers, strings, objects).
Mutable: Lists can be modified after creation (e.g., adding, removing, or changing elements).
Syntax: Created using square brackets, e.g., my_list = [1, 2, 'three', 4.0]
"""
# an Empty List
""" os_list = list()
print(type(os_list))
os_list.append("Windows")
os_list.append("Linux")
os_list.append("Mac")
os_list.append("Unix")
print(os_list) """

os_list2 = ["apple", "banana", "cherry"]
print(f"type os_list2: {type(os_list2)}")
for item in os_list2:
    print(item, end=" ")
print("\n")
print(f"first item: {os_list2[0]}")
print(f"third item: {os_list2[2]}")
os_list2.append("orange")
for item in os_list2:
    print(item, end=" ")
