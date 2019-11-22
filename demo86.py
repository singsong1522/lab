from abc import ABC, abstractmethod
class A1(ABC):
    def __init__(self, value):
        super().__init__()
        self.value = value
        pass
    @abstractmethod
    def doSomething(self):
        pass
class B1(A1):
    def doSomething(self):
        print('value={}'.format(self.value))
    pass
b1 = B1(300)
#a1 = A1(400)
print(type(b1),)
b1.doSomething()
