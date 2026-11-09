def shell_sort(values: list[int]) -> None:
    """Сортирует список методом Шелла; шаг каждый раз делится на два."""
    gap = len(values) // 2

    while gap > 0:
        for index in range(gap, len(values)):
            key = values[index]
            position = index

            while position >= gap and values[position - gap] > key:
                values[position] = values[position - gap]
                position -= gap

            values[position] = key

        gap //= 2
