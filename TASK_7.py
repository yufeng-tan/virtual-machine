# TASK 7
# (HL) Implement a desugar function that converts Sexprs into J0. 
# Test it by verifying that the J0 Sexprs produce the original J0 examples. 
# From now on, whenever you write test programs, write them as Sexprs and run them through desugar.

# test string

# (-3) = (* -1, desugar(3))
string_1 = '(-3)'

string_2 = '(- 30, 2)'

#(Mult(Num(3), Num(4)))
string_3 = '(* 3, 4)'

#(Add(1, Mult(Num(3), Num(4))))
string_4 = '(+ 1, (* 3, 4))'


def desugar(s):
    sexpr = str(s).replace(' ', '')

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
    else: return sexpr

        

    #print(sexpr)

print(desugar(string_3))





#(Mult(5, Mult(1, Add(3, 8))))
string_5 = '(* 5, (* 1, (+ 3, 8)))'

#(Add(8, Add(0, Mult(4, Mult(3, 2)))))
string_6 = '(+ 8, (+ 0, (* 4, (* 3, 2))))'

