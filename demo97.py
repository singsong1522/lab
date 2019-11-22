import unittest

def fun(x):
    return x+1

class MyTest1(unittest.TestCase):
    def setUp(self):
        print('prepare data')
    def tearDown(self) -> None:
        print('store record')
    def test1(self):
        print('test1...')
        self.assertEqual(fun(3), 4)
    @unittest.skip("bug #31245")
    def test2(self):
        print('test2...')
        self.assertEqual(fun(-1), 1)

if __name__ == '__main__':
    unittest.main()

