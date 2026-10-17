import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 1080, 500)
y = np.sin(np.radians(x))
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='y = sin(x)', color='blue', linewidth=2)
plt.title('График синуса от 0 до 6pi (в градусах')
plt.xlabel('Градусы')
plt.ylabel('Значение синуса')
plt.xticks(np.arange(0, 1081, 180))
plt.grid(True)
plt.legend()
plt.show()
