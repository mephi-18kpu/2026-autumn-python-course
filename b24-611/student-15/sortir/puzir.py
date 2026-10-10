def bubble_sort(values: list[int]) -> None:

    for end_index in range(len(values)-1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = (
                    values[index + 1],
                    values[index],
                )
