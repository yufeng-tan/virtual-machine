# Write a test-suite of a dozen J3 programs. 

test_1 = [['let', ['x', 5], ['y', 6]], ['+', 'x', 'y']]
test_2 = [['let', ['x', 5]], ['+', 'x', 'y']]
test_3 = [['let', ['x', 5]], ['+', 'x', 'x']]
test_4 = [['let', ['x', 5]], ['+', 'x', ['let', ['x', ['+', 1, 'x']]], ['+', 'x', 'x']], ['+', 'x', 'y']]
test_5 = '((lamda(x) x) 5)'
test_6 = '(((lamda(x) (lamda(y) x)) 5) 6)'
test_7 = '((lamda(y) 5) 6)'
