# (HL & LL) Define data structures to represent J3 programs and runtime values. 
# e::= x|v|(e e ...)|(if e e e)
# v::= number|boolean|prim|(lamda(x...)e)
# x::= variable-not-otherwise-mentioned
# prime::=+|*|/|-|<=|<|=|>|>=

prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

class x:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return str(self.x)

class V:
    def __init__(self, v):
        if isinstance(v, (int, bool,f)) or str(v) in prim_list:
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
