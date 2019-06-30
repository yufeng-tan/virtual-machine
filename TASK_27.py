# (HL) Extend your big-step interpreter to evaluate J2 programs. 
# Add a mapping from function symbols to definitions as an argument and use your substitution function.

test_1 = ['g', '10']
test_2 = ['f', '9', '1']
test_3 = ['f', '9', ['g', '1']]
test_4 = ['+', ['g', '10'], ['f', '9', '1']]

test_5 = ['+', ['+', '4', '3'], '5']
test_6 = ['+', '4', ['+', '3', '7']]
test_7 = ['+', '2', '3']
test_8 = ['*', '4', ['+', '3', '7']]
test_9 = ['/', '40', ['+', '3', '7']]


prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

def convert(string):
    string = string.replace('(', '')
    string = string.replace(')', '')
    li = list(string.split(' '))

    return li

def subsitution(e, v):

    e = str(e)
    v = str(v)
    return e.replace('x', v)

def f(x, y):
    return (x) * 2 + (y) * (-1)

def g(x):
    return f(x, x)


def interp(lt):
    if len(lt) == 3 and lt[0] in prim_list:
        if lt[0] == '+':
            if isinstance(lt[1], list):
                num1 = interp(lt[1])
                if isinstance(lt[2], list):
                    num2 = interp(lt[2])
                    return int(num1)    + int(num2)
                else:
                    return int(num1) + int(lt[2])
            elif isinstance(lt[2], list):
                num2 = interp(lt[2])
                num1 = int(lt[1])
                return num1 + num2
            else:
                return int(lt[1]) + int(lt[2])
        if lt[0] == '*':
            if isinstance(lt[1], list):
                num1 = interp(lt[1])
                if isinstance(lt[2], list):
                    num2 = interp(lt[2])
                    return int(num1) * int(num2)
                else:
                    return int(num1) * int(lt[2])
            elif isinstance(lt[2], list):
                num2 = interp(lt[2])
                num1 = int(lt[1])
                return num1 * num2
            else:
                return int(lt[1]) * int(lt[2])
        if lt[0] == '/':
            if isinstance(lt[1], list):
                num1 = interp(lt[1])
                if isinstance(lt[2], list):
                    num2 = interp(lt[2])
                    return int(num1) / int(num2)
                else:
                    return int(num1) / int(lt[2])
            elif isinstance(lt[2], list):
                num2 = interp(lt[2])
                num1 = int(lt[1])
                return num1 / num2
            else:
                return int(lt[1]) / int(lt[2])
        if lt[0] == '-':
            if isinstance(lt[1], list):
                num1 = interp(lt[1])
                if isinstance(lt[2], list):
                    num2 = interp(lt[2])
                    return int(num1) - int(num2)
                else:
                    return int(num1) -int(lt[2])
            elif isinstance(lt[2], list):
                num2 = interp(lt[2])
                num1 = int(lt[1])
                return num1 - num2
            else:
                return int(lt[1]) - int(lt[2])
    if lt[0] == 'f' and len(lt) == 3:
        return f(int(lt[1]), int(lt[2]))

    if lt[0] == 'g' and len(lt) == 2:
        return g(int(lt[1]))





print(interp(test_5))
                
print(interp(test_6))

print(interp(test_7))

print(interp(test_8))

print(interp(test_9))

# ['+', ['g', '10'], ['f', '9', '1']]
print(interp(test_4))

#result
'''
12
14
5
40
4.0
27
'''




