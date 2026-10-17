#System imports
import time
from collections.abc import Callable
# External imports

# User imports
<<<<<<< Updated upstream
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
=======
from generate_listing import read_generation_parametrs, generate_value
from sort_function import bubble_sort
#############################################
def measure_time(function: Callable[..., object], *args: object) -> tuple[object, float]:
    start_time = time.time()
    result = function(*args)
    stop_time = time.time()

    return result, stop_time - start_time



def main() -> None:
    parametrs = read_generation_parametrs()
    values = generate_value(parametrs[0], parametrs[1], parametrs[2])
    print(values)
    result = measure_time(bubble_sort, values)
    print(result[1], values)

>>>>>>> Stashed changes


main()
