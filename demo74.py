import functools

def my_oreo(func):
    @functools.wraps(func)
    def wrapper():
        print("upper side chocolate")
        func()
        print("---lower side chocolate---")
    return wrapper

@my_oreo
def add_regular_filling():
    print("butter cream!")

print(repr(my_oreo))
print(repr(add_regular_filling))