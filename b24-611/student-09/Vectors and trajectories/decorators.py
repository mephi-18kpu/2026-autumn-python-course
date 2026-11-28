#System imports

#External imports
from time import time, sleep

from numpy.typing import mypy_plugin


#User imports

########################

def emptydecorator(func):
    def wrapper():
        result=func()
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        start_time = time()
        print(f'Start time: {start_time}')
        end_time = time()
        print(f'Execution time: {end_time-start_time}')
        return result
    return wrapper

@timer
def my_func():
    sleep(2)
    print("MyFunc")


my_func()
