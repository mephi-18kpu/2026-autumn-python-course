import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

# funktsiya: Integrand) - мы указали тип функции которую будем интегрировать и для которой
# применим метод интегрирования
def integrate_left_rectangles(uzly: NDArray[np.float64], funktsiya: Integrand) -> float:
    if len(uzly) < 2:
        raise ValueError("Нужно минимум два узла")
    shag = uzly[1] - uzly[0]
    summa = 0.0 # сумма интгерирования (площадь под кривой)
    for i in range(len(uzly) - 1):  # здесь не войдёт крайняя правая граница, но нам это и не нужно -
        # ведь это метод левых прямоугольников
        summa = summa + funktsiya(uzly[i])
    return shag * summa # поскольку шаг не изменяется, можно просто сразу в конце домножить
                                                    # всю сумму на шаг


def integrate_right_rectangles(uzly: NDArray[np.float64], funktsiya: Integrand) -> float:
    if len(uzly) < 2:
        raise ValueError("Нужно минимум два узла")
    shag = uzly[1] - uzly[0]
    summa = 0.0
    for i in range(1, len(uzly)): # а здесь наоборот не войдёт крайняя левая граница -
        # ведь это метод правых прямоугольников
        summa = summa + funktsiya(uzly[i])
    return shag * summa


def integrate_midpoint_rectangles(uzly: NDArray[np.float64], funktsiya: Integrand) -> float:
    if len(uzly) < 2:
        raise ValueError("Нужно минимум два узла")
    shag = uzly[1] - uzly[0]
    summa = 0.0
    for i in range(len(uzly) - 1):
        seredina = (uzly[i] + uzly[i + 1]) / 2.0 # берёт середину отрезка и уже в ней
        # вычисляет значение функции
        summa = summa + funktsiya(seredina)
    return shag * summa
