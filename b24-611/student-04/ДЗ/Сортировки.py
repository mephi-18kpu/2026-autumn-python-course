def shaker_sort(values: list[int]) -> None:
    """Сортирует список по возрастанию шейкерной сортировкой.

    Args:
        values: Изменяемый исходный список.
    """
    left = 0
    right = len(values) - 1

    while left < right:
        swapped = False

        # Проход слева направо: максимум уезжает в позицию right.
        for index in range(left, right):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )
                swapped = True

        right -= 1

        # Проход справа налево: минимум уезжает в позицию left.
        for index in range(right, left, -1):
            if values[index - 1] > values[index]:
                values[index - 1], values[index] = (
                    values[index],
                    values[index - 1],
                )
                swapped = True

        left += 1

        # Если за целую пару проходов не было обменов — готово.
        if not swapped:
            break

def gnome_sort(values: list[int]) -> None:
    """Сортирует список по возрастанию гномьей сортировкой.

    Args:
        values: Изменяемый исходный список.
    """
    index = 0
    length = len(values)

    while index < length:
        if index == 0 or values[index - 1] <= values[index]:
            index += 1
        else:
            values[index - 1], values[index] = (
                values[index],
                values[index - 1],
            )
            index -= 1


def check_sort(sort_function, source_values: list[int]) -> None:
    """Проверяет, что сортировка совпадает с sorted()"""
    expected = sorted(source_values)
    values = source_values.copy()

    result = sort_function(values)


test_cases = [
    [],
    [7],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [-3, 0, -10, 5, -1],
    [2, 2, 1, 1, 3, 3, 2],
    [5, 1, 4, 2, 8],
]

for sort_function in (shaker_sort, gnome_sort):
    for case in test_cases:
        check_sort(sort_function, case)
    print(f"{sort_function.__name__}: все проверки пройдены")

