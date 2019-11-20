l1=[3,1,4,5,9,14,24,30]

sum=0
for l in l1:
    sum += l
print("sum={}".format(sum))
numbers = [6,-5,3,-8,4,-2,5,-4,11]
for n in numbers:
    if n < 0:
        numbers.remove(n)
print(numbers)

numbers2 = [6,-5,3,-8,4,-2,5,-4,11]
for n in numbers2[:]:
    if n < 0:
        numbers2.insert(0,n)
print(numbers2)


