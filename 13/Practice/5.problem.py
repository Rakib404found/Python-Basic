from functools import reduce

l = [11, 2, 65, 70, 40, 95, 99,69, 222]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater, l))