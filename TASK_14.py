# (HL) Implement find-redex, a function that breaks a term into a context and a redex. 


test_string = '(if (< (+ 1 1) 5) 3 4)'
# return (if (< HOLE 5) 3 4) and (+ 1 1)


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

def find_redex(s):
    max_parenthsis = maxDepth(s)
    max_parenthsis_start = find_nth(test_string, '(', maxDepth(test_string))
    max_parenthsis_end = find_nth(test_string, ')', 1)
    redex = s[max_parenthsis_start:max_parenthsis_end+1]
    new_s = s.replace(redex, 'HOLE')
    return new_s + ' ' + redex
    

print(find_redex(test_string))
# (if (< HOLE 5) 3 4) (+ 1 1)   
