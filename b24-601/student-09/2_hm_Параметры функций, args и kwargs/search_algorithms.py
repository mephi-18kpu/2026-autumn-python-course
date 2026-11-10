def linear_search(values: list[int], target: int) -> int | None:
    """Возвращает индекс найденного элемента или None."""
    for index, value in enumerate(values):
        if value == target:
            return index

    return None


def binary_search(values: list[int], target: int) -> int | None:
    """Ищет элемент бинарным поиском в списке, отсортированном по возрастанию."""
    left_index = 0
    right_index = len(values) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = values[middle_index]

        if middle_value == target:
            return middle_index
        if middle_value < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return None
