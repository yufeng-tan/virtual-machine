# Extend your CK0 machine into the CK1 to evaluate J2 programs. 


test_1 = 'delta if 2<5 true then 2 else 5 k'
test_2 = 'delta true kif 2 5 k'
test_3 = 'delta false kif 2 5 k'
test_4 = ['delta', '+', ['g', '10'], ['f', '9', '1'], 'k']

prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

def convert(string):
    li = list(string.split(' '))
    return li

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


# test_4 = ['delta', '+', ['g', '10'], ['f', '9', '1'], 'k']
def CK1(expr):
    if isinstance(expr, list):
        li = expr[1:-1]
        rst = interp(li)
        lt = 'delta' + ' ' + str(rst) + ' ' + 'k'
        return convert(lt)
        
    else:
        li = convert(expr)

        if li[1] == 'if':
            lt = 'delta' + ' ' + li[2] + ' ' + 'kif' + ' ' + li[5] + ' ' +  li[7] + ' ' + li[8]
            return convert(lt)
        if li[1] == 'true':
            lt = 'delta' + ' ' + li[3] + ' ' + 'k'
            return convert(lt)
        if li[1] == 'false':
            lt = 'delta' + ' ' + li[3] + ' ' + 'k'
            return convert(lt)

print(CK1(test_1))
print(CK1(test_2))
print(CK1(test_3))
print(CK1(test_4))

