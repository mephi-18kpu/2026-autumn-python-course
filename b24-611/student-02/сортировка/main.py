from generation import *
from bubble_sort import bubble_sort
import time


def main():
    count, minimum_value, maximum_value = read_generation_parameters()
    values = generate_values(count, minimum_value, maximum_value)
    print(values)

    bubble_sort(values)
    print(values)


def measure_execution_time(
    function: Callable[..., object],
    *args: object,
) -> tuple[object, float]:
    start_time = time.time()
    result = function(*args)
    stop_time = time.time()

    return result, stop_time - start_time


main()
