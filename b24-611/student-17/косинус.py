from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from fontTools.diff import color

radians = np.linspace(0,6 * np.pi, 100)

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(radians, np.cos(radians), label="Косинус", color="tab:orange")
ax.set_xlabel("Угол, радианы")
ax.set_ylabel("Значение функции")
ax.set_title("График косинуса")
ax.grid(True)
ax.legend()

output_directory = Path(__file__).resolve().parent/"results"
output_directory.mkdir(exist_ok=True)
fig.savefig(output_directory / "trigonometry_plot.png", dpi=150)
plt.show()
