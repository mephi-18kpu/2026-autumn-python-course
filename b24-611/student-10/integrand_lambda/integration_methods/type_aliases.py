from typing import Callable
import numpy as np

# подынтегральная функция: одно число -> одно число
Integrand = Callable[[float], float]

# массив узлов сетки
Nodes = np.ndarray
