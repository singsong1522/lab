print("hello")

if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(type(l1), type(l2))
    print(l1, l2)
    import numpy

    a1 = numpy.array(l1)
    a2 = numpy.array(l2)
    print(type(a1), type(a2))
    print(a1 + a2)