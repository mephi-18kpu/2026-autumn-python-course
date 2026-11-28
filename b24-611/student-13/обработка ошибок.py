# System imports
#import numpy as np
#import matplotlib.pyplot as plt
#from pathlib import Path
# External imports

# User imports

#############################################

#прашивает колличество, считывает значения. количество элементов целое, не ругается на строки и тд
#преобразование к флоат и поделить пополам, если происходит ошибка выбрасываем исключение valueerror и завершаем
#try  на вызов всех функций


def create_list(values: list) -> None:
    n = int(input("Веедите колличество элементов: "))
    for i in range(n):
        values.append(input(f"Введите элемент {i + 1}: "))


def change_values(values: list) -> None:
    for i in range(len(values)):
        values[i] = float(values[i]) / 2


values = []

try:
    create_list(values)
    change_values(values)
    print(values)
except ValueError as error:
    print(f"Введите целое число ({error})")
except TypeError:
    print("Не тот тип данных")
