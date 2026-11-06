#Файл для "организации" пакета файлов
#Собираем все методы из разных файлов в 1 пакет

from .type_aliases import Integrand, IntegrationMethod
from .rectangles import integrate_left_rectangles, integrate_right_rectangles, integrate_midpoint_rectangles
from .trapezoid import integrate_trapezoid
from .simpson import integrate_simpson

__all__ = [
    "Integrand",
    "IntegrationMethod",
    "integrate_left_rectangles",
    "integrate_right_rectangles",
    "integrate_midpoint_rectangles",
    "integrate_trapezoid",
    "integrate_simpson"
]
