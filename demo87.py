class SimpleMeta(type):  #meta class
    #def __new__(cls, *args, **kwargs):
    def __new__(cls, className, superClasses,
                attributeDict):
        print(f"類別名稱是:{className}")
        print(f'父類別是:{superClasses}')
        print(f"其餘屬性:{attributeDict}")
        return type.__new__(cls, className,
                            superClasses,attributeDict)
class S:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class A(S, metaclass=SimpleMeta):
    pass
s1 = S('James',20)
print(type(s1), s1.__class__,s1.__class__.__bases__)
print(s1.name, s1.age)
print('now, will prepare a1')
a1 = A('Mark',43)
print('now, a1 generated')
print(a1.name, a1.age)
print(type(a1),a1.__class__, a1.__class__.__bases__)