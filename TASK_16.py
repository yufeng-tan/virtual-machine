# (HL) Refine your definition of contexts to only allow evaluation contexts. 
# E::= []|(if E e e)|(v... E e...)


prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

class V:
    def __init__(self, v):
        if isinstance(v, (int, bool)) or str(v) in prim_list:
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
        if self.list[0] == 'HOLE':
            return 'HOLE'
        if self.list[0] == 'if' and (self.list[1] == 'true' or self.list[1] == 'false') and len(self.list) == 4:
            if self.list[1] == 'true':
                return 'E[' + self.list[2] + ']'
            if self.list[1] == 'false':
                return 'E[' + self.list[3] + ']'
        if isinstance(self.list[0], V):
            return str(self.list)




print(E(['HOLE']))

print(E(['if', 'true', 'et', 'ef']))

print(E(['if', 'false', 'et', 'ef']))

print(E([V('>'), '3', '1']))
