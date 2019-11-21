def my_oreo(func):
    def wrapper(x):
        print("upper side chocolate")
        print('filling=%s'%func(x))
        print("---lower side chocolate---")
    return wrapper

@my_oreo
def add_regular_filling(fill):
    return "%s_cream" % fill

add_regular_filling('chocolate')