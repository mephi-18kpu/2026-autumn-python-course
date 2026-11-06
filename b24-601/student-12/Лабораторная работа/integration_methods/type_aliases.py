"""Псевдонимы типов для функций численного интегрирования."""
from typing import Callable
import numpy as np
from numpy.typing import NDArray

# Тип подынтегральной функции (принимает float, возвращает float)
Integrand = Callable[[float], float]

# Тип метода интегрирования (принимает массив узлов и функцию, возвращает float)
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]