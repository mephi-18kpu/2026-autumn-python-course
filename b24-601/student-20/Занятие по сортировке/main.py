"""Содержит примеры для занятия о сортировке и поиске."""
# System imports

# External imports

# User imports
from generate import read_generation_parameters
from generate import generate_values
from generate import measure_execution_time
from generate import generate_number
from sort import bubble_sort
from sort import shaker_sort
from sort import gnome_sort
from sort import stupid_sort
from sort import odd_even_sort
from sort import comb_sort
from sort import shells_sort
from sort import insertion_sort
from data import TRIAL_COUNT
from data import COUNT
from data import MINIMUM_VALUE
from data import MAXIMUM_VALUE
from search import linear_search
from search import binary_search
#############################################


def main() -> None:
    print()
    print("Ручная работа с массивами и поиск значений в них")

    parameters = read_generation_parameters()
    generated_list = generate_values(parameters[0], parameters[1], parameters[2])

    print("Выберите способ сортировки: \n"
          "Метод пузырька - 1\n"
          "Шейкерная сортировка - 2\n"
          "Гномья сортировка - 3\n"
          "Глупая сортировка - 4\n"
          "Четно-нечетная сортировка - 5\n"
          "Сортировка расческой - 6\n"
          "Сортировка вставками - 7\n"
          "Сортировка Шелла - 8\n")

    match int(input()):
        case "1":
            bubble_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")
        case "2":
            shaker_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")
        case "3":
            gnome_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")
        case "4":
            stupid_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")
        case "5":
            odd_even_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")
        case "6":
            comb_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")
        case "7":
            insertion_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")
        case "8":
            shells_sort(generated_list)
            _, time_parameters = measure_execution_time(bubble_sort, generated_list)
            print(f"Результат:{time_parameters}")

    print(generated_list)

    print("Выберите способ поиска:\n"
          "Линейный поиск - 1\n"
          "Бинарный поиск - 2\n")

    match int(input()):
        case "1":
            index = linear_search(generated_list, int(input()))
            _, time_parameters = measure_execution_time(linear_search, generated_list)
            print(f"Результат:{time_parameters}")
            print(f"Индекс заданного числа: {index}")
        case "2":
            index = binary_search(generated_list, int(input()))
            _, time_parameters = measure_execution_time(binary_search, generated_list)
            print(f"Результат:{time_parameters}")
            print(f"Индекс заданного числа: {index}")


def test() -> None:
    sort_functions = [
        ("Пузырьковая", bubble_sort),
        ("Шейкерная", shaker_sort),
        ("Гномья", gnome_sort),
        ("Глупая", stupid_sort),
        ("Четно-нечетная", odd_even_sort),
        ("Расческой", comb_sort),
        ("Шелла", shells_sort),
        ("Простыми вставками", insertion_sort),
    ]

    for trial_number in range(1, TRIAL_COUNT + 1):
        source_values = generate_values(COUNT, MINIMUM_VALUE, MAXIMUM_VALUE)
        expected_values = sorted(source_values)

        for sort_name, sort_function in sort_functions:
            values_to_sort = source_values.copy()
            _, elapsed_time = measure_execution_time(sort_function, values_to_sort)

            print(f"Повтор {trial_number}, {sort_name}: {elapsed_time:.5f} с")
            print(f"Результат верный: {values_to_sort == expected_values}")

    find_functions = [
        ("Линейная", linear_search),
        ("Бинарная", binary_search),
    ]

    for trial_number in range(1, TRIAL_COUNT + 1):
        source_values = generate_values(COUNT, MINIMUM_VALUE, MAXIMUM_VALUE)
        values = sorted(source_values)
        index = generate_number(COUNT)
        target_value = values[index]

        for find_name, find_function in find_functions:
            result, elapsed_time = measure_execution_time(find_function, values, target_value)
            print(f"Повтор {trial_number}, {find_name}: {elapsed_time:.8f} с")
            print(f"Результат верный: {values[int(result)] == target_value}")


if __name__ == "__main__":
    test()
    main()
