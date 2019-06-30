# (HL) Define a substitution function that plugs the value of a variable into references to that variable. 

def subsitution(e, v):

    e = str(e)
    v = str(v)
    return e.replace('x', v)


print(subsitution('x', 5))

print(subsitution('(* 7 x)', 5))

print(subsitution('(+ (* 7 x) (* 2 (* x x)) 1)', 5))
