import copy

l1=list('ABCDE')
l2=l1
l3=l1[:]
l4=list(l1)
print(l1,l2,l3,l4)
l5=copy.copy(l1)
l6=copy.deepcopy(l1)
print(l5,l6)
print(hex(id(l1)))
print(hex(id(l5)))
print(hex(id(l6)))
l1[0]='a'
l2[1]='b'
print(l1,l2,l3)
print(l4,l5,l6)

import numpy
a1=numpy.array([1,2,3,4,5])
a2=a1
a3=a1.copy()
print(a1,a2,a3)
a1*=2
print(a1,a2,a3)
print(hex(id(a1)))
print(hex(id(a2)))
print(hex(id(a3)))

