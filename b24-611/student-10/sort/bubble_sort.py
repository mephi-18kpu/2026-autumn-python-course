def bubble_sort(values: list[int]) -> None:

    for end_i in range(len(values) - 1, 0, 1):
        for i in range(end_i):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = (

                    values[i + 1],
                    values[i],

                )
