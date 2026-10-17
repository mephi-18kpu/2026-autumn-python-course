""" Создает """
from math import degrees

import matplotlib.pyplot as plt
# System imports
import numpy as np
import matplotlib as mlt

# External imports

# User imports

#############################################

if __name__ == "__main__":

    degrees_axis = np.linspace(0, 1080, 1000)
    sin_values_axis = np.sin(np.deg2rad(degrees_axis))

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(degrees_axis, sin_values_axis, label="Синус", color="blue")
    ax.set_xlabel("Угол, градусы")
    ax.set_ylabel("Значение функции")
    ax.set_title("Синус")
    ax.grid()

    plt.show()

