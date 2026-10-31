import numpy as np
import matplotlib.pyplot as plt

n=int(input('Введите желаемое количество точек '))
radangles=np.linspace(0, 18.84, n)
degangles=radangles/6.28*180

fig, (ax1, ax2, ax3, ax4) = plt.subplots(2,2, figsize=(8,4))
ax1.plot(degangles, np.cos(radangles), label='косинус', color='tab:blue')
ax2.plot(degangles, np.sin(radangles), label='sinus', color='tab:red')
ax3.plot(degangles, np.tan(radangles) label='tangens', color='tab:olive')
ax3.plot(degangles, np.tan(radangles) label='tangens', color='tab:pink')
ax1.set(xlabel='Углы')
ax1.set(ylabel='Значение функций')
ax1.grid(True)
ax1.legend()
ax2.set(xlabel='Углы')
ax2.set(ylabel='Значение функций')
ax2.grid(True)
ax2.legend()



plt.show()
