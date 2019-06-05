# TASK 9
# (HL) Write a test-suite of a dozen J1 programs.  
# These should be written as Sexprs.


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
        str_if = self.n.split(',')[0]
        str_ec = self.n.split(',')[1]
        str_et = self.n.split(',')[2]
        str_ef = self.n.split(',')[3]
        return str('(' + str_if + ',' + str_ec + ',' + str_et + ',' + str_ef + ')')

class E_ne:
    def __init__(self, n):
        if len(str(n)) > 1:
            self.n = n
        else:
            self.n = 'error'

    def __str__(self):
        ne = self.n.split(',')
        return str(ne)



# e::= v|(e e...)|(if e e e)
# v::= number|boolean|prim
# prim ::= + | * | / | - | <= | < | = | > | >=

print(E_v('5'))

print(E_v('+'))

print(E_v('>='))

# (if e e e)
print(E_if('if, A is bigger than B, return A, return B'))

print(E_if('if, > A B, A, B'))


print(E_ne('abc,123,def,456, ghi'))


