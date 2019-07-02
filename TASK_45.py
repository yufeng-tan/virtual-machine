#  Extend your standard library to include options and basic list functions, like map, filter, and fold. 

def Add1(n):
    return n + 1

class Maybe:
    def __init__(self, val):
        self.val = val

    def __str__(sefl):
        return str(1) + '+ ' + sefl.val

class List:
    def __init__(self, li):
        self.li = list(li.split(' '))

    def __str__(self):
        return str(self.li)

# error
class Map:
    def __init__(self, func, li):
        self.func = func
        self.li = li

    def __str__(self):
        return str(map(Add1, self.li))


print(Maybe('A'))

print(List('1 2 3'))

print(Map(Add1, [1, 2, 3]))


