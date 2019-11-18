a1 = 'c'
a2 = "c"
print(type(a1), type(a2))
a3 = b'c'
a4 = b"c"
print(type(a3), type(a3))
print(a1 == a2)
print(a3 == a4)
print(a1 == a3)
print('------------------------------------')
print(hex(id(a1)),hex(id(a2)))
a5='ABC'
a6='中文字'
print(type(a5), type(a6), len(a5), len(a6))