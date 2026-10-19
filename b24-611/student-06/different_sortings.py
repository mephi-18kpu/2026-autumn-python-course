import random

def stupid_sort(values: list[int]) -> None:
    i = 0
    n = len(values)
    while i < n - 1:
        if values[i] > values[i + 1]:
            values[i], values[i + 1] = values[i + 1], values[i]
            i = 0
        else:
            i += 1


def odd_even_sort(values: list[int]) -> None:
    n = len(values)
    if n < 2:
        return

    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(0, n - 1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False

        for i in range(1, n - 1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False


def comb_sort(values: list[int]) -> None:
    n = len(values)
    gap = n
    shrink = 1.247
    is_sorted = False

    while not is_sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True

        for i in range(0, n - gap):
            if values[i] > values[i + gap]:
                values[i], values[i + gap] = values[i + gap], values[i]
                is_sorted = False


def insertion_sort(values: list[int]) -> None:
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key


def shell_sort(values: list[int]) -> None:
    n = len(values)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = values[i]
            j = i
            while j >= gap and values[j - gap] > key:
                values[j] = values[j - gap]
                j -= gap
            values[j] = key
        gap //= 2

if __name__ == "__main__":
    source_values = [random.randint(-50, 50) for _ in range(15)]
    expected_result = sorted(source_values)

    print(f"Исходный список для проверки: {source_values}\n")

    sorting_algorithms = {
        "Глупая сортировка": stupid_sort,
        "Чётно-нечётная сортировка": odd_even_sort,
        "Сортировка расчёской": comb_sort,
        "Сортировка вставками": insertion_sort,
        "Сортировка Шелла": shell_sort
    }

    for name, sort_func in sorting_algorithms.items():
        test_copy = source_values.copy()

        result_none = sort_func(test_copy)

        is_correct = (test_copy == expected_result) and (result_none is None)

        status = "Ура, победа" if is_correct else "Увы..."
        print(f"{name:27}: {test_copy} -> {status}")

        # Гарантируем корректность через assert
        assert test_copy == expected_result, f"Алгоритм '{name}' отсортировал неправильно"
        assert result_none is None, f"Алгоритм '{name}' не вернул None"

    print("\nВсе алгоритмы успешновые")
