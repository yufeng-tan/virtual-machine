# Extend CEK0 to CEK1 to evaluate J3 programs. 

test_1 = [['lambda', 'x'], 5]

def CEK1(expr):
    if isinstance(expr[0], list):
        if expr[0][0] == 'lambda' and len(expr[0]) == 2:
            return expr[1]
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

print(CEK1(test_1))