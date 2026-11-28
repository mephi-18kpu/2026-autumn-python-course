import random
import time
from _collections_abc import Callable

def read_generation_par() -> tuple[int, int, int]:
    count = int(input("колво элементов: "))
    min_value = int(input("мин значение: "))
    max_value = int(input("макс значение: "))

    if count < 0:
        raise ValueError("олво элементов не отрицательное")

    if min_value > max_value:
        raise ValueError("мин значение больше макс")

    return count, min_value, max_value

def gen_values(
    count: int,
    min_value: int,
    max_value: int,
) -> list[int]:

    if count < 0:
        raise ValueError("kолво элементов не отрицательное")

    if min_value > max_value:
        raise ValueError("мин значение больше макс")

    return [ random.randint(min_value, max_value)
             for _ in range(count) ]


def bubble_sort(values: list[int]) -> None:

    for end_index in range(len(values) - 1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1], values[index])

def show_arg(*args: int) -> None:
    print(args)

numbers = [3, 1, 2]
show_arg(3, 2, 1)
show_arg(*numbers)


