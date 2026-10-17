#System imports

# External imports

# User imports

#############################################

def bubble_sort(values: list[int]) -> None:
    for end_index in range(len(values) - 1, 0, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]


def shaker_sort(values: list[int]) -> None:
    start_index = 0
    for end_index in range(len(values) - 1, start_index, -1):
        for index in range(end_index):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]

        for index in range(end_index, start_index + 1, -1):
            if values[index] < values[index - 1]:
                values[index], values[index - 1] = values[index - 1], values[index]
        start_index += 1

def gnome_sort(values: list[int]) -> None:
    flag = False
    end_index = len(values) - 1
    index = 0
    while flag == False:
        if index == end_index:
            flag = True
        elif values[index] <= values[index + 1]:
            index += 1
            print(index)
            print(values)
        elif values[index] > values[index + 1]:
            values[index], values[index + 1] = values[index + 1], values[index]
            index -= 1
            print(index)
            print(values)
        if index < 0:
            index = 1


