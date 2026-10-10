import random
import time
from collections.abc import Callable

def read_generation_parameters() -> tuple[int, int, int]:

    count = int(input("количество элементов: "))
    minimum_value = int(input("минимальное значение: "))
    maximum_value = int(input("максимальное значение: "))

    if count < 0:
        raise ValueError("Количество элементов не может быть отрицательным")
    if minimum_value > maximum_value:
        raise  ValueError("минимальное значение больше максимального")

    return count, minimum_value, maximum_value

def generate_values(
    count: int,
    minimum_value: int,
    maximum_value: int,
) -> list[int]:

    if count < 0:
        raise ValueError("количество элементов не может быть отрицательным.")

    if minimum_value > maximum_value:
        raise ValueError("минимальное значение больше максимального")

    return [
        random.randint(minimum_value, maximum_value)
        for _ in range(count)
    ]
