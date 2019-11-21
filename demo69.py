def my_oreo(func):
    def wrapper():
        print("upper side chocolate")
        func()
        print("---lower side chocolate---")
    return wrapper

@my_oreo
def add_regular_filling():
    print("butter cream!")

add_regular_filling()