course1 = {'name':'python','instructor':'mark'}
course2 = {'instructor':'mark','name':'python'}
print(course1==course2)
print(course1)
print(course2)
print(course1['name'])
print(course2['instructor'])
course1['duration']=20
print(course1)
course3=dict(name='python',instructor='mark')
print(type(course3),course3)
course4=dict([('name','python'),('instructor','mark')])
print(course4)
