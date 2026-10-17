"""Сравнение теоретической кривой с отдельными измерениями."""

# System imports
from pathlib import Path

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


curve_angles = np.linspace(0, 180, 181)
curve_values = np.sin(np.deg2rad(curve_angles))

measured_angles = np.array([0, 30, 60, 90, 120, 150, 180])
measured_values = np.array([0.02, 0.48, 0.89, 0.97, 0.85, 0.52, -0.01])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(curve_angles, curve_values, label="Теоретический синус", color="tab:blue")
ax.scatter(measured_angles, measured_values, label="Измерения", color="tab:red")
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение синуса")
ax.set_title("Кривая и отдельные точки")
ax.grid(True)
ax.legend()

output_directory = Path(__file__).resolve().parent / "results"
output_directory.mkdir(exist_ok=True)
fig.savefig(output_directory / "scatter_example.png", dpi=150)
plt.show()
