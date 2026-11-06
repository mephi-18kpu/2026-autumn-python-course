from numpy.typing import NDArray
import numpy as np
from .type_aliases import Integrand

#На каждом интервале график заменяем на отрезок прямой, тем самым получая трапеции

def integrate_trapezoid(uzly: NDArray[np.float64], f: Integrand) -> float:
    if len(uzly) < 2:            # Проверка существования ширины
        return 0.0

    shag = uzly[1] - uzly[0]     #Узнаем ширину прямоугольника

    # S=0.5(a+b)*shag тогда не крайние удвоятся, а для крайних мы их высоту должны поделить на 2

    krai_lev = f(uzly[0]) / 2.0
    krai_prav = f(uzly[-1]) / 2.0
    sum_plosh = krai_lev + krai_prav #Заранее добавили известные величины высот для крайних узлов

    for i in range(1, len(uzly) - 1):  #Добавляем к сумме высоты всех средних узлов
        sum_plosh += f(uzly[i])

    return sum_plosh * shag #Формула площади
