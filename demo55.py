try:
    with open('data2\\testfile1','w') as file1:
         file1.write("write something")
    # file will be closd here
except:
    print("something bad....")