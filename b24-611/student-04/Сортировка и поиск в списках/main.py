from generation import *
import time
from collections.abc import Callable


def bubble_sort(values: list[int]) -> None:
    for end_index in range(len(values)-1,0,-1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )


def measure_execution_time(
    function: Callable[..., object],
    *args: object,
) -> tuple[object, float]:
    start_time = time.time()
    result = function(*args)
    stop_time = time.time()

    return result, stop_time - start_time


def main():
    count, minimum_value, maximum_value = read_generation_parameters()
    values = generate_values(count, minimum_value, maximum_value)
    print(values)
    res, time = measure_execution_time(bubble_sort, values)
    print(values)
    print(res, time)


main()
