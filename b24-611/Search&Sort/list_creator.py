#System imports
import random
import time
from collections.abc import Callable
#External imports

#User imports

##########################
def read_generation_parameters() -> tuple[int, int, int]:
    #Почему кортеж?
    count = int(input('Количество элементов: '))
    minimum_value = int(input('Минимальное значение: '))
    maximum_value = int(input('Максимальное значение: '))

    if count < 0:
        raise ValueError('Количество элементов должно быть неотрицательным')

    if minimum_value>maximum_value:
        raise ValueError('Минимальное значение должно быть меньше максимального')

    return count, minimum_value, maximum_value

def generate_values(
    count: int,
    minimum_value: int,
    maximum_value: int,
) -> list[int]:
    if count < 0:
        raise ValueError('Количество элементов должно быть неотрицательным')

    if minimum_value > maximum_value:
        raise ValueError('Минимальное значение должно быть меньше максимального')

    return[
        random.randint(minimum_value, maximum_value)
        for i in range(count)
    ]
