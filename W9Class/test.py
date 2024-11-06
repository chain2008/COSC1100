#https://www.w3schools.com/python/ref_func_map.asp
def myfunc(a, b):
    return a +"_"+b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)

#convert the map into a list, for readability:
print(list(x))
