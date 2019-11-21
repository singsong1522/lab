def my_oreo(func):
    def wrapper(x):
        print("upper side chocolate")
        func(x)
        print("---lower side chocolate---")
    return wrapper

@my_oreo
def add_regular_filling(fill):
    print("%s_butter!" % fill)

add_regular_filling('mint_chocolate')
add_regular_filling('vanilla')