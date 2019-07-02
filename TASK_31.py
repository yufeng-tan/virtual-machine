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

# return ['delta', 'e0', 'env', 'kapp', 'v0...', 'e1...', 'k']
test_7 = ['delta', 'vn', 'env', 'kapp', 'v0...', 'e0...', 'k']

# return ['delta', 'delta(p, v0...vn)', 'env', 'k']
test_8 = ['delta', 'vn', 'env', 'kapp', 'pv0', 'v0', ' ', 'k']

# return 'Let define (f x0...) e) = delta f' + ['delta', 'e', 'env[x0->v0]', 'k']
test_9 = ['delta', 'vn', 'env', 'kapp', 'fv0', ' ', 'k' ]

def CEK0(expr):
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
    if expr[4] == 'v0...':
        return ['delta', 'e0', expr[2], expr[3], expr[4], 'e1...', expr[6]]
    if expr[1] == 'vn' and expr[4] == 'pv0':
        return ['delta', 'delta(p, v0...vn)', expr[2], expr[7]]
    if expr[1] == 'vn':
        def_str = 'Let define (f x0...) e) = delta f'
        li = ['delta', 'e', 'env[x0->v0]', 'k']
        return [def_str, li]
    else:
        return 'Error!'


print(CEK0(test_1))

print(CEK0(test_2))

print(CEK0(test_3))

print(CEK0(test_4))

print(CEK0(test_5))

print(CEK0(test_6))

print(CEK0(test_7))

print(CEK0(test_8))

print(CEK0(test_9))
