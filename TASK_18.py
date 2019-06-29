# (HL) Implement the CC0 machine interpreter for J1. 

import sys

sys.setrecursionlimit(1500)

test_string = '(+ 1 (* 2 (if true 3 4)))'
test_string1 = '(+ 1 7)'
# return Num(7)


# function takes a string and returns the maximum depth nested parenthsis
def maxDepth(s):
    current_max = 0
    max = 0
    n = len(s)

    for i in range(n):
        if s[i] == '(':
            current_max += 1
            if current_max > max:
                max = current_max
        elif s[i] == ')':
            if current_max > 0:
                current_max -= 1
            else:
                return -1

    if current_max != 0:
        return -1

    return max

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

# RecursionError: maximum recursion depth exceeded in comparison
def find_redex(s):
    max_parenthsis = maxDepth(s)
    max_parenthsis_start = find_nth(test_string, '(', maxDepth(test_string))
    max_parenthsis_end = find_nth(test_string, ')', 1)
    redex = s[max_parenthsis_start:max_parenthsis_end+1]
    new_s = s.replace(redex, 'HOLE')
    return new_s + ' ' + redex

def convert(string):
    string = string.replace('(', '')
    string = string.replace(')', '')
    li = list(string.split(' '))

    return li


def kret(expr):
    if maxDepth(expr) <= 1:
        return expr
    else:
        return find_redex(expr)

def CC0(expr):
    if(maxDepth == 1):
        return expr
    else:
        if (maxDepth(expr)!=1):
            st = find_redex(expr)
            max_parenthsis = maxDepth(expr)
            max_parenthsis_start = find_nth(test_string, '(', maxDepth(test_string))
            max_parenthsis_end = find_nth(test_string, ')', 1)
            redex = expr[max_parenthsis_start:max_parenthsis_end+1]
            new_s = expr.replace(redex, 'HOLE')
            redex_result = CC0(redex)
            new_s = new_s.replace('HOLE', redex_result)
            return CC0(new_s)

        else:
            li = convert(expr)
            if li[0] == '+':
                return int(li[1]) + int(li[2])
            if li[0] == '-':
                return int(li[1]) - int(li[2])
            if li[0] == '*':
                return int(li[1]) * int(li[2])
            if li[0] == '/':
                return int(li[1]) / int(li[2])
            if li[0] == 'if':
                if li[1] == 'true':
                    return li[2]
                else:
                    return li[3]
        


    

# print(find_redex(test_string))
# (if (< HOLE 5) 3 4) (+ 1 1)

print(kret(test_string))

print(convert(test_string1))

print(CC0(test_string))

