import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0, 6 * np.pi, 1000 )

y_cos = np.cos(x)
y_tan = np.tan(x)
y_cot = 1/np.tan(x)

y_tan[abs(y_tan) > 10] = np.nan
y_cot[abs(y_tan) > 10] = np.nan

plt.figure(figsize=(12, 6))
plt.plot(x, y_cos, label="y=cos(x)", color="blue", linewidth=2)
plt.plot(x, y_tan, label="y=tan(x)", color="red", linewidth=1.5)
plt.plot(x, y_cot, label="y=cot(x)", color="green", linewidth=1.5)
plt.title("график cos от 0-0pi")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid(True)
plt.legend()

plt.show()
