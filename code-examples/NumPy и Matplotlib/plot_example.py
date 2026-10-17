"""Построение графиков синуса и косинуса."""

# System imports
from pathlib import Path

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


angles = np.linspace(0, 180, 181)
radians = np.deg2rad(angles)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(angles, np.sin(radians), label="Синус", color="tab:blue")
ax.plot(angles, np.cos(radians), label="Косинус", color="tab:orange")
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение функции")
ax.set_title("Синус и косинус")
ax.grid(True)
ax.legend()

output_directory = Path(__file__).resolve().parent / "results"
output_directory.mkdir(exist_ok=True)
fig.savefig(output_directory / "trigonometry_plot.png", dpi=150)
plt.show()
