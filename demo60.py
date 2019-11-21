def outer(num1):
    def inner_increment(x):
        return x+1
    num2 = inner_increment(num1)
    print(num1, num2)
#inner_increment(40) 不能在外面引用
outer(50)
