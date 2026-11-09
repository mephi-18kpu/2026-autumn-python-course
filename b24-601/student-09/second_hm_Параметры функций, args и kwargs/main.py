import random
from time import perf_counter

from shaker_sort import shaker_sort
from gnome_sort import gnome_sort
from stupid_sort import stupid_sort
from odd_even_sort import odd_even_sort
from comb_sort import comb_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from search_algorithms import linear_search, binary_search


def read_generation_parameters() -> tuple[int, int, int]:
    """Считывает количество элементов и границы диапазона."""
    count = int(input("Количество элементов: "))
    minimum_value = int(input("Минимальное значение: "))
    maximum_value = int(input("Максимальное значение: "))

    if count < 0:
        raise ValueError("Количество элементов не может быть отрицательным.")
    if minimum_value > maximum_value:
        raise ValueError("Минимальное значение больше максимального.")

    return count, minimum_value, maximum_value


def generate_values(count: int, minimum_value: int, maximum_value: int) -> list[int]:
    """Создаёт список случайных целых чисел."""
    if count < 0:
        raise ValueError("Количество элементов не может быть отрицательным.")
    if minimum_value > maximum_value:
        raise ValueError("Минимальное значение больше максимального.")

    return [
        random.randint(minimum_value, maximum_value)
        for _ in range(count)
    ]


def main() -> None:
    count, minimum_value, maximum_value = read_generation_parameters()
    source_values = generate_values(count, minimum_value, maximum_value)
    expected_values = sorted(source_values)

    print("\nИсходный список:")
    print(source_values)
    print("\nРезультаты сортировок:")

    sort_functions = [
        ("Шейкерная", shaker_sort),
        ("Гномья", gnome_sort),
        ("Глупая", stupid_sort),
        ("Чётно-нечётная", odd_even_sort),
        ("Расчёской", comb_sort),
        ("Вставками", insertion_sort),
        ("Шелла", shell_sort),
    ]

    if count > 100:
        print(
            "Предупреждение: глупая сортировка очень медленная. "
            "Для большого списка её проверка может занять много времени."
        )

    for sort_name, sort_function in sort_functions:
        values_to_sort = source_values.copy()

        start_time = perf_counter()
        sort_function(values_to_sort)
        elapsed_time = perf_counter() - start_time

        is_correct = values_to_sort == expected_values
        print(f"{sort_name}: {values_to_sort}")
        print(f"  Результат верный: {is_correct}")
        print(f"  Время выполнения: {elapsed_time:.6f} с")

    target = int(input("\nВведите целое число для поиска: "))

    linear_result = linear_search(source_values, target)
    sorted_values = source_values.copy()
    sorted_values.sort()
    binary_result = binary_search(sorted_values, target)

    print("\nЛинейный поиск:")
    if linear_result is None:
        print("Элемент не найден.")
    else:
        print(f"Элемент найден. Индекс в исходном списке: {linear_result}")

    print("\nБинарный поиск:")
    if binary_result is None:
        print("Элемент не найден.")
    else:
        print(f"Элемент найден. Индекс в отсортированном списке: {binary_result}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Ошибка ввода: {error}")
