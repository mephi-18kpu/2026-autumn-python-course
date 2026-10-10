import random
import time
from collections.abc import Callable

def read_generation_parametrs() -> tuple[int, int, int]:

    count =  int(input("Количество элементов: "))
    minimum_value = int(input("Минимальное значение: "))
    maximum_value = int(input("Максимальное значение: "))

    if count < 0:
        raise ValueError("Количество элементов не может быть отрицательным.")
    if  minimum_value > maximum_value:
        raise ValueError("Минимальное значение больше максимального.")
    return count, minimum_value, maximum_value
def generate_values(
    count: int,
    minimum_value: int,
    maximum_value: int,
) -> list[int]:

    if count < 0:
        raise ValueError("Количество элементов не может быть отрицательным.")

    if minimum_value > maximum_value:
        raise ValueError("Минимальное значение больше максимального.")

    return [
        random.randint(minimum_value, maximum_value)
        for _ in range(count)
        ]
def bubble_sort(values: list[int]) -> None:

    for end_index in range(len(values)-1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )
def measure_execution_time(
    function: Callable[...,object],
    *args: object,
) -> tuple[object, float]:
    start_time = time.time()
    result = function(*args)
    stop_time = time.time()
    return result, stop_time - start_time


