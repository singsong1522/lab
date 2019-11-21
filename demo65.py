def make_increment(n):
    return lambda x: x + n
print(type(make_increment))
print(type(make_increment(5)))
f = make_increment(10)
print(f(10),f(20))


def make_increment_detail(n):
    def becomeLamda(x):
        return  x + n

    return  becomeLamda

g = make_increment_detail(10)
print(g(10), g(20))

def make_tuple(p):
    return  lambda x: (x, 'p' * p)

g2 = make_tuple(5)
print(g2(1),g2(2),g2(3))