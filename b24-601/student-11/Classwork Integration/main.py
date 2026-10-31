import numpy as np

from integration_methods import Integrand, IntegrationMethod

Integrand = lambda x: np.exp**x
space = np.linspace(0, 10**3, 10**2, np.float64)


