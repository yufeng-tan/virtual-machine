# Modify your CK1 machine into the CEK0 machine. 


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
        def_str = 'Let define (f x0...) e) = delta F'
        li = ['delta', 'e', 'env[x0->v0]', 'k']
        return [def_str, li]
    else:
        return 'Error!'
