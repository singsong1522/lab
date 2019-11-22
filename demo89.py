class MetaSingleton(type):    #meta class test
    _instances = {}
    def __call__(self, *args, **kwargs):
        print('inside metaclass singleton')
        if self not in self._instances:
            print("object no yet created")
            print("create one")
            self._instances[self] = \
               super().__call__(*args, **kwargs)
        print('return instance')
        return self._instances[self]

class SingletonClass(metaclass=MetaSingleton):
    def __init__(self):
        print(f'SC id-{hex(id(self))}')
class RegularClass():
    pass

x1 = SingletonClass()
x2 = SingletonClass()
print(x1==x2,hex(id(x1)),hex(id(x2)))
y1 = RegularClass()
y2 = RegularClass()
print(y1==y2, hex(id(y1)),hex((id(y2))))
