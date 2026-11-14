from numpy.typing import NDArray
import numpy as np
from .type_aliases import Integrand

#Разбиваем площадь под графиком на прямоугольники с шириной shag

def integrate_left_rectangles(uzly: NDArray[np.float64], f: Integrand) -> float:
    if len(uzly) < 2:         # Проверка существования ширины
        return 0.0

    shag = uzly[1] - uzly[0] #Узнаем ширину прямоугольника
    sum_plosh = 0.0

    for i in range(len(uzly) - 1):  #Левые прямоугольники поэтому -1 мы учитываем левый край
        sum_plosh += f(uzly[i])     #Суммируем значения функций в точках

    return sum_plosh * shag  #Формула площади


def integrate_right_rectangles(uzly: NDArray[np.float64], f: Integrand) -> float:
    if len(uzly) < 2:
        return 0.0

    shag = uzly[1] - uzly[0]
    sum_plosh = 0.0

    for i in range(1, len(uzly)):   #Уже правые прямоугольники поэтому не учитываем самый левый край
        sum_plosh += f(uzly[i])

    return sum_plosh * shag


def integrate_midpoint_rectangles(uzly: NDArray[np.float64], f: Integrand) -> float:
    if len(uzly) < 2:
        return 0.0

    shag = uzly[1] - uzly[0]
    sum_plosh = 0.0

    for i in range(len(uzly) - 1):
        mid_x = (uzly[i] + uzly[i + 1]) / 2.0 #Ищем среднее значение между левым и правым краем столбика
        sum_plosh += f(mid_x)

    return sum_plosh * shag
