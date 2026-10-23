
def stupid_sort(arr: list[int]) -> None:
    """Глупая сортировка: после обмена возвращаемся к началу."""
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i = 0
        else:
            i += 1


def odd_even_sort(arr: list[int]) -> None:
    """Чётно-нечётная сортировка."""
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False

        # Сначала пары с чётным левым индексом.
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Затем пары с нечётным левым индексом.
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


def comb_sort(arr: list[int]) -> None:
    """Сортировка расчёской с коэффициентом 1.247."""
    n = len(arr)
    gap = n
    shrink = 1.247
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True


def insertion_sort(arr: list[int]) -> None:
    """Сортировка вставками."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def shell_sort(arr: list[int]) -> None:
    """Сортировка Шелла с последовательностью шагов n//2, ... , 1."""
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = key

        gap //= 2


# Проверка всех алгоритмов на копиях одного списка.
source_values = [8, 3, 7, 1, 9, 2, 5, 3]
expected = sorted(source_values)

sort_functions = [
    stupid_sort,
    odd_even_sort,
    comb_sort,
    insertion_sort,
    shell_sort,
]

for sort_function in sort_functions:
    values = source_values.copy()
    result = sort_function(values)

    assert values == expected, (
        f"{sort_function.__name__}: "
        f"ожидалось {expected}, получено {values}"
    )
    assert result is None, (
        f"{sort_function.__name__} должна возвращать None"
    )

    print(f"{sort_function.__name__}: {values}")

print("Все проверки пройдены!")
