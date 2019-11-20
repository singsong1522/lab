l1=[]
l2=['a','b']
l3=list('abc')
l4=[1,2,3,4]
l5=[1,2,3,'d','e']
l6=list()
l7=['a','b','c']
lists=[l2,l2,l3,l4,l5]

for l in lists:
    print(type(l),len(l),l)
print(l3==l7,l3 !=l7)
print(l3==l2,l3 !=l2)
print(l3[0]==l2[0],l3[1] !=l2[1])
# print(l1[1])  #OOR Error
print(l5[1.0])


#print(type(l1),type(l2),type(l3),type(l4),type(l5))
#print(len(l1),len(l2),len(l3),len(l4),len(l5))