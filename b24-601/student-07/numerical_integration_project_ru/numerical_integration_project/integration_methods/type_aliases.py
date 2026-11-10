"""Псевдонимы типов для методов численного интегрирования."""

from typing import Callable

import numpy as np
from numpy.typing import NDArray

# Подынтегральная функция: принимает число и возвращает число.
Integrand = Callable[[float], float]

# Метод интегрирования: принимает сетку и функцию, возвращает приближённый интеграл.
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]
