l1=['apple','banana','orange','citron','grava']
l2=l1
l3=l1[:]        #[:]all element
l4=list(l1)
print(l1,l2)
l1[2]='kiwi'
print(l1,l2,l3,l4)
l3=[]
print(len(l1),len(l2), len(l3))
print(l1[:2],l1[2:],l1[1:3])
#[:2] from first to exclude 3rd
