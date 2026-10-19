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
