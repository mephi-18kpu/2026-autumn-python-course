from generations import read_generation_parameters, generate_values
from measure import measure_execution_time
from bubblesort import bubble_sort, shaker_sort, gnome_sort
from home_sorts import (
    stupid_sort,
    odd_even_sort,
    comb_sort,
    insertion_sort,
    shell_sort,
)
from search import linear_search, binary_search


TRIAL_COUNT = 3
STUPID_SORT_LIMIT = 100


def main() -> None:
    count, minimum_value, maximum_value = read_generation_parameters()

    sort_functions = [
        ("Пузырьковая", bubble_sort),
        ("Шейкерная", shaker_sort),
        ("Гномья", gnome_sort),
        ("Глупая", stupid_sort),
        ("Чётно-нечётная", odd_even_sort),
        ("Расчёской", comb_sort),
        ("Вставками", insertion_sort),
        ("Шелла", shell_sort),
    ]

    for trial_number in range(1, TRIAL_COUNT + 1):
        source_values = generate_values(count, minimum_value, maximum_value)
        expected_values = sorted(source_values)

        print(f"\n=== Повтор {trial_number} ===")
        print(f"Исходный список: {source_values}")

        for sort_name, sort_function in sort_functions:
            if sort_name == "Глупая" and count > STUPID_SORT_LIMIT:
                print(f"  {sort_name:16s}: пропущено (n = {count} слишком велико)")
                continue

            values_to_sort = source_values.copy()
            _, elapsed_time = measure_execution_time(
                sort_function, values_to_sort
            )
            is_correct = values_to_sort == expected_values
            print(
                f"  {sort_name:16s}: {elapsed_time:.6f} с, "
                f"результат верный: {is_correct}"
            )

    print("\n=== Поиск ===")
    sample = [8, 3, 8, 1]
    sorted_sample = sorted(sample)
    print(f"linear_search({sample}, 8) = {linear_search(sample, 8)}")
    print(
        f"binary_search({sorted_sample}, 8) = "
        f"{binary_search(sorted_sample, 8)}"
    )
    print(
        f"binary_search({sorted_sample}, 10) = "
        f"{binary_search(sorted_sample, 10)}"
    )


if __name__ == "__main__":
    main()
