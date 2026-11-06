from typing import Callable
import numpy as np
from numpy.typing import NDArray

Integrand = Callable[[float], float] #Создаем псевдоним для подынтегральной функции
IntegrationMethod = Callable[[NDArray[np.float64], Integrand], float]
#Создаем псевдоним для метода: на вход получает массив точек и функцию, возвращает число
