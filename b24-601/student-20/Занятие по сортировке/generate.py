""" Содержит функции для создания списка со случайными значениями."""
# System imports
import random
import time
from collections.abc import Callable

# External imports

# User imports

#############################################


def read_generation_parameters() -> tuple[int, int, int]:
    """Считывает количество элементов и границы диапазона.

    Returns:
        Количество элементов, нижнюю и верхнюю границы.

    Raises:
        ValueError: Введены неверные границы.
    """
    count = int(input("Количество элементов: "))
    minimum_value = int(input("Минимальное значение: "))
    maximum_value = int(input("Максимальное значение: "))

    if count < 0:
        raise ValueError("Количество элементов не может быть отрицательным.")

    if minimum_value > maximum_value:
        raise ValueError("Минимальное значение больше максимального.")

    return count, minimum_value, maximum_value


def generate_values(
    count: int,
    minimum_value: int,
    maximum_value: int,
) -> list[int]:
    """ Создает список случайных целых чисел.
    Args:
        count: Количество элементов.
        minimum_value: Нижняя граница.
        maximum_value: Верхняя граница.

    Returns:
        Список случайных чисел.

    Raises:
        ValueError: Количество или границы заданы неверно.
    """

    if count < 0:
        raise ValueError("Количество элементов не может быть отрицательным.")

    if minimum_value > maximum_value:
        raise ValueError("Минимальное значение больше максимального.")

    return [
        random.randint(minimum_value, maximum_value)
        for _ in range(count)
    ]


def measure_execution_time(
    function: Callable[..., object],
    *args: object,
) -> tuple[object, float]:
    """Вызывает функцию и измеряет время выполнения

    Args:
        function: Вызываемая функция.
        *args: Ее позиционные аргументы.

    Returns:
        Результат функции и время выполнения в секундах.
    """

    start_time = time.time()
    result = function(*args)
    stop_time = time.time()

    return result, stop_time - start_time


def generate_number(
    count: int,
) -> int:
    """ Создает случайный индекс списка.

    Args:
        count: Длина списка.

    Returns:
        Случайное число меньше длины списка
    """

    return random.randint(0, count)
