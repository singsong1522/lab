import os
import sys
print(sys.executable)
print(sys.argv)
print(os.getcwd())
for agrument in sys.argv:
    print('get an argument:',agrument)