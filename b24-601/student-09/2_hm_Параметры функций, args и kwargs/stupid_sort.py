def stupid_sort(values: list[int]) -> None:
    """Глупая сортировка: после каждого обмена возвращается к началу."""
    index = 0

    while index < len(values) - 1:
        if values[index] > values[index + 1]:
            values[index], values[index + 1] = values[index + 1], values[index]
            index = 0
        else:
            index += 1
