class Employee(object):
    def __init__(self):
        self.work_content = 'work'
    def doWork(self):
        print('working on %s'%self.work_content)

e1 = Employee()
e1.doWork()

class RD(Employee):
    def doWork(self):
        print("repeat & debug")
rd1 = RD()
rd1.doWork()

class FAE(Employee):
    def doWork(self):
        print("collaborate customers")
fae1 = RD()
fae1.doWork()

class Scientist(Employee):
    def doWork(self):
        print("build models")
s1=Scientist()
s1.doWork()
rd2=RD()
fae2= FAE()
s2=Scientist()
employees = [rd1,None,3.14,'hello world', rd2,
             s1, fae1, s2, fae2]
for e in employees:
    if isinstance(e, Employee):
        e.doWork()
