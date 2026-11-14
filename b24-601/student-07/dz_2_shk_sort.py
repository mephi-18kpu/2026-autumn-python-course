def shaker_sort(values: list[int]) -> None:
    left = 0
    right = len(values) - 1

    while left < right:
        swapped = False

        # Проход слева направо: перемещаем максимум вправо
        for i in range(left, right):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True

        if not swapped:
            return

        right -= 1
        swapped = False

        # Проход справа налево: перемещаем минимум влево
        for i in range(right, left, -1):
            if values[i - 1] > values[i]:
                values[i - 1], values[i] = values[i], values[i - 1]
                swapped = True

        if not swapped:
            return

        left += 1
def gnome_sort(values: list[int]) -> None:
    i = 1

    while i < len(values):
        if i == 0 or values[i] >= values[i - 1]:
            i += 1
        else:
            values[i], values[i - 1] = values[i - 1], values[i]
            i -= 1

def test_sort(sort_func):
    test_cases = [
        [],
        [5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [-3, -1, -7, 0, 2],
        [3, 1, 3, 2, 1, 2],
    ]

    for case in test_cases:
        values = case.copy()
        expected = sorted(case)

        result = sort_func(values)

        assert values == expected, (
            f"{sort_func.__name__}: "
            f"вход {case}, ожидалось {expected}, получено {values}"
        )
        assert result is None, "Функция должна возвращать None"

    print(f"{sort_func.__name__}: все тесты пройдены!")


test_sort(shaker_sort)
test_sort(gnome_sort)
