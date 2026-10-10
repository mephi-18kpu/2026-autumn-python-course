import random

def read_generation_parameters() -> tuple[int,int,int]:
    count = int(input("Amount of elements"))
    minimum_value = int(input("min value"))
    maximum_value = int(input("max value"))
    if count < 0:
        raise ValueError ("Колво элементов не може быть отрицательным")
    if minimum_value > maximum_value:
        raise ValueError ("Минимальное знаычение не может быть больше максимально")
    return count, minimum_value, maximum_value


def generate_values(
    count: int,
    minimum_value: int,
    maximum_value: int,
) -> list[int]:
    if count < 0:
        raise ValueError ("Колво элементов не може быть отрицательным")
    if minimum_value > maximum_value:
        raise ValueError ("Минимальное знаычение не может быть больше максимально")
    return [
        random.randint(minimum_value, maximum_value)
        for _ in range(count)
    ]

