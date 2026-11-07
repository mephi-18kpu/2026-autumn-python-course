import numpy as np
from .type_aliases import Integrand

def integrate_trapezoid(nodes, function: Integrand) -> float:
    """Метод трапеций на равномерной сетке."""
    h = float(nodes[1] - nodes[0])
    total = 0.5 * function(float(nodes[0])) + 0.5 * function(float(nodes[-1]))
    
    for x in nodes[1:-1]:
        total += function(float(x))
        
    return h * total