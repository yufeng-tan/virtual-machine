# (HL) Write a dozen test J5 programs that use the standard library. 


prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=', 'pair', 'fst', 'snd', 'inl', 'inr']

class x:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return str(self.x)

class V:
    def __init__(self, v):
        if isinstance(v, (int, bool)) or str(v) in prim_list or isinstance(v, str) or isinstance(v, list):
            self.v = v
        else:
            self.v = 'error'

    def interp(self):
        return self.v

    def __str__(self):
        return str(self.interp())

class E:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return str(self.list)

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




test_1 = ['case', str(V('inl')), 'as', ['inl', 'e1'], ['inr', 'e2']]
test_2 = ['case', str(V('inl')), 'as', ['inl', 2], ['inr', 3]]
test_3 = ['pair', 1, 2]
test_4 = [str(V('fst')), [1, 2]]
test_5 = [str(V('snd')), [1, 2]]

print(E(test_2))
print(E(test_3))
print(E(test_4))
print(E(test_5))

print(Maybe('A'))
print(List('1 2 3'))





