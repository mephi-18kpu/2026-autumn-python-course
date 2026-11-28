def empty_decorator(func):
    def wrapper ():
        result = func()
        return result
    return wrapper

def timer(func):
    def wrapper():
        start_time = time()
        print(f'Start time: {start_time}')
        result = func()
        end_time = time()

        print(f'Processing time: {end_time - start_time}')
        return result
    return wrapper

def my_func():
   print('MyFunc, sleeping...')
   sleep(2)

my_func()
