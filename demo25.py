l1 =list('abc')
l2=l1
print(l1==l2)
l3=list(l1)
print(l1==l3)
print(hex(id(l1))==hex(id(l2)))
print(hex(id(l1))==hex(id(l3)))
