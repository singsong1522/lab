def infinite_generator(start=0):
    while True:
        yield  start
        start += 2

for num in infinite_generator():
    print(num, end=", ")
    if num > 50:
        break
        