# TASK 11
# (HL) Extend your interpreter for J1.


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


class E_if2:
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


print(E(['if', '<', '3', '4']).interp())
print(E(['if', '<', '6', '2']).interp())
print(E(['if', '<=', '3', '4']).interp())
print(E(['if', '>=', '7', '7']).interp())
print(E(['if', '=', '7', '7']).interp())
print(E(['if', '=', '7', '9']).interp())
print(E(['+', '7', '9']).interp())
print(E(['-', '7', '9']).interp())
print(E(['*', '7', '9']).interp())
print(E(['/', '7', '9']).interp())
print(E(['+']).interp())


'''
3 is less than 4
2 is less than 6
3 is less than or equal to 4
7 is greater or equal to 7
7 is equal to 7
7 is not equal to 9
16
63
63
0.7777777777777778
['+']
'''
