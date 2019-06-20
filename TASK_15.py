# (HL) Implement a small-step interpreter for J1 using contexts. 
# It should repeatedily call find-redex and plug until there are no more redexes. 

test_string = '(if (< (+ 1 1) 5) 3 4)'
# return (if (< HOLE 5) 3 4) and (+ 1 1)
# return (if HOLE 3 4 ) and (< HOLE 5) and (+ 1 1)
