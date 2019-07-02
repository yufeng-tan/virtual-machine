# Extend your J4 data structures to J5.

# e::= x | v | (e e ...) | (if e e e)
#   | (case e as [(inl x) => e][(inr x) => e])
#   | (obj [x:e] ... ) | (ref e x)
# v::= number | boolean |prim | lambda x (x ...) e
#   | unit | (pair v v) | (inl v) | (inr v)
#   | (obj[x:v] ...)
# x::= variable-not-otherwise-mentioned
# prim::= + | * | / | - | <= | < | = | > | >=
#   | pair | fst | snd | inl | inr

prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=', 'pair', 'fst', 'snd', 'inl', 'inr']

class x:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return str(self.x)

class V:
    def __init__(self, v):
        if isinstance(v, (int, bool,f)) or str(v) in prim_list or isinstance(v, str) or isinstance(v, list):
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
