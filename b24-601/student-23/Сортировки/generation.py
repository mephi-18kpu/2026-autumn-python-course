"""Содержит примеры для занятия о сортировке и поиске."""

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
        ValueError: Введены нецелые числа или неверные границы.
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
    """Создаёт список случайных целых чисел.

    Args:
        count: Количество элементов.
        minimum_value: Нижняя включительная граница.
        maximum_value: Верхняя включительная граница.

    Returns:
        Список случайных значений.

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
