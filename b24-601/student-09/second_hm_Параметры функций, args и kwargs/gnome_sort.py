def gnome_sort(values: list[int]) -> None:
    """Сортирует список по возрастанию гномьим методом на месте."""
    index = 0

    while index < len(values):
        if index == 0 or values[index] >= values[index - 1]:
            index += 1
        else:
            values[index], values[index - 1] = values[index - 1], values[index]
            index -= 1
