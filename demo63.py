def foo():
    y="local"
    print('inside y=%s' % y)

foo()
#print(y)
x=5

def bar():
    x = 10
    print("Local x=%d" % x)

bar()
print("x=%d" % x)

def outer():
    x2 = "local"
    def inner():
        nonlocal x2
        x2 = "non local"
        print(f"inner:{x2}")
    print(f"outer1:{x2}")
    inner()
    print(f"outer2:{x2}")
outer()


