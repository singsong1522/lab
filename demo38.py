animals=['alpaca','baboon']
def addAnimal(x):
    x.append('zebra')

print(hex(id(animals)),animals)
addAnimal(animals)
print(hex(id(animals)),animals)
animals2=('alpaca','baboon')
y=3.14
z=500
def addAnimal2(x):
    x += ('zebra',)
    print('inside,x={},{},{}'.format(x,3.14,500))
    print(f'inside,x={x},{y},{z}')

print(hex(id(animals2)),animals2)
addAnimal2(animals)
print(hex(id(animals2)),animals2)