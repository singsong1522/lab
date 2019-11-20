v1=()
print(type(v1))
v2=[]
print(type(v2))
v3={}
print(type(v3))

course1 = {'id':'POOP','duration':30,'point':5.5,
           'schedule':['Saturday','Sunday'],'date':'1-Dec-2019',
           'instructor':'何孟翰'}
print('Language' in course1,'何孟翰' in course1,'id' in course1)

for k in course1:
    print([f'key={k},value={course1[k]}' for k in course1.keys()])

for v in course1.values():
    print(v)
for i in course1.items():
    print(type(1),i)

for i,j in course1.items():
    print((f"key={i},value={j}"))


#print(course1['price'])
print(course1.get('price'))


