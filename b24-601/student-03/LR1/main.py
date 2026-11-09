import numpy as np
import matplotlib.pyplot as plt
from integration_methods import (   #Импорты
    Integrand,
    IntegrationMethod,
    integrate_left_rectangles,
    integrate_midpoint_rectangles,
    integrate_right_rectangles,
    integrate_trapezoid,
    integrate_simpson,
)

function: Integrand = lambda x: np.exp(x)
exact_value = np.e - 1
a = 0
b = 1               ##Параметры сетки

# Лучше чуть больше элементов сделать, 10 ** 4 и 10**5 добавь
N_array = [10, 10 ** 2, 10 ** 3]

methods = {
    "Левые прямоугольники": integrate_left_rectangles,
    "Правые прямоугольники": integrate_right_rectangles,
    "Средние прямоугольники": integrate_midpoint_rectangles,
    "Трапеции": integrate_trapezoid,
    "Симпсон": integrate_simpson,
}               #Словарь: Названия - методы

errors_by_method = {name: [] for name in methods.keys()}  #Словарь ошибок соответ. методу

for N in N_array:
    nodes = np.linspace(a, b, N)

    # Лучше сразу в N_array делать нужное количество элементов
    if N % 2 == 0:
        nodes = np.linspace(a, b, N + 1)

    for name, method in methods.items():            #Считаем ошибку для каждого метода

        # Для сохранения ошибки создавать ещё один словарь не обязательно.
        # Лучше просто
        # error = abs(exact_value - method(nodes, function))
        # errors_by_method[name].append(error)
        error = {name: abs(exact_value - method(nodes, function))}

        errors_by_method[name].append(error[name]) #Добавялем в словарь по названию метода ошибку для него


#График Графичек Графинчик
# Лучше делай через fig, ax
# Это явнее и удобнее при дальнейшей модификации графиков
plt.figure(figsize=(10, 6))

for name in methods.keys():
    plt.loglog(N_array, errors_by_method[name], marker='o', label=name)

plt.xlabel("Количество узлов N (логарифмический масштаб)")
plt.ylabel("Абсолютная погрешность (логарифмический масштаб)")
plt.title("Зависимость абсолютной погрешности от количества узлов N")
plt.grid(True, which="both", linestyle="--", alpha=0.7)
plt.legend()

# Лучше размещай в самом конце, чтобы сначала всё вывелось в консоль,
# а потом уже график на весь экран появлялся
plt.show()

#Табличка Табличечка *тут не придумал*
print(f"{'Метод':<25} | {'N=10':<12} | {'N=100':<12} | {'N=1000':<12}")
print("-" * 70)

for name in methods.keys():
    # Вот это мега костыль, тк при изменении количества элементов
    # в N_array надо будет переписывать ещё и здесь.
    # Так что лучше подумай и придумай как сделать через цикл.
    err_10 = errors_by_method[name][0]
    err_100 = errors_by_method[name][1]
    err_1000 = errors_by_method[name][2]


    print(f"{name:<25} | {err_10:<12.2e} | {err_100:<12.2e} | {err_1000:<12.2e}")


"""
Как мы видим методы левых и правых прямоугольников дают практически одинаковый результат
Стоит отметить, что метод Симпсона, как и предполагалось, оказывается самым точным и,
чем больше сетку мы ему даем, тем он точнее апроксимирует исходную функцию
"""
