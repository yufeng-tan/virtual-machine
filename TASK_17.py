# (HL) Refine find-redex so that it looks for evaluation contexts. 

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

prim_list = ['+', '*', '/', '-', '<=', '<', '=', '>', '>=']

class V:
    def __init__(self, v):
        if isinstance(v, (int, bool)) or str(v) in prim_list:
            self.v = v
        else:
            self.v = 'error'

    def interp(self):
        return self.v

    def __str__(self):
        return str(self.interp())


class E:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        if self.list[0] == 'HOLE':
            return 'HOLE'
        if self.list[0] == 'if' and (self.list[1] == 'true' or self.list[1] == 'false') and len(self.list) == 4:
            if self.list[1] == 'true':
                return 'E[' + self.list[2] + ']'
            if self.list[1] == 'false':
                return 'E[' + self.list[3] + ']'
        if isinstance(self.list[0], V):
            return str(self.list)

def find_redex(s):
    max_parenthsis = maxDepth(s)
    max_parenthsis_start = find_nth(test_string, '(', maxDepth(test_string))
    max_parenthsis_end = find_nth(test_string, ')', 1)
    redex = s[max_parenthsis_start:max_parenthsis_end+1]
    new_s = s.replace(redex, 'HOLE')
    return new_s + ' ' + redex
    

print(find_redex(test_string))
# (if (< HOLE 5) 3 4) (+ 1 1)
