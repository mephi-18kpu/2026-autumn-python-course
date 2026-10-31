# System imports

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################

angles = np.linspace(0, 1080, 1081)
radians = np.deg2rad(angles)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(angles, np.cos(radians), label="Косинус", color="tab:green")
ax.plot(angles, np.sin(radians), label="Синус", color="tab:red")

#sinus = np.sin(radians)[np.sin(radians) !=0 ]
#cosinus = np.cos(radians)[np.cos(radians) !=0 ]

#ax.plot(angles, sinus / cosinus, label="Тангентс", color="tab:blue")
#ax.plot(angles,  cosinus / sinus, label="Котангентс", color="tab:orange")
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение функции")
ax.set_title("Тригонометрические функции")
ax.grid(True)
ax.legend()

plt.show()
