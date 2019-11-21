def divide(x, y):
    try:
        result = x / y
    # except FileNotFoundError:
    except ZeroDivisionError:
        print("divide by zero")
    else:
        print(f"result={result}")
    finally:
        print("calculate finished")


divide(5, 3)
divide(0, 8)
divide(8, 0)
divide(0, 0)
divide('3', '2')
