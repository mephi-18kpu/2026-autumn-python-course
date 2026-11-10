def comb_sort(values: list[int]) -> None:
    """Сортирует список расчёской с коэффициентом уменьшения шага 1.3."""
    gap = len(values)
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        swapped = False

        for index in range(len(values) - gap):
            if values[index] > values[index + gap]:
                values[index], values[index + gap] = values[index + gap], values[index]
                swapped = True
