def stupid_sort(values: list[int]) -> None:
    index = 0
    while index < len(values) - 1:
        if values[index] > values[index + 1]:
            values[index], values[index + 1] = (
                values[index + 1],
                values[index],
            )
            index = 0
        else:
            index += 1


def odd_even_sort(values: list[int]) -> None:
    n = len(values)
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(1, n - 1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False

        for i in range(0, n - 1, 2):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False


def comb_sort(values: list[int], shrink: float = 1.3) -> None:
    n = len(values)
    gap = n
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False

        for i in range(n - gap):
            if values[i] > values[i + gap]:
                values[i], values[i + gap] = values[i + gap], values[i]
                swapped = True


def insertion_sort(values: list[int]) -> None:
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key


def shell_sort(values: list[int]) -> None:
    n = len(values)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = values[i]
            j = i
            while j >= gap and values[j - gap] > temp:
                values[j] = values[j - gap]
                j -= gap
            values[j] = temp
        gap //= 2
