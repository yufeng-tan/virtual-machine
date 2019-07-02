# Make a tweak to the CEK0 machine to give it dynamic scope, commit that, then revert it. 


# return ['delta', 'env(x)', 'mt', 'k']
test_1 = ['delta', 'x', 'mt', 'k']


# return ['delta', '<', 'env', 'kif', '2', '5', 'env', 'k']
test_4 = ['delta', ['if', '<', '2', '5'], 'env', 'k']

# return ['delta', '2', 'old_env', 'k']
test_5 = ['delta', 'true', 'new_env', 'kif', '2', '5', 'old_env', 'k']

# return ['delta', '5', 'env', 'k']
test_6 = ['delta', 'false', 'new_env', 'kif', '2', '5', 'old_env', 'k']

# return ['delta', 'e0', 'env', 'kapp', 'v0...', 'e1...', 'env', 'k']
test_7 = ['delta', 'vn', '__', 'kapp', 'v0...', 'e0...', 'env', 'k']

# return ['delta', 'delta(p, v0...vn)', 'mt', 'k']
test_8 = ['delta', 'vn', '__', 'kapp', 'pv0', ' ', '__', 'k']


# return ['delta', 'e', 'mt[x0<-v0]...[xn<-vn]', 'k'] + 'where delta(f) = (define(f x0...xn) e)'
test_9 = ['delta', 'vn', '__', 'kapp', 'fv0', ' ', '__', 'k' ]

def CEK0(expr):
    if expr[1] == 'x' and expr[2] == 'mt':
        return ['delta', 'env(x)', expr[2], expr[3]]
    if isinstance(expr[1], list):
        return ['delta', expr[1][1], expr[2], 'kif', expr[1][2], expr[1][3], expr[2],'k']
    if expr[1] == 'true':
        return ['delta', expr[4], expr[6], 'k']
    if expr[1] == 'false':
        return ['delta', expr[5], expr[6], 'k']
    if expr[4] == 'v0...':
        return ['delta', 'e0', 'env', expr[3], expr[4], 'e1...', 'env', expr[6]]
    if expr[1] == 'vn' and expr[4] == 'pv0':
        return ['delta', 'delta(p, v0...vn)', 'mt', expr[7]]
    if expr[1] == 'vn':
        def_str = 'where delta(f) = (define(f x0...xn) e)'
        li = ['delta', 'e', 'mt[x0<-v0]...[xn<-vn]', 'k']
        return [li, def_str]
    else:
        return 'Error!'


print(CEK0(test_1))

print(CEK0(test_4))

print(CEK0(test_5))

print(CEK0(test_6))

print(CEK0(test_7))

print(CEK0(test_8))

print(CEK0(test_9))


