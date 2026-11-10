def shaker_sort(values: list[int]) -> None:
    """Сортирует список по возрастанию шейкерным методом на месте."""
    left = 0
    right = len(values) - 1

    while left < right:
        swapped = False
        for index in range(left, right):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True
        right -= 1

        if not swapped:
            break

        swapped = False
        for index in range(right, left, -1):
            if values[index - 1] > values[index]:
                values[index - 1], values[index] = values[index], values[index - 1]
                swapped = True
        left += 1

        if not swapped:
            break
