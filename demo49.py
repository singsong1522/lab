a1 =range(10)
print(a1,type(a1),len(a1),list(a1))
print([x for x in a1])

a2 = range(5,10)
print([x for x in a2])

a3 =range(50,100,2)
print([x for x in a3])

for i in range(10):
    print('*',end="")
print()
for _ in range(10):
    print('*',end='')
print()

import math
a4 = range(0,int(math.pi))
print([x for x in a4])

import numpy
a6=numpy.arange(0,1,0.1)
print([x for x in a6])

a7 = numpy.arange(0,numpy.pi,0.1)
print([x for x in a7])

a8 = numpy.linspace(0,numpy.pi)
print(len(a8),a8)

