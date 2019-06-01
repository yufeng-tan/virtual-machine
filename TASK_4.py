# TASK 4
# Implement a big-step interpreter for J0. 
# Connect to your test suite.


class Num:
    def __init__(self, n):
        self.n = n

    def interp(self):
        return self.n

    def __str__(self):
        return str(self.interp())

class Add:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    
    def interp(self):
        n1 = Num(self.l).interp()
        n2 = Num(self.r).interp()
        return Num(n1.n + n2.n)

    def __str__(self):
        return '(' + '+ ' + str(self.l) + ' ' + str(self.r) + ')'

class Sub:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def interp(self):
        n1 = Num(self.l).interp()
        n2 = Num(self.r).interp()
        return Num(n1.n - n2.n)

    def __str__(self):
        return '(' + '- ' + str(self.l) + ' ' + str(self.r) + ')'

class Mult:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def interp(self):
        n1 = Num(self.l).interp()
        n2 = Num(self.r).interp()
        return Num(n1.n * n2.n)

    def __str__(self):
        return '(' + '* ' + str(self.l) + ' ' + str(self.r) + ')'

class Div:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def interp(self):
        n1 = Num(self.l).interp()
        n2 = Num(self.r).interp()
        return Num(n1.n / n2.n)

    def __str__(self):
        return '(' + '/ ' + str(self.l) + ' ' + str(self.r) + ')'



# test suit

# (+ 3 4)
print(Add(Num(3), Num(4)))
print(Add(Num(3), Num(4)).interp())


# (* 3 4)
print(Mult(Num(3), Num(4)))
print(Mult(Num(3), Num(4)).interp())


# (- 3 4)
print(Sub(Num(3), Num(4)))
print(Sub(Num(3), Num(4)).interp())

# (/ 3 4)
print(Div(Num(3), Num(4)))
print(Div(Num(3), Num(4)).interp())

''' result
(+ 3 4)
7
(* 3 4)
12
(- 3 4)
-1
(/ 3 4)
0.75
'''