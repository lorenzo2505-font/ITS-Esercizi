#elementi separati tra loro di una lista
mylist = ["a", "b", "c"]
print(*mylist)

#esempio args

def add(*args):
    total = 0
    for number in args:
        total=total + number
    return total
print(add(2,3))
print(add(10,  20, 30))

