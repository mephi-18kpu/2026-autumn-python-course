def stupid_sort(values: list[int]) -> None:
    n = len(values)
    index = 0
    while index < n - 1:
        if values[index] > values[index + 1]:
            values[index], values[index + 1] = values[index + 1], values[index]
            index = 0
        else:
            index += 1