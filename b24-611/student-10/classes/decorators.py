



'''
def empty_decorator(func):
    def wrapper():
        result = func()
        return result
    return wrapper

@empty_decorator
def my_func():
    print("MyFunc")

my_func = empty_decorator(my_func)
'''
