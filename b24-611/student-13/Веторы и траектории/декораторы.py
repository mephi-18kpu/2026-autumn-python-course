from time import time, sleep

def empty_decorator(func):
    def wrapper():
        result = func()
        return result
    return wrapper()

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        print(f"Время начала: {start_time}")

        result = func(*args, **kwargs)

        end_time = time()
        print(f"Время выполнения: {end_time - start_time}")

        return result
    return wrapper()

@empty_decorator
def my_func(a, b):
    print("Myfunc")

my_func(1, 2)
