def bubble_sort(values: list[int]) -> None:
    """Сортирует список по возрастанию методом пузырька.

    Args:
        values: Изменяемый исходный список.
    """
    for end_index in range(len(values) - 1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )
def shaker_sort(values: list[int]) -> None:
    left, right = 0, len(values) - 1
    swapped = True
    while swapped and left < right:
        swapped = False
        for index in range(left, right):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True
        right -= 1
        for index in range(right, left, -1):
            if values[index - 1] > values[index]:
                values[index - 1], values[index] = values[index], values[index - 1]
                swapped = True
        left += 1
def gnome_sort(values: list[int]) -> None:
    pos = 1
    while pos < len(values):
        if pos < 1: pos = 1
        if values[pos] < values[pos-1]:
            values[pos], values[pos-1] = values[pos-1], values[pos]
            pos -= 1
        else:
            pos += 1
def stupid_sort(values: list[int]) -> None:
    pos = 0
    while pos < len(values) - 1:
        pos += 1
        if values[pos] < values[pos - 1]:
            values[pos], values[pos - 1] = values[pos - 1], values[pos]
            pos = 0
def insertion_sort(values: list[int]) -> None:
    for index in range(1, len(values)):
        current = values[index]
        position = index - 1

        while position >= 0 and values[position] > current:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = current
def even_uneven_sort(values: list[int]) -> None:
    even = True
    change = True
    while change:
        change = False
        while change:
            change = False

            for index in range(0, len(values) - 1, 2):
                if values[index] > values[index + 1]:
                    values[index], values[index + 1] = values[index + 1], values[index]
                    change = True

            for index in range(1, len(values) - 1, 2):
                if values[index] > values[index + 1]:
                    values[index], values[index + 1] = values[index + 1], values[index]
                    change = True
def brush_sort(values: list[int]) -> None:
    step_parameter = len(values)-1
    while step_parameter > 0:
        for index in range(0, len(values) - step_parameter):
            if values[index] > values[index + step_parameter]:
                values[index], values[index + step_parameter] = values[index + step_parameter], values[index]
        step_parameter = int(step_parameter/1.247)
def shell_sort(values: list[int]) -> None:
    step = len(values) - 1

    while step > 0:
        for start in range(step):
            subsequence = values[start::step]
            insertion_sort(subsequence)
            values[start::step] = subsequence

        step = int(step / 1.247)
