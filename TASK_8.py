# TASK 8
# (HL) Define data structures to represent J1 programs, with pretty printers. 
# e::= v|(e e...)|(if e e e)
# v::= number|boolean|prim
# prim ::= + | * | / | - | <= | < | = | > | >=

prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

class E_v:
    def __init__(self, n):
        if str(n).isnumeric() or isinstance(n, bool) or str(n) in prim_list:
            self.n = n
        else:   self.n = 'error'

    def __str__(self):
        return str(self.n)

class E_if:
    def __init__(self, n):
        if str(n)[0:2] == 'if':
            self.n = n
        else:   self.n = 'error'

    def __str__(self):
        return str(self.n)

class E_ne:
    def __init__(self, n):
        if len(str(n)) > 1:
            self.n = n
        else:
            self.n = 'error'
    def __str__(self):
        return str(self.n)



print(E_v('+'))

print(E_if('if e e e'))

print(E_ne('e e e e e e e e e e e'))

print(E_ne('e'))