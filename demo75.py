import functools
import time


def timer(func):
    def wrapper_timer(*args, **kwags):
        startTime = time.perf_counter()
        value = func(*args, **kwags)
        endTime = time.perf_counter()
        runTime = endTime - startTime
        print("finished{!r} in {:.4f} seconds".format(
            func.__name__, runTime))
        return value

    return wrapper_timer
@timer
def spend_time_to_calculate(num_times):
    result = 0
    for _ in range(num_times):
        # print(sum([i**2 for i in range(10000)])) test
        result = sum([i**2 for i in range(10000)])
    return result

print(spend_time_to_calculate(1000))
# spend_time_to_calculate(1000)  test
