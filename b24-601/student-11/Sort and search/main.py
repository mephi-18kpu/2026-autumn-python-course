# System imports
import random
import time
from collections.abc import Callable

# External imports

# User imports
import generation
import bubble_sort as bs

#############################################


def measure_execution(
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


def main() ->None:
    numbers = generation.generate_values(20,0, 100)
    sorted_numbers, execution_time = measure_execution(bs.bubble_sort, numbers.copy())

    print(f"Неотсортированный список: {numbers}\n"
          f"Отсортированный список: {sorted_numbers}\n"
          f"Время выполнения: {execution_time}")



main()
