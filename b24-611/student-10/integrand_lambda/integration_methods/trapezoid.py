import numpy as np
from .type_aliases import Integrand, Nodes


def integrate_trapezoid(nodes: Nodes, function: Integrand) -> float:
    h = float(nodes[1] - nodes[0])
    total = 0.5 * (function(float(nodes[0])) + function(float(nodes[-1])))
    for x in nodes[1:-1]:           # внутренние узлы целиком
        total += function(float(x))
    return float(total * h)
