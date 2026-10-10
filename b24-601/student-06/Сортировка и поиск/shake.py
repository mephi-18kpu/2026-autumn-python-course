def shake_sort(list_of_numbers) -> list:
    flag = 0
    for i in range(len(list_of_numbers) - 1, 0, -1):
        for j in range(i):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j+1], list_of_numbers[j]
        for j in range(i-1, 0, -1):
            if list_of_numbers[j] < list_of_numbers[j-1]:
                list_of_numbers[j], list_of_numbers[j - 1] = list_of_numbers[j-1], list_of_numbers[j]
        for _ in range(len(list_of_numbers)-1):
            if (list_of_numbers[_+1] - list_of_numbers[_]) <= 0:
                break
            else:
                flag += 1
        if flag == len(list_of_numbers):
            break
    return list_of_numbers
