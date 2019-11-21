class Employee(object):
    def __init__(self):
        self.work_content = 'work'
    def doWork(self):
        print('working on %s'%self.work_content)
class RD(Employee):
    def __init__(self):
        self.work_content = "Research*Development"
rd1 = RD()
rd1.doWork()
