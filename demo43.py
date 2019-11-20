sales=['S','M','L','L','M','L','L','S','M','S','M','L','L']
statistics={}

for r in sales:
    statistics.setdefault(r,0)
    statistics[r] += 1
print(statistics)

sales2=[('S',20),('M',30),('L',40),
        ('S',20),('M',30),('L',40),
        ('S',20),('M',30),('L',40),
        ('S',20),('M',30),('L',40)]

statistics2={}
for r,q in sales2:
    statistics2.setdefault(r,0)
    statistics2[r] += q
print(statistics2)
