from typing import Callable
import numpy as np

from numpy.typing import NDArray #тип данных для массива

Integrand = Callable[[float], float]
Integration_Method = Callable[[NDArray[np.float64], Integrand], float] #берем массив точек? и функция которую будем интегрировать
