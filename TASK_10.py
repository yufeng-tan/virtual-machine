# TASK 10
# (HL) Extend desugar to emit J1 programs.

# test strings
string_1 = 'if, A is bigger than B, return A, return B'
string_2 = 'if, >= 4 2, 4, 2'
string_3 = '(* 3, 4)'
string_4 = 'abc,123,def,456, ghi'


def desugar(s):
    sexpr = str(s)

    if sexpr.startswith('(') and sexpr.endswith(')'):
        sexpr = sexpr[1:-1]

    # operator == '-'
    if sexpr[0] == '-' and ',' not in sexpr:
        sexpr_2 = sexpr[1:]
        return ('(' + '*' + ' ' + '-1' + ',' + desugar(sexpr_2) + ')')
    elif sexpr[0] == '-' and ',' in sexpr:
        sexpr_1 = sexpr[1:].split(',')[0]
        sexpr_2 = sexpr[1:].split(',')[1]
        return ('(' + '+' + ' ' + desugar(sexpr_1) + ',' + desugar('-' + sexpr_2) + ')')
    elif sexpr[0] == '+' and ',' not in sexpr:
        return '0'
    elif sexpr[0] == '+' and ',' in sexpr:
        sexpr_1 = sexpr[1:].split(',')[0]
        sexpr_2 = sexpr[1:].split(',')[1]
        return ('(' + '+' + ' ' + desugar(sexpr_1) + ',' + desugar(sexpr_2) + ')')
    elif sexpr[0] == '*' and ',' not in sexpr:
        return '1'
    elif sexpr[0] == '*' and ',' in sexpr:
        sexpr_1 = sexpr[1:].split(',')[0]
        sexpr_2 = sexpr[1:].split(',')[1]
        return ('(' + '*' + ' ' + desugar(sexpr_1) + ',' + desugar(sexpr_2) + ')')
    elif sexpr[:2] == 'if' and ',' in sexpr:
        sexpr_1 = sexpr[2:].split(',')[1]
        sexpr_2 = sexpr[2:].split(',')[2]
        sexpr_3 = sexpr[2:].split(',')[3]
        return ('(' + sexpr[0:2] + ',' + sexpr_1 + ',' + sexpr_2 + ',' + sexpr_3 + ')')
    elif ',' in sexpr:
        ne = sexpr.split(',')
        return str(ne)
    else: return sexpr


print(desugar(string_1))

print(desugar(string_2))

print(desugar(string_3))

print(desugar(string_4))