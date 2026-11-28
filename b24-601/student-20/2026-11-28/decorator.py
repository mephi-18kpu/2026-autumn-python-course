from time import time, sleep

def empty_decorator(func):
    def wrapper():
        result = func()
        return result
    return wrapper()

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        print(f"Start time: {start_time}")
        result = func(*args, **kwargs)
        end_time = time()
        print(f"End time: {end_time}")

        print(f"Processing time: {end_time - start_time}")
        return result
    return wrapper

@timer
def my_func(a, b):
    print(f"MyFunc a = {a}, b = {b}, sleeping...")
    sleep(2)

my_func(1, 2)
