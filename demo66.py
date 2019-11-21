class Counter(object):
    def __init__(self, low, high):
        print('object construct')
        self.current = low
        self.high = high
    def __iter__(self):
        print('prepare to interate')
        return self
    def __next__(self):
        print('next')
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return  self.current -1
c = Counter(1,10)
print(type(c))
print([l for l in c])

