from collections import UserDict

class MyOwnDict(UserDict):
    def __init__(self, data ={}, **kwargs):
        super().__init__()
        self.update(data)
        self.update(kwargs)
    def __add__(self, other):
        self.data.update(other)
        return self

x1 = {'name':'pyoo'} #error input
x2 = {'duration':35} #error input
#print(x1+x2)

y1 = MyOwnDict(codeName='PYOO')
y2 = MyOwnDict(duration=35)
y3 = MyOwnDict(instructor='MarkHo')
#y4 = MyOwnDict(recommand={'follow':'BDPY'})
y4 = MyOwnDict({'follow':'BDPY'}) #test ..step debug...
print(y1)
print(y1 + y2)
print(y1+y2+y3)
print(y1+y2+y3+y4)

