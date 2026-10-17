def bubble_sort(sorting_list: list[int]) -> list[int]:
    for i in range(0, len(sorting_list)):
        for j in range(0, len(sorting_list) - i - 1):
            if sorting_list[j+1] < sorting_list[j]:
                sorting_list[j+1], sorting_list[j] = sorting_list[j], sorting_list[j+1]

    return sorting_list

def gnome_sort(sorting_list: list[int]) -> list[int]:
    i = 1
    while i < len(sorting_list):
        if i == 0 or sorting_list[i] >= sorting_list[i - 1]:
            i += 1
        else:
            sorting_list[i], sorting_list[i - 1] = sorting_list[i - 1], sorting_list[i]
            i -= 1

    return sorting_list

def cocktail_sort(sorting_list: list[int]) -> list[int]:
    for i in range(len(sorting_list)):
        flag = False

        for j in range(i, len(sorting_list) - 1 - i):
            if sorting_list[j] > sorting_list[j + 1]:
                sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]
                flag = True

        for j in range(len(sorting_list) - 2 - i, i, -1):
            if sorting_list[j] < sorting_list[j - 1]:
                sorting_list[j], sorting_list[j - 1] = sorting_list[j - 1], sorting_list[j]
                flag = True
        if not flag:
            break

    return sorting_list

def stupid_sort(sorting_list: list[int]) -> list[int]:
    i = 0
    while i < len(sorting_list) - 1:
        if sorting_list[i] > sorting_list[i + 1]:
            sorting_list[i + 1], sorting_list[i] = sorting_list[i], sorting_list[i + 1]
            i = 0
        else:
            i += 1

    return sorting_list

def odd_even_sort(sorting_list: list[int]) -> list[int]:
    for i in range(len(sorting_list)):
        flag = False
        for j in range(i%2, len(sorting_list) - 1, 2):
            if sorting_list[j] > sorting_list[j+1]:
                sorting_list[j], sorting_list[j+1] = sorting_list[j+1], sorting_list[j]
                flag = True
        if not flag:
            break

    return sorting_list

def comb_sort(sorting_list: list[int]) -> list[int]:
    n = len(sorting_list)
    gap = n
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        gap = max(1, int(gap / shrink))
        is_sorted = gap == 1  # may stay True only if this gap-1 pass makes no swaps

        for j in range(n - gap):
            if sorting_list[j] > sorting_list[j + gap]:
                sorting_list[j], sorting_list[j + gap] = sorting_list[j + gap], sorting_list[j]
                is_sorted = False

    return sorting_list

def insertion_sort(sorting_list: list[int]) -> list[int]:
    for i in range(1, len(sorting_list)):
        vsp = sorting_list[i]
        for j in range(i - 1, -1, -1):
            if sorting_list[j] > vsp:
                sorting_list[j + 1], sorting_list[j] = sorting_list[j], vsp
            else:
                sorting_list[j + 1] = vsp
                break

    return sorting_list

def shell_sort(sorting_list: list[int]) -> list[int]:
    n = len(sorting_list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            current = sorting_list[i]
            j = i

            while j >= gap and sorting_list[j - gap] > current:
                sorting_list[j] = sorting_list[j - gap]
                j -= gap

            sorting_list[j] = current

        gap //= 2

    return sorting_list
