x1='apple'
x2='banana'
x1,x2=x2,x1
print(x1,x2)
x3=3.14
x4=None
x3,x4=x4,x3
print(x3,x4)
v1=['a','b','c']
t1=('a','b','c')
#v1.append('d')
t2=tuple(v1)
v2=list(t1)
v2.append('d')
print(type(t2),type(v2),v2)

