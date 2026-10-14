def bubble_sort(values: list[int]) -> None:
    for end_index in range(len(values) - 1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )


def shaker_sort(values: list[int]) -> None:
    left = 0
    right = len(values) - 1
    swapped = True

    while swapped and left < right:
        swapped = False

        for index in range(left, right):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )
                swapped = True
        right -= 1

        for index in range(right, left, -1):
            if values[index - 1] > values[index]:
                values[index - 1], values[index] = (
                    values[index],
                    values[index - 1],
                )
                swapped = True
        left += 1


def gnome_sort(values: list[int]) -> None:
    index = 0
    while index < len(values):
        if index == 0 or values[index - 1] <= values[index]:
            index += 1
        else:
            values[index - 1], values[index] = (
                values[index],
                values[index - 1],
            )
            index -= 1
