l1=list('ASHJKLQUB123498567Mashuecdflqmc')

def sortByLowercase(x):
    return str.lower(x)

l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
#l1.sort(key=str.lower)
l1.sort(key=sortByLowercase)
print(l1)

