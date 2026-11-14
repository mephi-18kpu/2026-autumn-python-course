from numpy.typing import NDArray
import numpy as np
from .type_aliases import Integrand

#Метод проводит параболу через каждые 3 точки, и получается что один участок метода охватывает 2 интервала сетки

def integrate_simpson(uzly: NDArray[np.float64], f: Integrand) -> float:
    if len(uzly) < 3:          # Проверка возможности задания параболы (нужно минимум 3 точки)
        return 0.0

    if len(uzly) % 2 == 0: #Метод Симпсона работает, когда отрезок разбит на четное число интервалов, а количество точек при этом всегда на 1 больше
        print("Ошибка: для метода Симпсона нужно нечётное число узлов")
        return 0.0

    shag = uzly[1] - uzly[0]      #Узнаем ширину "столбца"

    sum_plosh = f(uzly[0]) + f(uzly[-1]) #Первая и последние почки входят в формулу без коэф-ов

    for i in range(1, len(uzly) - 1):
        if i % 2 != 0:
            sum_plosh += 4.0 * f(uzly[i])  #Если индекс нечетный, то умножаем высоту на 4
        else:
            sum_plosh += 2.0 * f(uzly[i])  #Если индекс четный, то умножаем на 2

    return sum_plosh * shag / 3.0
