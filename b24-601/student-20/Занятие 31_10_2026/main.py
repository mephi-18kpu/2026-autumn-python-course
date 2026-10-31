"""."""

# System imports

# External imports
import numpy as np

# User imports
import integration_methods as im

#############################################

given_function: im.Integrand = lambda x: np.exp(x)


if __name__ == "__main__":
    net = np.linspace(0, 1, 100)
