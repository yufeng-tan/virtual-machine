#  Write a dozen test J3 programs, including extensions to your standard library. 

test_1 = [['let', ['x', 5], ['y', 6]], ['+', 'x', 'y']]
test_2 = [['let', ['x', 5]], ['+', 'x', 'y']]
test_3 = [['let', ['x', 5]], ['+', 'x', 'x']]
test_4 = [['let', ['x', 5]], ['+', 'x', ['let', ['x', ['+', 1, 'x']]], ['+', 'x', 'x']], ['+', 'x', 'y']]
test_5 = '((lambda(x) x) 5)'
test_6 = '(((lambda(x) (lambda(y) x)) 5) 6)'
test_7 = '((lambda(y) 5) 6)'

# nat-unfold = 
#   (lanbda rec (f Z n)
#       (if (= n 0) Z 
#           (f n (rec f Z (- n 1)))))