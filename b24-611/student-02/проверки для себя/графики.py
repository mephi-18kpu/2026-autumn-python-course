from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


angles = np.linspace(0, 600, 181)
radians = np.deg2rad(angles)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(angles, np.sin(radians), label="синус", color="tab:blue")
ax.plot(angles, np.cos(radians), label="косинус", color="tab:orange")
ax.set_xlabel("угол, градусы")
ax.set_ylabel("значение функции")
ax.set_title("синус и косинус")
ax.grid(True)
ax.legend()

output_directory = Path(__file__).resolve().parent / "results"
output_directory.mkdir(exist_ok=True)
fig.savefig(output_directory / "trigonometry_plot.png", dpi=150)
plt.show()
