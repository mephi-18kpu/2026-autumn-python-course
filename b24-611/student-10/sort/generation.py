# System imports
import random
import time
from collections.abc import Callable

# External imports

# User imports


def read_generation_parameters() -> tuple[int, int, int]:

    count = int(input("кол-во эл_ов"))
    minimum_value = int(input("мин значение"))
    maximum_value = int(input("макс значение"))

    if count < 0:
        raise ValueError("кол-во эл-ов не может быть <0")

    if minimum_value > maximum_value:
        raise ValueError("мин знач не может быть > макс знач")
    return count, minimum_value, maximum_value


def generate_values(

    count: int,
    minimum_value: int,
    maximum_value: int,

) -> list[int]:

    if count < 0:
        raise ValueError("кол-во эл-ов не может быть < 0")
    if minimum_value > maximum_value:
        raise ValueError("мин знач не может быть > макс знач")

    return [

        random.randint(minimum_value, maximum_value)
        for _ in range(count)

    ]
