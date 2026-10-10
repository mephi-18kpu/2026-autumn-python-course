from generation import read_generation_parameters, generate_values
from sort import bubble_sort
import time
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
def main():
    parameters = read_generation_parameters()
    output = generate_values(parameters[0],parameters[1],parameters[2])
    print(output)
    print(measure_execution_time(bubble_sort, output))
    return 0
main()
