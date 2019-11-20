l1=list('ABCXZ')
print(l1.index('C'),l1.index('Z'))
# print(l1.index('Q')) OOR Error
print(l1.count('Q'),l1.count('C'),l1.count('Z'))
l2=list('ASDFGHJKL')
for l in l2:
    print(l in l1 and l1.index(l),end=', ')

