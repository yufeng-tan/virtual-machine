# TASK 3
# Write a test-suite of a dozen J0 programs. 
# A test suite means examples with their expected output.


class Add:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + '+ ' + str(self.l) + ' ' + str(self.r) + ')'

class Sub:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + '- ' + str(self.l) + ' ' + str(self.r) + ')'

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

class Div:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + '/ ' + str(self.l) + ' ' + str(self.r) + ')'



# test suit

# (* 3 4)
print(Mult(Num(3), Num(4)))

# (+ 1 (* 3 4))
print(Add(1, Mult(Num(3), Num(4))))

# (* 5 (* 1 (+ 3 8)))
print(Mult(5, Mult(1, Add(3, 8))))

# (+ 8 (+ 0 (* 4 (* 3 2))))
print(Add(8, Add(0, Mult(4, Mult(3, 2)))))

# (- 8 (* 1 4))
print(Sub(8, Mult(1, 4)))

# (/ (* 4 5) (- 5 3))
print(Div(Mult(4, 5), Sub(5, 3)))

# (+ (/ (- 5 1) 3) 2)
print(Add(Div(Sub(5, 1), 3), 2))



''' result
(* 3 4)
(+ 1 (* 3 4))
(* 5 (* 1 (+ 3 8)))
(+ 8 (+ 0 (* 4 (* 3 2))))
(- 8 (* 1 4))
(/ (* 4 5) (- 5 3))
(+ (/ (- 5 1) 3) 2)
'''