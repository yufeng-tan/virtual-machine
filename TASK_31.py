# Write test cases that verify your CEK0 machine does NOT have dynamic scope. 

# return error
test_1 = ['delta', 'x', 'mt', 'k']

# return ['delta', '3', mt, 'k']
test_2 = ['delta', 'x', ['x', '3'], 'k']

# return ['delta', 'x', 'env', 'k' ]
test_3 = ['delta', 'x', ['y', '3'], 'k']

# return ['delta', '<', 'env', 'kif', '2', '5', 'k']
test_4 = ['delta', ['if', '<', '2', '5'], 'env', 'k']

# return ['delta', '2', 'env', 'k']
test_5 = ['delta', 'true', 'env', 'kif', '2', '5', 'k']

# return ['delta', '5', 'env', 'k']
test_6 = ['delta', 'false', 'env', 'kif', '2', '5', 'k']

# return 'Let define (f x0...) e) = delta f' + ['delta', 'e', 'env[x0->v0]', 'k']
test_7 = ['delta', 'vn', 'env', 'kapp', 'fvo', ' ', 'k' ]

def CK1(expr):
    if expr[1] == 'x' and expr[2] == 'mt':
        return 'error'
    if expr[1] == 'x' and isinstance(expr[2], list) and expr[1] == expr[2][0]:
        expr[1] = expr[2][1]
        expr[2] = 'mt'
        return expr
    if expr[1] == 'x' and isinstance(expr[2], list) and expr[1] != expr[2][0]:
        expr[2] = 'env'
        return expr
    if isinstance(expr[1], list):
        return ['delta', expr[1][1], 'env', 'kif', expr[1][2], expr[1][3], 'k']
    if expr[1] == 'true':
        return ['delta', expr[4], 'env', 'k']
    if expr[1] == 'false':
        return ['delta', expr[5], 'env', 'k']
    if expr[1] == 'vn':
        def_str = 'Let define (f x0...) e) = delta f'
        li = ['delta', 'e', 'env[x0->v0]', 'k']
        return [def_str, li]
    else:
        return 'Error!'


print(CK1(test_1))

print(CK1(test_2))

print(CK1(test_3))

print(CK1(test_4))

print(CK1(test_5))

print(CK1(test_6))

print(CK1(test_7))
