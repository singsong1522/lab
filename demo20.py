a1 = None
a2 = None
print(type(a1), type(a2))
print(a1 == a2)
print(hex(id(a1)), hex(id(a2)))
print('-------------------------')
import ast

x1 = "None"
x2 = "None"
x3 = "None"
y1 = ast.literal_eval(x1)
print(y1, type(y1))
y2 = None if x2 == "None" else x2
print(y2, type(y2))
y3 = eval(x3)
print(y3, type(y3))
y4 = eval("2+3*4")
print(y4, type(y4))
print('------------------------------')
import util.const
print(util.const.GRAVITY)
from util import const
print(const.MAX_CONCURRENT_JOBS)
import util.const as c
print(c.PI)
