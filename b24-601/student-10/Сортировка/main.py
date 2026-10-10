"""Содержит примеры для занятия о сортировке и поиске."""

# System imports
import random
import time
from collections.abc import Callable
from unittest import result


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


def bubble_sort(values: list[int]) -> None:
    """Сортирует список по возрастанию методом пузырька.

    Args:
        values: Изменяемый исходный список.
    """
    for end_index in range(len(values) - 1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )

def measure_execution_time(
    function: Callable[..., object],
    *args: object,
) -> tuple[object, float]:
    """Вызывает функцию и измеряет время выполнения.

    Args:
        function: Вызываемая функция.
        *args: Её позиционные аргументы.

    Returns:
        Результат функции и время выполнения в секундах.
    """
    start_time = time.time()
    result = function(*args)
    stop_time = time.time()

    return result, stop_time - start_time

def main() -> None:
    count, minimum_value, maximum_value = read_generation_parameters()
    values = generate_values(count, minimum_value, maximum_value)

    print("\n Исходный список:",values)
    measure_execution_time(bubble_sort, values)
    # bubble_sort(values)

    print("\n Отсортированный список:",values)
    print("\n Время:", result)
if __name__ == "__main__":
    main()