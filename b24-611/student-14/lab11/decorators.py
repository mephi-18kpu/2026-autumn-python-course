from datetime import time
from unittest import result


def empty_decorator(func):
    def wrapper():
        result = func()
        return result
    return wrapper

def timer(func):
    def wrapper():
        start_time = time()
        print(f"время начала{start_time}")
        result = func()
        end_time = time()
        print(f"время конца {end_time}")
        return result
    return wrapper


@timer
def my_func():
    print("MyFunc, sleeping")
    sleep(2)

my_func()
