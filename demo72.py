def my_oreo(func):
    def wrapper(*x):
        print("upper side chocolate")
        func(*x)
        print("---lower side chocolate---")
    return wrapper

@my_oreo
def add_regular_filling(*fills):
    for f in fills:
        print("%s_butter cream!"%f)

add_regular_filling('cherry')
fillings=['apple','chocolate','blueberry']
add_regular_filling(*fillings)
