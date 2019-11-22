from collections import UserList
class MyOwnList(UserList):
    def __setitem__(self, key, value):
        if key == len(self.data):
            self.data.append(value)
        else:
            self.data[key] = value
    def square(self):
        for key in range(0, len(self.data)):
            self.data[key] = self.data[key] ** 2
l1 = MyOwnList()

for p in range(10):
    l1[p] = 2 * p
l1.square()
print(l1)
