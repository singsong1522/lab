def getDigit(x):
    returnDigit = 0
    while x > 0:
        x= x // 10
        returnDigit += 1
    return returnDigit

print(getDigit(1024))
print(getDigit(65536))
print(getDigit(10))

