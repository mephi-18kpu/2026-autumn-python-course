def odd_even_sort(values: list[int]) -> None:
    """Сортирует список чётно-нечётной сортировкой на месте."""
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for index in range(0, len(values) - 1, 2):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                is_sorted = False

        for index in range(1, len(values) - 1, 2):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                is_sorted = False
