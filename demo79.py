class Car:
    vendor = 'lexus'
    valid = True
c1 = Car()
c2 = Car()
print(c1.vendor, c2.vendor, Car.vendor)
Car.isImport = True
print(c1.isImport, c2.isImport, Car.isImport)
c1.passenger = 4
c2.color = 'red'
print(c1.passenger, c1.vendor, c1.valid, c1.isImport)
print(c2.color, c2.vendor, c2.valid, c2.isImport)
c3 = Car()
print(c3.vendor, c3.valid, c3.isImport)
