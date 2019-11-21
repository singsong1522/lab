class Car:
    def __init__(self):
        self.speed = 0
    def run(self, speed):
        self.speed = speed
        pass
    def query(self):
        return self.speed
c1 = Car()
print(c1.query())
c1.run(80)
print(c1.query())
