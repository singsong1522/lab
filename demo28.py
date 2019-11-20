list1=[5,6,7]
total=0
for number in list1:
    total += number
print('total=%d' % total)

list2=['apple','banana','orange','watermeton']
s1="todqy ,we have:"
for fruit in list2:
    s1 += "%s," % (fruit)
print(s1)
fruit_length=[]

for f in list2:
    fruit_length.append(len(f))
print(fruit_length)

fruit_length2=[len(f) for f in list2]
print(fruit_length2)
#part2
print('apple' in list2,'kiwi' in list2)
print('apple' not in list2,'kiwi' not in list2)
a1,a2,a3,a4 =list2
print(a1,a2,a3,a4)
list2.append('passion fruit')
print(list2)


