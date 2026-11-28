from time import time, sleep


def empty_decorator(func):
    def wrapper():
        result = func()
        return  result
    return wrapper()

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        print(f"start_time: {start_time}")
        result = func()
        end_time = time()

        print(f"Processing time: {end_time - start_time}")
        return  result
    return wrapper

def repeat(n):
    ...


@repeat(100)
def my_func(a, b):
    print(f"MyFunc, a = {a}, b = {b}, sleeping...")
    sleep(2)


#my_func = empty_decorator(my_func)

my_func(1,2)

# @empty_decorator
# def my_func():
#     print("MyFunc")
