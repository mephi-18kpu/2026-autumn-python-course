import numpy as np
from .type_aliases import Integrand, Nodes


def integrate_simpson(nodes: Nodes, function: Integrand) -> float:
    if len(nodes) < 3:
        raise ValueError("Симпсон: нужно минимум 3 узла")
    if len(nodes) % 2 == 0:
        raise ValueError("Симпсон: нужно нечётное число узлов")

    h = float(nodes[1] - nodes[0])
    total = function(float(nodes[0])) + function(float(nodes[-1]))
    for i in range(1, len(nodes) - 1):
        w = 4.0 if i % 2 == 1 else 2.0
        total += w * function(float(nodes[i]))
    return float(total * h / 3.0)
