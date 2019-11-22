photos = ['data\\p1.png',
          'data\\p2.png',
          'data\\p3.png']
archives = ['data\\rar01.rar',
            'data\\rar02.rar',
            'data\\rar03.rar']

for photo in archives:
    file1 = open(photo, "rb")
    index = 1
    byte = file1.read(1)
    while byte != "" and index <9:
        x = int.from_bytes(byte, byteorder='little')
        print('%d,%s' % (index, str(hex(x))))
        byte = file1.read(1)
        index += 1
    print('-------')
    file1.close()