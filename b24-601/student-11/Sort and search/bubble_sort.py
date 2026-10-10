def bubble_sort(sorting_list: list[int]) -> list[int]:
    for i in range(0, len(sorting_list)):
        for j in range(0, len(sorting_list) - i - 1):
            if sorting_list[j+1] < sorting_list[j]:
                sorting_list[j+1], sorting_list[j] = sorting_list[j], sorting_list[j+1]
    return sorting_list
