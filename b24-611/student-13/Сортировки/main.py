#System imports
import time
from collections.abc import Callable
# External imports

# User imports

from generate_listing import generate_value, read_generation_parametrs
from sort_function import bubble_sort, shaker_sort, gnome_sort

#############################################

def measure_execution_time(function: Callable[..., object], *args: object) -> float:
    start_time = time.time()
    function(*args)
    stop_time = time.time()

    return stop_time - start_time

def main() -> None:
    count, max_value, min_value = read_generation_parametrs()
    value = generate_value(count, max_value, min_value)
    print(value)
    sort_time = measure_execution_time(gnome_sort, value)
    print(value,"время: ", sort_time)



main()
