s1 = {'A'}
print(type(s1),len(s1))
s2 ={}
print(type(s2))
s3=set()
print(type(s3),len(s3))
s4 = {'A','P','P','L','E'}
s5 = set(list('BANANA'))
print(s4)
print(s5)
print(s4|s5)
print(s4&s5)
print(s4^s5)
s4.add('X')
print(s4)
s4.remove('X')
print(s4)
# s4.remove('X')  --> KeyError: 'X'

