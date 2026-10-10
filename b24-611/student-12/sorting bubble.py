from random import randint
import time
from collections.abc import Callable

def generate_list(amount, start, stop): # генерирует список из случайных целых чисел в диапазоне от start до stop включительно
    generated_list = [randint(start, stop) for i in range(amount)]
    return generated_list

#реализация сортировки пузырьком

def sorting_bubble(list_for_sorting):
    if len(list_for_sorting) == 1:
        return list_for_sorting
    else:
        amount_of_sorted_elements = 0
        while amount_of_sorted_elements < len(list_for_sorting):
            index = 1
            while index < len(list_for_sorting) - amount_of_sorted_elements:
                if list_for_sorting[index-1] > list_for_sorting[index]:
                    list_for_sorting[index-1], list_for_sorting[index] = list_for_sorting[index], list_for_sorting[index-1] # поменяли местами
                index += 1
            amount_of_sorted_elements += 1
        return list_for_sorting


amount, start, stop = list(map(int, input('Введите параметры для генерации списка - количество элементов и диапазон [a; b]: ').split()))
our_list = generate_list(amount, start, stop)
print(*our_list)
print(*sorting_bubble(our_list))


