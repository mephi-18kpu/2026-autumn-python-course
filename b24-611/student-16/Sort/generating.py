import random
import time

def read_param() -> tuple[int, int, int]:
    count = int(input("Колво элементов: "))
    min_bound = int(input("Минимальное значение: "))
    max_bound = int(input("Максимальное значение: "))

    if (count < 0) :
        raise ValueError("Количество не может быть меньше 0")

    if min_bound > max_bound:
        raise ValueError("Нижняя граница не может быть больше верхней")


    return count, min_bound, max_bound

def generating(count: int, min_bound: int, max_bound: int) -> list[int]:

    if (count < 0) :
        raise ValueError("Количество не может быть меньше 0")
    if min_bound > max_bound:
        raise ValueError("Нижняя граница не может быть больше верхней")

    return [random.randint(min_bound, max_bound) for i in range(count)]

def bubble_sort(values: list[int]) -> None:
    for end_i in range(len(values) - 1, 0, -1):
        for start_i in range(0, len(values)-1, 1):
            if values[start_i] > values[start_i+1]:
                values[start_i], values[start_i+1] = (values[start_i + 1], values[start_i])
                
