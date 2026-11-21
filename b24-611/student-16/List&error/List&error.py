import math
from typing import List

import matplotlib.pyplot as plt
import numpy as np

def create_list(values: list) -> None:
    n = int(input("Введите кол-во элементов: "))
    for i in range(n):
        values.append(input(f"Введите элемент {i+1}: "))


def change_values(values: list) -> None:
    for i in range(len(values)):
        values[i] = float(values[i])/2


values = []

try:
    create_list(values)
    change_values(values)
    print(values)
except ValueError as er:
    print(f"Введите целое число ({er})")
except TypeError:
    print("Не тот тип данных, возможно, строка")
