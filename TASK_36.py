# (HL) Extend desugar to support let expressions. 

prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

test_1 = [['let', ['x', 5], ['y', 6]], ['+', 'x', 'y']]
test_2 = [['let', ['x', 5]], ['+', 'x', 'y']]
test_3 = [['let', ['x', 5]], ['+', 'x', 'x']]
#test_2 = [['let', ['x', 5]], ['+', 'x', ['let', ['x', ['+', 1, 'x']]], ['+', 'x', 'x']], ['+', 'x', 'y']]

def desuger(lt):
    if lt[0][0] == 'let':
        if len(lt[0]) == 2:
            x = lt[0][1][1]
            if lt[1][1] == lt[0][1][0]:
                lt[1][1] = x
                if lt[1][2] == lt[0][1][0]:
                    lt[1][2] = x                       
                    return desuger(lt[1])
                else:
                    return 'error'
        if len(lt[0]) == 3:
            x = lt[0][1][1]
            y = lt[0][2][1]
            if lt[1][1] == lt[0][1][0] and lt[1][2] == lt[0][2][0]:
                lt[1][1] = x
                lt[1][2] = y
                return desuger(lt[1])
            else:
                return 'error'
    if len(lt) == 4 and lt[0] == 'if':
        if lt[1] == '<=':
            if lt[2] <= lt[3]:
                return lt[2]
            else:
                return lt[3]
        if lt[1] == '<':
            if lt[2] < lt[3]:
                return lt[2]
            else:
                return lt[3]
        if lt[1] == '=':
            if lt[2] == lt[3]:
                return lt[2]
            else:
                return 'false'
        if lt[1] == '>':
            if lt[2] > lt[3]:
                return lt[2]
            else:
                return lt[3]
        if lt[1] == '>=':
            if lt[2] >= lt[3]:
                return lt[2]
            else:
                return lt[3]
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

print(desuger(test_3))
print(desuger(test_2)) 
print(desuger(test_1)) 