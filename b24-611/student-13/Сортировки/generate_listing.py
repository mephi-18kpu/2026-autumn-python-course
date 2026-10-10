#System imports
import random
import time
# External imports

# User imports

#############################################

def read_generation_parametrs() -> tuple[int, int, int]:
    count = int(input("Введите количество элементов: "))
    max_value = int(input("Введите максимальный элемент: "))
    min_value = int(input("Введите минимальный элемент: "))

    if count < 0:
        raise ValueError("Количесвто элементов не может быть отрицательным")
    if max_value < min_value:
        raise ValueError("Максимальный элемент меньше минимального")

    return count, max_value, min_value

def generate_value(count: int, max_value: int, min_value: int) -> list[int]:
    if count < 0:
        raise ValueError("Количесвто элементов не может быть отрицательным")
    if max_value < min_value:
        raise ValueError("Максимальный элемент меньше минимального")

    listing = list[]

    for x in range(count):
        listing[x - 1] = random.randint(min_value, max_value)
    return list
