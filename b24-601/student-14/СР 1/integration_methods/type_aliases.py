"""Общие псевдонимы типов для методов численного интегрирования."""

from typing import Callable

import numpy as np
from numpy.typing import NDArray


# Подынтегральная функция: получает одно число и возвращает одно число.
Integrand = Callable[[float], float]

# Метод интегрирования: получает узлы сетки и функцию, возвращает результат.
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]
