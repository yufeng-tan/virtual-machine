# (HL & LL) Define data structures to represent J2 programs and function definitions. 
# d::= (define(fx...)e)
# e::= x|v|(e e ...)|(if e e e)
# v::= number|boolean|prim|f
# x::= variable-not-otherwise-mentioned
# f::= variable-not-otherwise_mentioned
# prime::=+|*|/|-|<=|<|=|>|>=

prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

class f:
    def __init__(self, f):
        self.f = f
    def __str__(self):
        return str(self.f)

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

    def interp(self):
        if len(self.list) == 4 and self.list[0] == 'if':
            if self.list[1] == '<' and self.list[2] < self.list[3]:
                return self.list[2] + ' is less than ' + self.list[3]
            elif self.list[1] == '<' and self.list[2] > self.list[3]:
                return self.list[3] + ' is less than ' + self.list[2]

            elif self.list[1] == '<=' and self.list[2] <= self.list[3]:
                return self.list[2] + ' is less than or equal to ' + self.list[3]
            elif self.list[1] == '<=' and self.list[2] > self.list[3]:
                return self.list[3] + ' is less than ' + self.list[2]

            elif self.list[1] == '>' and self.list[2] > self.list[3]:
                return self.list[2] + ' is greater than ' + self.list[3]
            elif self.list[1] == '>' and self.list[2] < self.list[3]:
                return self.list[3] + ' is greater than ' + self.list[2]

            elif self.list[1] == '>=' and self.list[2] >= self.list[3]:
                return self.list[2] + ' is greater or equal to ' + self.list[3]
            elif self.list[1] == '>=' and self.list[2] < self.list[3]:
                return self.list[3] + ' is greater than ' + self.list[2]

            elif self.list[1] == '=' and self.list[2] == self.list[3]:
                return self.list[2] + ' is equal to ' + self.list[3]
            elif self.list[1] == '=' and self.list[2] != self.list[3]:
                return self.list[2] + ' is not equal to ' + self.list[3]

        if len(self.list) == 3 and self.list[0] in prim_list:
            if self.list[0] == '+':
                return int(self.list[1]) + int(self.list[2])
            if self.list[0] == '*':
                return int(self.list[1]) * int(self.list[2])
            if self.list[0] == '/':
                return int(self.list[1]) / int(self.list[2])
            if self.list[0] == '-':
                return int(self.list[1]) * int(self.list[2])

        if len(self.list) != 4 or len(self.list) != 3:
            return self.list

