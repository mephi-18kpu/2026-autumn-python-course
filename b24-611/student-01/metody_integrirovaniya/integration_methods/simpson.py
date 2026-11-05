import numpy as np
from numpy.typing import NDArray
from .type_aliases import Integrand


def integrate_simpson(uzly: NDArray[np.float64], funktsiya: Integrand) -> float:
    if len(uzly) < 3 or len(uzly) % 2 == 0:
        raise ValueError("Нужно нечётное число узлов, не меньше трёх")

    shag = uzly[1] - uzly[0]
    summa_1 = 0.0
    summa_2 = 0.0

    for i in range(1, len(uzly) - 1, 2): # здесь мы будем брать только нечётные значения
        # (причём не берём первую точку и последнуюю точку)
        summa_1 = summa_1 + funktsiya(uzly[i])

    for i in range(2, len(uzly) - 1, 2): # Здесь же будем брать только чётные значения (опять же
        # не включая первую и последнюю точки)
        summa_2 = summa_2 + funktsiya(uzly[i])

    rezultat = funktsiya(uzly[0]) + 4.0 * summa_1 + 2.0 * summa_2 + funktsiya(uzly[-1]) # формула из лекции
    # которая окончательно приводит к результату по методу Симпсона
    return (shag / 3.0) * rezultat
