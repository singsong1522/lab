x='golbal'
def foo():
    print(f'[foo]x={x}')
foo()

y='global2'
def bar():
    y='local2'
    print(f'[bar]y={y}')
bar()

z = 5


def calculate():
    global z
    # z = 3
    print('1[calculate]z=%d' % z)
    z *= 2
    print('2[calculate]z=%d' % z)


calculate()
print('outside, z=%d' % z)

p = [5]


def calculate2():
    print('1[calculate2]p=%d' % p[0])
    p[0] *= 2
    print('2[calculate2]p=%d' % p[0])


print('outside, p=%d' % p[0])
calculate2()
print('outside, p=%d' % p[0])


class DemoObject:
    def __init__(self, value):
        self.value = value


q1 = DemoObject(5)


def calculate3(obj):
    print('1[calculate3]q=%d' % obj.value)
    obj.value *= 2
    print('2[calculate3]q=%d' % obj.value)
print('q1.value=%d'%q1.value)
calculate3(q1)
