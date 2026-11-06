from unittest.mock import right


def shaker_sort(values: list[int]) -> None:
    left_index = 0
    right_index = len(values) - 1

    while left_index < right_index:
        flag = False
        for current in range(left_index, right_index):
            if values[current] > values[current + 1]:
                values[current], values[current + 1] = values[current + 1], values[current]
                flag = True
        right_index -= 1
        if not flag: break

        flag = False
        for current in range(right_index, left_index, -1):
            if values[current - 1] > values[current]:
                values[current -1], values[current] = values[current], values[current - 1]
                flag = True
        left_index += 1
        if not flag: broke
