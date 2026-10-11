""" Содержит алгоритмы сортировки."""
# System imports

# External imports

# User imports

#############################################


def bubble_sort(values: list[int]) -> None:
    """Сортирует список по возрастанию методом пузырька."""

    for end_index in range(len(values)-1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]


def shaker_sort(values: list[int]) -> None:
    """Реализует шейкерную сортировку."""

    left_limit = 0
    right_limit = len(values) - 1
    move_flag = True

    while move_flag:
        move_flag = False

        for index in range(left_limit, right_limit):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                move_flag = True
        right_limit -= 1

        if not move_flag:
            break

        for index in range(right_limit, left_limit, -1):
            if values[index] < values[index - 1]:
                values[index], values[index - 1] = values[index - 1], values[index]
                move_flag = True
        left_limit += 1


def gnome_sort(values: list[int]) -> None:
    """Реализует гномью сортировку."""

    end_index = len(values)
    index = 0
    return_pos = 0

    while index < end_index:
        if index == 0 or values[index] > values[index - 1]:
            if return_pos > 0:
                index = return_pos
                return_pos = 0
            else:
                index += 1
        else:
            if return_pos == 0:
                return_pos = index + 1
            values[index], values[index - 1] = values[index - 1], values[index]
            index -= 1


def stupid_sort(values: list[int]) -> None:
    """Реализует глупую сортировку."""

    index = 0
    last_index = len(values) - 1

    while index < last_index:
        if values[index] > values[index + 1]:
            values[index], values[index + 1] = values[index + 1], values[index]
            index = 0
        else:
            index += 1


def odd_even_sort(values: list[int]) -> None:
    """Реализует четно-нечетную сортировку."""

    index = 0
    last_index = len(values) - 1
    move_flag = True

    while move_flag:

        move_flag = False

        for index in range(0, last_index, 2):  # Четный проход.
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                move_flag = True

        for index in range(1, last_index, 2):  # Нечетный проход.
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                move_flag = True


def comb_sort(values: list[int]) -> None:
    """Реализует сортировку расческой."""

    length = len(values)
    gap = length
    sorted_flag = True

    while sorted_flag:

        gap = int(gap // 1.25)

        if gap < 1:
            gap = 1
            sorted_flag = False

        sorted_flag = False

        for index in range(length - gap):
            if values[index] > values[index + gap]:
                values[index], values[index + gap] = values[index + gap], values[index]
                sorted_flag = True


def insertion_sort(values: list[int]) -> None:
    """Реализует сортировку вставками."""

    for index in range(1, len(values)):

        key = values[index]
        current_index = index - 1

        while key < values[current_index] and current_index >= 0:
            values[current_index + 1] = values[current_index]
            current_index -= 1

        values[current_index + 1] = key


def shells_sort(values: list[int]) -> None:
    """Реализует сортировку Шелла."""

    length = len(values)
    gaps = []
    gap = 1

    while gap < length:
        gaps.append(gap)
        gap = int(gap * 2.25) + 1

    for gap in reversed(gaps):
        for index in range(gap, length):
            key = values[index]
            current_index = index

            while key < values[current_index - gap] and current_index >= gap:
                values[current_index] = values[current_index - gap]
                current_index -= gap

            values[current_index] = key

