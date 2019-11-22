class SimpleMeta(type):  #meta class 學習
    #def __new__(cls, *args, **kwargs):
    def __new__(cls, className, superClasses,
                attributeDict):
        print(f"類別名稱是:{className}")
        print(f'父類別是:{superClasses}')
        print(f"其餘屬性:{attributeDict}")
        return type.__new__(cls, className,
                            superClasses,attributeDict)
    def __call__(self, *args, **kwargs):
        print('prarameter passes in:')
        for a in args:
            print(a)
        return super().__call__(*args, **kwargs)

class S:
    def __init__(self, name, age):
        print("init in S")
        print("customize in S")
        self.name = name
        self.age = age
class A(S, metaclass=SimpleMeta):
    def __init__(self, name, age):
        print("init in A")
        super().__init__(name, age)
        print("customize in A")
    pass

a1 = A("Mark",43)
#a1 = A()
print(a1.name, a1.age)