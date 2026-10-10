
import random
import time
from collections.abc import Callable

def read_generation_parameters() -> tuple[int,int,int]:

    count=int(input("Количество элементов: "))
    minimum_value=int(input("Минимальное значение: "))
    maximum_value=int(input("Максимальное значение: "))

    if count<0:
        raise ValueError("Количество элементов не может быть отрицательным.")

    if minimum_value>maximum_value:
        raise ValueError("Минимальное значение больше максимального.")

    return count, minimum_value, maximum_value


def generative_values(
    count: int,
    minimum_value: int,
    maximum_value: int,

) -> list[int]:

    if count<0:
        raise ValueError("Количество элементов не может быть отрицательным.")

    if minimum_value>maximum_value:
        raise ValueError("Минимальное значение больше максимального.")

    return [
        random.randint(minimum_value, maximum_value)
        for _ in range(count)
    ]


