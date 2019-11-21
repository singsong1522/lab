try:
    file1 = open('data2\\testfile1','w')
    print("this line may exception")
    file1.write('write something')
except FileNotFoundError:
    print("file will be closed")
else:
    print("file will be closed")
    file1.close()
print("do something else")
