"""Псевдонимы типов для функций численного интегрирования."""

# System imports
from typing import Callable

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports

#############################################

# Определение типа для подынтегральной функции (принимает вещественное число, возвращает вещественное)
Integrand = Callable[[float], float]

# Определение типа для метода численного интегрирования
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]