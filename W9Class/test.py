def funciton1():
    print("You have no child")

def function1(child3, child2, child1):
    #You can also send arguments with the key = value syntax.
    #This way the order of the arguments does not matter.
    print(f"Your children are {child1}, {child2}, {child3}")

function1(child2 = "Tobias", child1 = "Emil", child3 = "Linus")
funciton1()
