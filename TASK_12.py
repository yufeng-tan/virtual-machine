# (HL) Define data structures to represent contexts. 
# C::= []|(if C e e)|(if e C e)|(if e e C)|(e... C e...)

class C:
    def __init__(self, list):
        self.list = list
