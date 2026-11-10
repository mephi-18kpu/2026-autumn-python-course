"""Пакет методов численного интегрирования.

Публичные объекты:
    Integrand — тип подынтегральной функции.
    IntegrationMethod — тип метода интегрирования.
    integrate_left_rectangles — метод левых прямоугольников.
    integrate_midpoint_rectangles — метод средних прямоугольников.
    integrate_right_rectangles — метод правых прямоугольников.
    integrate_trapezoid — метод трапеций.
    integrate_simpson — метод Симпсона.
"""

from typing import List

from .rectangles import (
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
)
from .simpson import integrate_simpson
from .trapezoid import integrate_trapezoid
from .type_aliases import Integrand, IntegrationMethod

# Перечень имён, доступных при импорте пакета со звёздочкой.
__all__: List[str] = [
    "Integrand",
    "IntegrationMethod",
    "integrate_left_rectangles",
    "integrate_midpoint_rectangles",
    "integrate_right_rectangles",
    "integrate_trapezoid",
    "integrate_simpson",
]
