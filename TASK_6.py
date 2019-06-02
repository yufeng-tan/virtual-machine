# TASK 6
# (HL) Convert your J0 test-suite into Sexprs. 

# test string

string_1 = '(-3)'

string_2 = '(- 3, 2)'

#(Mult(Num(3), Num(4)))
string_3 = '(* 3, 4)'

#(Add(1, Mult(Num(3), Num(4))))
string_4 = '(+ 1, (* 3, 4))'

#(Mult(5, Mult(1, Add(3, 8))))
string_5 = '(* 5, (* 1, (+ 3, 8)))'

#(Add(8, Add(0, Mult(4, Mult(3, 2)))))
string_6 = '(+ 8, (+ 0, (* 4, (* 3, 2))))'


