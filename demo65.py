def make_increment(n):
    return lambda x: x + n

f = make_increment(10)
print(f(10),f(20))

def make_increment_detail(n):
    def becomeLamda(x):
        return  x + n

    return  becomeLamda

g = make_increment_detail(10)
print(g(10), g(20))


