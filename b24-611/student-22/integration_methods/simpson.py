"""Модуль реализации метода Симпсона."""

# System imports

# External imports
import numpy as np
from numpy.typing import NDArray

# User imports
from .type_aliases import Integrand

#############################################


def integrate_simpson(
    nodes: NDArray[np.float64],
    function: Integrand,
) -> float:
    """Вычисление интеграла методом Симпсона (парабол).

    S_h = (h / 3) * (f_0 + 4 * sum_{j=1}^{n/2} f_{2j-1} + 2 * sum_{j=1}^{n/2-1} f_{2j} + f_n)
    Число узлов N должно быть нечётным (N >= 3), число интервалов n = N - 1 чётным.
    """
    N = len(nodes)
    if N < 3 or N % 2 == 0:
        raise ValueError("Число узлов должно быть нечётным и не менее 3.")

    h = (nodes[-1] - nodes[0]) / (N - 1)

    f_0 = function(float(nodes[0]))
    f_n = function(float(nodes[-1]))

    odd_sum = sum(function(float(nodes[i])) for i in range(1, N - 1, 2))
    even_sum = sum(function(float(nodes[i])) for i in range(2, N - 1, 2))

    return float((h / 3.0) * (f_0 + 4.0 * odd_sum + 2.0 * even_sum + f_n))
