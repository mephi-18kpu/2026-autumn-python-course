from time import time, sleep

def empty_decorator(func):
    def wrapper():
        result = func()
        return result
    return wrapper()

def timer(func):
    def wrapper():
        start_time = time()
        print(f"Время начала: {start_time}")
        result = func()
        end_time = time()
        print(f"Время konca: {end_time-start_time}")
        return result
    return wrapper

@timer
def my_func():
    print("eeee")
    sleep(2)

my_func()
