# (HL) Connect your test-suite to your CK0 interpreter to verify that it works. 

test_1 = 'if 2<5 true then 2 else 5 k0'
# ['if', '2<5', 'true', 'then', '2', 'else', '5', 'k0']
test_2 = 'true kif 2 5 k0'
test_3 = 'false kif 2 5 k0'

def convert(string):
    li = list(string.split(' '))
    return li


def CK0_interp(expr):
    li = convert(expr)

    if li[0] == 'if':
        lt = li[1] + ' ' + 'kif' + ' ' + li[4] + ' ' +  li[6] + ' ' + li[7]
        return convert(lt)
    if li[0] == 'true':
        lt = li[2] + ' ' + 'k0'
        return convert(lt)
    if li[0] == 'false':
        lt = li[2] + ' ' + 'k0'
        return convert(lt)

print(CK0_interp(test_1))
print(CK0_interp(test_2))
print(CK0_interp(test_3))
