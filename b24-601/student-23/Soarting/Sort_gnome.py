def gnome_sort(values: list[int]) -> None:
    index = 0
    n = len(values)

    while index < n:
        if index == 0 or values[index] >= values[index - 1]:
            index += 1
        else:
            values[index], values[index - 1] = values[index - 1], values[index]
            index -= 1