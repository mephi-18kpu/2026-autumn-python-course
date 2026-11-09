def insertion_sort(values: list[int]) -> None:
    """Сортирует список простыми вставками на месте."""
    for index in range(1, len(values)):
        key = values[index]
        position = index - 1

        while position >= 0 and values[position] > key:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = key
