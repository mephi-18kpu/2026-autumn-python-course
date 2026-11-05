import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand

def integrate_trapezoid(uzly: NDArray[np.float64], funktsiya: Integrand) -> float:
    if len(uzly) < 2:
        raise ValueError("Нужно минимум два узла")
    shag = uzly[1] - uzly[0]
    summa = (funktsiya(uzly[0]) + funktsiya(uzly[-1])) / 2.0
    for i in range(1, len(uzly) - 1):
        summa = summa + funktsiya(uzly[i]) # здесь формально мы должны разделить на 2.
        # Но ведь если подумать:
        # мы используем значение функции в этой конкретной точке. На следующем шаге мы опять
        # возьмём это же значение, только уже рассматривая следующую трапецию. Таким образом
        # в окончательной сумме каждая из точек
        # (кроме крайней правой и крайней левой) учтётся дважды
        # просто каждый раз значение будет делиться пополам. И тогда можно сразу взять значение
        # не деля его пополам
    return shag * summa
