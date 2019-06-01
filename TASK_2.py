# TASK 2
# Write a pretty-printer for J0 programs.

class Add:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + '+ ' + str(self.l) + ' ' + str(self.r) + ')'

class Num:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

class Mult:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + '* ' + str(self.l) + ' ' + str(self.r) + ')'




print(Mult(Num(3), Num(4)))
print(Add(1, Mult(Num(3), Num(4))))

# result 
# (* 3 4)
# (+ 1 (* 3 4))
