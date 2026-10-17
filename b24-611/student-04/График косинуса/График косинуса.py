#системные библиотеки
from pathlib import Path

#библиотеки для обработки и выведеня  данных

import numpy as np
import matplotlib.pyplot as plt

########################################################

angles = np.linspace(0,360,181)
radians =  np.deg2rad(angles)

fig, ax = plt.subplots(figsize = (8,4))
ax.plot(angles,np.sin(radians),label = "Синус", color = "tab:blue")
ax.plot(angles,cos)
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение функции")
ax.set_title("График зависимости тригонометрических функций от аргумента")
ax.grid(True)
ax.legend()

#Сохранение значений функций в файл

output_directory = Path(__file__).resolve().parent / "results"
output_directory.mkdir(exist_ok=True)

#Сохранение изображения графика на компьютер

fig.savefig(output_directory/"trigonometry_plot", dpi = 150)
plt.show()
