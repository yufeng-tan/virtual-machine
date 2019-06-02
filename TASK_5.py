# TASK 5
# Define a data structure to represent Sexprs. 
# se::= empty|(cons se se)|string

# an empty class for sexpr
class sexpr:
    pass

# subclass for string
class sexpr_string(sexpr):
    def __init__(self, s):
        if isisinstance(s, str):
            self.s = s

    def __str__(self):
        return str(self.s)

# subclass for pair of sexpr
class sexpr_pair(sexpr):
    def __init__(self, s):
        if isinstance(s, tuple):
            self.s = s

# subclass for empty
class sexpr_empty(sexpr):
    def __init__(self, s):
        if not string.strip():
            self.s = s

