import numpy as np
from .type_aliases import Integrand

def integrate_simpson(nodes, function: Integrand) -> float:
    """Метод Симпсона (парабол)."""
    h = float(nodes[1] - nodes[0])
    n = nodes.size - 1
    
    total = function(float(nodes[0])) + function(float(nodes[-1]))
    
    for i in range(1, n, 2):
        total += 4.0 * function(float(nodes[i]))
        
    for i in range(2, n, 2):
        total += 2.0 * function(float(nodes[i]))
        
    return (h / 3.0) * total