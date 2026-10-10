import random
import time
from function import *



try:
    count, min_val, max_val = read_generation_parametrs()
except ValueError as e:
    print(f"Ошибка ввода: {e}")
    exit()
values = generate_values(count, min_val, max_val)
print("Исходный список:", values)
bubble_sort(values)
print("Отсортированный список:", values)

