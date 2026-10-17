def bin_search(searching_list: list[int], target: int) -> int | None:
    right_index = len(searching_list) - 1
    left_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if searching_list[mid_index] == target:
            return mid_index

        if searching_list[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return None
