class Layout:
    pass
class Layout2:
    pass
l1 = Layout()
l2 = Layout2()

print(type(Layout),type(Layout2))
print(type(l1),type(l2))
print(l1.__class__,l2.__class__)