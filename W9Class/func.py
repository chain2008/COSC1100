# https://www.w3schools.com/python/python_functions.asp
# Python Built in Functions
# https://www.w3schools.com/python/python_ref_functions.asp

def funciton1():
    print("You have no child")

def function1(child3, child2, child1):
    #You can also send arguments with the key = value syntax.
    #This way the order of the arguments does not matter.
    print(f"Your children are {child1}, {child2}, {child3}")

function1(child2 = "Tobias", child1 = "Emil", child3 = "Linus")
funciton1()

def function1a(child3, child2, child1, /):
    #Positional-Only Arguments
    print(f"Your children are {child1}, {child2}, {child3}")

function1a(child2 = "Tobias", child1 = "Emil", child3 = "Linus")

def function1b(*, child3, child2, child1):
    #Keyword-Only Arguments
    print(f"Your children are {child1}, {child2}, {child3}")

function1b("Tobias", "Emil", "Linus")

# Arbitrary Arguments, *args
def function2(*kids):
    #parameters are accessed by their index
    print(f"You have {len(kids)} children")
    print("The youngest child is " + kids[2])

function2("Emil", "Tobias", "Linus")

def function3(**kid):
    """This way the function will receive a dictionary of arguments, 
    and can access the items accordingly"""
    print("His last name is " + kid["lname"])

last_name = "Refsnes"
function3(fname = "Tobias", lname = last_name)

def function4(food):
    """object as parameter"""
    for index in range(len(food)):
        food[index] += "new"

fruits = ["apple", "banana", "cherry"]
function4(fruits)
print(fruits)

def tri_recursion(k):
    #Recursion is a common mathematical and programming concept.
    if k > 0 :
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)

# https://www.w3schools.com/python/ref_func_slice.asp
# slice(start, end, step)
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

#https://www.w3schools.com/python/ref_func_map.asp
def myfunc(a, b):
    return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))