class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __eq__(self, other):
        return self.name == other.name and \
               self.duration == other.duration

    def __hash__(self):
        return hash((self.name,self.duration))

    def __str__(self):
        return f'[{self.name}]{self.duration}'

    def __repr__(self):
        return f'[{self.name}]{self.duration}'

c1 = Course('POOP',35)
c2 = c1
c3 = Course('POOP',35)
c4 = Course('BDPY',35)
s1 = {c1}
print(type(s1), s1, hex(hash(c1)))
print(hex(hash(c2)),hex(hash(c3)),hex(hash(c4)))

s1.add(c2)
print(s1)
s1.add(c3)
print(s1)
s1.add(c4)
print(s1)



