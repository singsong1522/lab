output1 = open("data\\output1.txt",'w')
linesToWrite = ["Hi, I am Mark\n","I would like to re-write"]
output1.writelines(linesToWrite)
output1.close()

for _ in range(50):
    output2 = open('data\\output2.txt', 'a')
    nextLines = ['\n add something']
    output2.writelines(nextLines)
    output2.close()