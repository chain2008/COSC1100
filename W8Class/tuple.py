""" 
https://www.w3schools.com/python/python_tuples.asp
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable 
"""

this_tuple = ("apple", "banana", "cherry", "orange", "cherry") #Tuples are written with round brackets
#this_tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
""" print(f"length: {len(this_tuple)}")
print(f"first item: {this_tuple[0]}")
this_tuple[3] = "orange"
print(f"forth item: {this_tuple[3]}") """

#this_tuple[1] = "orange"
#for item in this_tuple:
#    print(item, end=",") 

""" this_tuple = ("apple",)
print(type(this_tuple))

#NOT a tuple
this_tuple = ("apple")
print(type(this_tuple)) """

this_tuple = ("abc", 34, True, 40, "male")
for item in this_tuple:
    print(item, end=" ")
this_const = ("abc", 34, True, 40, "male")
print(this_const[0])
