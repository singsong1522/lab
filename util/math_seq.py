import  util
def fib(n):
    a, b = 0, 1
    print(util.MESSAGE1, end=' ')
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()