str1='abc'
list1=list('abc')
print(type(str1),type(list1))
for a,b in zip(str1,list1):
    print(a,b)
print(len(str1),len(list1))
list1[1]='B'
print(list1)
str1[1]='B'
