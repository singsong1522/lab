a1 = '500'
a2 = '3.14'
a3 = '8-7j'
a4 = 'True'
a5 = 'False'
r1 = int(a1)
print(r1, type(r1))
r2 = float(a2)
print(r2, type(r2))
r3 = float(a1)
print(r3, type(r3))
r4 = complex(a1)
print(r4, type(r4))
r5 = complex(a3)
print(r5, type(r5))
r6 = bool(a4)
r7 = bool(a5)
print(r6, r7, type(r6), type(r7))