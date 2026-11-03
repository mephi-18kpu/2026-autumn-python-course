# System imports

# External imports
import numpy as np
import matplotlib.pyplot as plt

# User imports
from integration_methods import (
Integrand,
IntegrationMethod,
integrate_left_rectangles,
integrate_right_rectangles,
integrate_midpoint_rectangles,
integrate_trapezoid,
integrate_simpson
)
#############################################

a=0
b=1
step=0.02
true_res=np.exp(1)-1

def main()->None:
    function: Integrand = lambda x: np.exp(x)
    integration_errors = {
        "left_rect": [],
        "right_rect": [],
        "mid_rect": [],
        "trapezoid": [],
        "simpson": []
    }
    grid_steps = []

    for i in range(1, 100):
        grid_steps.append(step/2*i)
        num_nodes =int((b - a) / (step/2*i) + 1)
        nodes=np.linspace(a, b, num_nodes)
        integration_errors['left_rect'].append(abs(integrate_left_rectangles(nodes, function)-true_res))
        integration_errors['right_rect'].append(abs(integrate_right_rectangles(nodes, function)-true_res))
        integration_errors['mid_rect'].append(abs(integrate_midpoint_rectangles(nodes, function)-true_res))
        integration_errors['trapezoid'].append(abs(integrate_trapezoid(nodes, function)-true_res))
        integration_errors['simpson'].append(abs(integrate_simpson(nodes, function)-true_res))

    print(f'{'Шаг интегрирования':<25} {'Левые прямоугольники':<25} {'Правые прямоугольники':<25} {'Средние прямоугольники':<25} {'Трапеции':<20} {'Симпсон':<20}')
    for i in range(0, len(grid_steps)):
        print(f'{grid_steps[i]:<25.2e} {integration_errors['left_rect'][i]:<25.2e} {integration_errors['right_rect'][i]:<25.2e} {integration_errors['mid_rect'][i]:<25.2e} {integration_errors['trapezoid'][i]:<20.2e} {integration_errors['simpson'][i]:<20.2e}')

    fig, ax=plt.subplots(figsize=(10,5))
    ax.loglog(grid_steps, integration_errors["left_rect"], label="Левые прямоугольники", color='tab:blue')
    ax.loglog(grid_steps, integration_errors["right_rect"], label="Правые прямоугольники", color='tab:red')
    ax.loglog(grid_steps, integration_errors["mid_rect"], label="Средние прямоугольники", color='tab:orange')
    ax.loglog(grid_steps, integration_errors["trapezoid"], label="Трапеции", color='tab:pink')
    ax.loglog(grid_steps, integration_errors["simpson"], label="Метод Симпсона", color='tab:green')
    ax.set_xlabel('Шаг интегрирования')
    ax.set_ylabel('Абсолютная погрешность')
    ax.legend()
    ax.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
