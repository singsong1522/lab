s1 = set(list('APPLE'))
s2 = set(list('BANANA'))
print(s1, s2)
# s1.add(s2)  --> TypeError: unhashable type: 'set'
s1.add(500)
s1.add('hello world')
s1.add(3.14)
s1.add(None)
print(s1)
# unhashable=immutable; hashable=mutable;
