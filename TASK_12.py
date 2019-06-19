# (HL) Define data structures to represent contexts. 
# C::= []|(if C e e)|(if e C e)|(if e e C)|(e... C e...)

class C:
    def __init__(self, list):
        if list[0] == 'HOLE' or list[1] == 'HOLE' or list[2] == 'HOLE':
            self.list = list
        else:
            self.list = ['error']

    def interp(self):
        return self.list

    def __str__(self):
        return str(self.interp())



print(C(['e', 'e', 'e']))


print(C(['e', 'HOLE', 'e']))
