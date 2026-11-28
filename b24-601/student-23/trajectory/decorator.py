from time import  time, sleep

def empty_decorator(func):
    def wrapper():
        result = func()
        return result
    return wrapper

def tirmer(func):
    def wrapper():
        start_time = time()
        print(f"Start_time: {start_time}")
        result = func(*args, **kwargs)
        end_time = time()

        print(f"Processing time: {end_time - start_time}")
        return result
    return wrapper

@tirmer
def my_func(a, b):
    print("MyFunc, a = {a}, b = {b}, sleeping...")
    sleep(2)

my_func()


