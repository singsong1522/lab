class SingletonParent(object):
    _instance = None

    def __init__(self):
        print('init is called')

    def __new__(cls, *args, **kwargs):
        print('new is called')
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
class SingleClass(SingletonParent):
    pass
s1 = SingleClass()
s2 = SingleClass()
print(hex(id(s1)), hex(id(s2)), s1 == s2)
class NormalClass():
    pass
s3 = NormalClass()
s4 = NormalClass()
print(hex(id(s3)), hex(id(s4)), s3 == s4)

