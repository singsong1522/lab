import struct
output1 = open('data\\demo96.binary','wb')
output2 = open('data\\demo96.ascii','w')

for i in range(100):
    packedI = repr(struct.pack('i',i))
    print(f'i={i}, pack={packedI}')
    output1.write(struct.pack('i',i))
    output2.write('%s\n' % str(i))
output1.close()
output2.close()

input1 = open('data\\demo96.binary',"rb")
block = input1.read(400)
str = ""
for ch in block:
    str += hex(ch) + " "
print(str)
input1.close()

