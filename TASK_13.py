# (HL) Implement plug, a function that fills the hole in a context with a program. 

class C:
    def __init__(self, list):
        self.list = list

class Add:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + '+ ' + str(self.l) + ' ' + str(self.r) + ')'

class Mult:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return '(' + '* ' + str(self.l) + ' ' + str(self.r) + ')'

def plug(list1, list2):
    tempList = []
    if 'HOLE' in list1:
        tempList = [l.replace('HOLE', str(list2)) for l in list1]
    if len(tempList) == 5:
        return '(' + ' ' +  tempList[0] + ' ' + tempList[1] + ' ' +tempList[2] + ' ' + tempList[3] + ' ' + tempList[4] + ')'
    if len(tempList) == 4:
        return '(' + ' ' +  tempList[0] + ' ' + tempList[1] + ' ' +tempList[2] + ' ' + tempList[3] + ')'

print(plug(['if', '<', 'HOLE', '3', '4'], '+ 1 1'))

print(plug(['if', 'HOLE', '3', '4'], '< 3 5'))