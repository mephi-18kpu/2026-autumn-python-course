import numpy as np
import matplotlib.pyplot as plt

#Импортируем наш созданный пакет

from integration_methods import Integrand, IntegrationMethod
from integration_methods import integrate_left_rectangles
from integration_methods import integrate_right_rectangles
from integration_methods import integrate_midpoint_rectangles
from integration_methods import integrate_trapezoid
from integration_methods import integrate_simpson

f_main: Integrand = lambda x: np.exp(x)   #Создаем нашу подынтегральную функцию "е в степ х"
tochnoe_znach = np.e - 1.0  #Чему равен в действительности интеграл


#В списке metody лежат пары из названия для графика и функции метода
metody: list[tuple[str, IntegrationMethod]] = [
    ("Левые прямоугольники", integrate_left_rectangles),
    ("Правые прямоугольники", integrate_right_rectangles),
    ("Средние прямоугольники", integrate_midpoint_rectangles),
    ("Трапеции", integrate_trapezoid),
    ("Симпсон", integrate_simpson)
]

n_massiv = [2, 4, 8, 16, 32, 64, 128] #Количество интервалов на которые разбиваем отрезок
h_values = [] #Пустой список, где будут добавляться значения шага для оси X
massiv_oshibok = [[] for _ in range(len(metody))]  #создаются пустые списки по количеству методов, для складывания ошибок

for n in n_massiv:   #Перебираем интервалы
    setka = np.linspace(0, 1, n + 1, dtype=np.float64) #Генерируем сетку, создавая точки исходя из количества интервалов
    shag = setka[1] - setka[0]
    h_values.append(shag) #Добавляем шаг в список

    for idx in range(len(metody)):
        method_name, method_func = metody[idx]
        result = method_func(setka, f_main) #Запуск метода
        oshibka = abs(result - tochnoe_znach) #Значение ошибки
        massiv_oshibok[idx].append(oshibka)

fig, ax = plt.subplots(figsize=(10, 6))  #Создание пустого холста

for idx in range(len(metody)):
    method_name = metody[idx][0]
    ax.loglog(h_values, massiv_oshibok[idx], marker='o', label=method_name)
#loglog значит что 2 оси у графика будут логарифмические.
#В логарифмическом масштабе зависимость ошибки от шага становится прямой линией.
#Наклон этой линии покажет, насколько метод точен

#Подписаны оси и заголовок
ax.set_xlabel("Шаг сетки h")
ax.set_ylabel("Абсолютная погрешность")
ax.set_title("Зависимость погрешности от шага")
ax.grid(True, which="both", linestyle="--") #Включаем сетку
ax.legend() #Легенда графика

fig.savefig("error_plot.png") #Сохраняем грфик в папку с проектом
plt.show() #Открываем окно с графиком на экране

#Результаты полностью согласуются с теорией.
#При уменьшении шага сетки вдвое погрешность методов левых и правых прямоугольников уменьшается примерно в 2 раза,
#средних прямоугольников и трапеций — в 4 раза, а метода Симпсона — в 16 раз,
#что согласуется с таблицей из лекции.
