class Car:
    max = 20000

    def __init__(x, speed=0, color=''):
        x.speed = speed
        x.color = color

    def run(self, speed):
        self.speed = speed

    def query(self):
        return self.speed

    @classmethod
    def getMax(cls):
        return cls.max * 0.8

    @staticmethod
    def insuranceRate(year, price):
        return (1 - (0.8 * year)) * price

print(Car.getMax())
print(Car.insuranceRate(2, 200000))
c1 = Car(90)
print(c1.query(), c1.getMax(), c1.max)
c1.run(80)
print(c1.query())
c2 = Car()
print(c2.query())
c3 = Car(color='pink')
print(c3.color)
c4 = Car(speed=40)
print(c4.speed, c4.color)
c5 = Car(color='brown', speed=120)
print(c4.speed, c5.color)

