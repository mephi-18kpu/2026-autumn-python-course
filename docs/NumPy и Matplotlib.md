# NumPy и Matplotlib: массивы, вычисления и графики

Для примеров понадобятся библиотеки NumPy и Matplotlib. Установите их в используемое окружение Python:

```console
python -m pip install numpy matplotlib
```

В коде принято использовать короткие имена `np` для NumPy и `plt` для модуля `matplotlib.pyplot`:

```python
import matplotlib.pyplot as plt
import numpy as np
```

## Зачем нужен NumPy

Список Python может хранить значения разных типов. Для численных вычислений часто нужен массив значений одного типа. Основной объект NumPy — `ndarray`: многомерный массив, над элементами которого можно выполнять операции сразу. Значительная часть вычислений внутри NumPy выполняется с помощью оптимизированного кода на C. Поэтому при обработке больших числовых массивов такие операции обычно быстрее циклов Python; на маленьких массивах выигрыш не гарантирован.

```python
values = [2, 4, 6]
print(values * 2)  # [2, 4, 6, 2, 4, 6] — повторение списка.

array = np.array(values)
print(array * 2)  # [ 4  8 12] — умножение каждого элемента.
```

NumPy полезен, когда нужны численные массивы, вычисления по всем элементам, статистика и подготовка данных для графиков. Обычные списки остаются удобными для небольших коллекций и значений разных типов.

## Создание и свойства массивов

```python
print(np.array([2, 4, 6]))  # [2 4 6].
print(np.arange(0, 10, 2))  # [0 2 4 6 8]: шаг равен 2, правая граница не входит.
print(np.linspace(0, 1, 5))  # [0.   0.25 0.5  0.75 1.  ]: пять равноотстоящих значений.
print(np.zeros(4))  # [0. 0. 0. 0.].

values = np.array([2, 4, 6])
print(values.dtype)  # Тип элементов, например int64; зависит от платформы.
print(values.shape)  # (3,) — длина единственного измерения.
print(values.ndim)  # 1 — количество измерений.
print(values.size)  # 3 — общее количество элементов.
```

`np.arange(start, stop, step)` удобно использовать, когда известен шаг. `np.linspace(start, stop, num)` — когда известно число точек на отрезке, включая обе границы по умолчанию. Запись `(3,)` — кортеж из одного числа; запятая отличает его от числа в скобках.

Двумерный массив можно представить как таблицу строк и столбцов:

```python
table = np.array([[1, 2, 3], [4, 5, 6]])
print(table.shape)  # (2, 3): две строки и три столбца.
print(table[1, 2])  # 6: строка с индексом 1, столбец с индексом 2.
```

## Операции, выборка и статистика

Арифметические операции с массивом применяются поэлементно. Два массива одинаковой формы можно складывать поэлементно. Обычные индексы, срезы и логические маски помогают выбирать значения:

```python
values = np.array([10, 12, 15])

print(values + 2)  # [12 14 17].
print(values * 2)  # [20 24 30].
print(values + np.array([1, 2, 3]))  # [11 14 18].
print(values[0])  # 10.
print(values[1:])  # [12 15].
print(values > 11)  # [False  True  True].
print(values[values > 11])  # [12 15].

print(np.sum(values))  # 37.
print(np.mean(values))  # 12.333333333333334.
print(np.min(values))  # 10.
print(np.max(values))  # 15.
print(np.std(values))  # Примерно 2.0548; по умолчанию деление на N.
```

Выражение `values > 11` создаёт массив логических значений. Запись `values[values > 11]` оставляет только те элементы, для которых условие истинно. `np.std()` по умолчанию вычисляет стандартное отклонение с `ddof=0`; при необходимости другого правила деления его задают явно.

## Математические функции

Функции NumPy также работают поэлементно. Для тригонометрических функций углы задают **в радианах**. Если исходные углы записаны в градусах, используйте `np.deg2rad()`:

```python
angles = np.array([0, 30, 90, 180])
radians = np.deg2rad(angles)

print(np.sin(radians))  # Примерно [0.  0.5 1.  0.]; последний элемент может быть близок к нулю.
print(np.cos(radians))  # Примерно [ 1.         0.8660254  0.        -1.       ].
print(np.abs(np.array([-3, 2, -1])))  # [3 2 1].
print(np.sqrt(np.array([0, 4, 9])))  # [0. 2. 3.].
print(np.pi)  # Примерно 3.141592653589793.
```

Очень маленькие остатки вместо точного нуля возникают из-за хранения вещественных чисел с конечной точностью. Например, `np.sin(np.pi)` может оказаться близким к нулю, но не равным ему точно.

## Текстовые файлы с числовыми данными

Файл [data/measurements.txt](data/measurements.txt) содержит три числа, по одному в строке: `10`, `12`, `15`. NumPy умеет загружать такие файлы и сохранять результат. Путь строим от каталога скрипта, используя `pathlib` из предыдущего занятия:

```python
from pathlib import Path

import numpy as np

lesson_directory = Path(__file__).resolve().parent
input_path = lesson_directory / "data" / "measurements.txt"
values = np.loadtxt(input_path)

print(values)  # [10. 12. 15.].
print(np.mean(values))  # 12.333333333333334.

output_directory = lesson_directory / "results"
output_directory.mkdir(exist_ok=True)
np.savetxt(output_directory / "doubled.txt", values * 2, fmt="%.1f")
# В doubled.txt будут строки 20.0, 24.0 и 30.0.
```

`np.loadtxt()` подходит для простых таблиц чисел. Параметр `fmt` в `np.savetxt()` задаёт формат записи; `"%.1f"` означает одно число после десятичной точки. Если в исходном файле есть заголовки или нестандартные разделители, параметры чтения потребуется настроить.

## Как устроен график Matplotlib

В Matplotlib `Figure` — вся фигура, включая поля и подписи; `Axes` — область, на которой строят данные; `Axis` — отдельная ось координат внутри этой области. В примерах используем явные объекты:

```python
fig, ax = plt.subplots()
```

`plt.subplots()` создаёт фигуру и область графика. Переменная `fig` нужна, например, для сохранения изображения через `fig.savefig()`. Через `ax` строят данные и задают заголовок, подписи осей, сетку и легенду. Если областей несколько, `plt.subplots()` может вернуть набор объектов `Axes`; здесь работаем с одной областью.

Ниже три примера для повторения на занятии. Они адаптируют приёмы из [официального простого графика](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html), [документации `Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html) и [примера с погрешностями](https://matplotlib.org/stable/gallery/statistics/errorbar_features.html). Каждый файл можно запускать отдельно. Изображение сохраняется в `results`, затем открывается окно графика. Если окно не появилось, проверьте, в каком окружении запускаете скрипт и доступен ли графический интерфейс.

### Линии: `ax.plot()`

Метод `plot(x, y)` соединяет точки линией. В [plot_example.py](plot_example.py) для углов от 0° до 180° строятся две функции:

```python
"""Построение графиков синуса и косинуса."""

# System imports
from pathlib import Path

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


angles = np.linspace(0, 180, 181)
radians = np.deg2rad(angles)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(angles, np.sin(radians), label="Синус", color="tab:blue")
ax.plot(angles, np.cos(radians), label="Косинус", color="tab:orange")
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение функции")
ax.set_title("Синус и косинус")
ax.grid(True)
ax.legend()

output_directory = Path(__file__).resolve().parent / "results"
output_directory.mkdir(exist_ok=True)
fig.savefig(output_directory / "trigonometry_plot.png", dpi=150)
plt.show()
```

`figsize=(8, 4)` задаёт размер фигуры в дюймах, а `dpi=150` — разрешение сохранённого изображения. `label` задаёт подпись линии для легенды, которую показывает `ax.legend()`. `color` задаёт цвет, `ax.grid(True)` включает сетку. Важно передать `np.sin()` и `np.cos()` радианы, а по горизонтали оставить градусы для читаемой подписи.

### Отдельные точки: `ax.scatter()`

Когда данные представляют отдельные измерения, их удобно показывать точками. В [scatter_example.py](scatter_example.py) линия показывает теоретическую зависимость, а точки — отдельные измеренные значения:

```python
"""Сравнение теоретической кривой с отдельными измерениями."""

# System imports
from pathlib import Path

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


curve_angles = np.linspace(0, 180, 181)
curve_values = np.sin(np.deg2rad(curve_angles))

measured_angles = np.array([0, 30, 60, 90, 120, 150, 180])
measured_values = np.array([0.02, 0.48, 0.89, 0.97, 0.85, 0.52, -0.01])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(curve_angles, curve_values, label="Теоретический синус", color="tab:blue")
ax.scatter(measured_angles, measured_values, label="Измерения", color="tab:red")
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение синуса")
ax.set_title("Кривая и отдельные точки")
ax.grid(True)
ax.legend()

output_directory = Path(__file__).resolve().parent / "results"
output_directory.mkdir(exist_ok=True)
fig.savefig(output_directory / "scatter_example.png", dpi=150)
plt.show()
```

В `ax.scatter(x, y)` массивы координат должны содержать одинаковое число элементов. У линии и точек разные наборы координат: плотная сетка для гладкой кривой и семь углов для измерений. На одном `Axes` можно сочетать разные способы отображения.

### Погрешности: `ax.errorbar()`

Если для каждого измерения известна погрешность по вертикали, добавьте её через `yerr`. В [errorbar_example.py](errorbar_example.py) значения погрешностей заданы отдельным массивом:

```python
"""Отображение измерений с заданными погрешностями."""

# System imports
from pathlib import Path

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


curve_angles = np.linspace(0, 180, 181)
curve_values = np.sin(np.deg2rad(curve_angles))

measured_angles = np.array([0, 30, 60, 90, 120, 150, 180])
measured_values = np.array([0.02, 0.48, 0.89, 0.97, 0.85, 0.52, -0.01])
measurement_errors = np.array([0.05, 0.04, 0.06, 0.05, 0.07, 0.05, 0.06])

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(curve_angles, curve_values, label="Теоретический синус", color="tab:blue")
ax.errorbar(
    measured_angles,
    measured_values,
    yerr=measurement_errors,
    fmt="o",
    capsize=4,
    label="Измерения с погрешностями",
    color="tab:red",
)
ax.set_xlabel("Угол, градусы")
ax.set_ylabel("Значение синуса")
ax.set_title("Измерения и погрешности")
ax.grid(True)
ax.legend()

output_directory = Path(__file__).resolve().parent / "results"
output_directory.mkdir(exist_ok=True)
fig.savefig(output_directory / "errorbar_example.png", dpi=150)
plt.show()
```

`yerr` задаёт размер вертикальных отрезков погрешности для каждой точки; этот массив должен соответствовать массиву измерений. `fmt="o"` показывает значения круглыми маркерами, `capsize=4` добавляет горизонтальные окончания отрезков. Matplotlib не вычисляет погрешности по измеренным значениям: в этом примере их передали готовыми. Не следует автоматически считать `np.std()` всей серии погрешностью каждого отдельного измерения.

### Короткая запись через `pyplot`

Для небольшого одноразового графика можно вызывать функции прямо через `plt`. Такой стиль тоже встречается в документации Matplotlib:

```python
import matplotlib.pyplot as plt

plt.plot([0, 1, 2], [0, 1, 4], label="y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
```

`plt` обращается к текущей фигуре и текущей области графика. Когда нужно явно понимать, к какому графику относятся линии и подписи, запись через `fig, ax = plt.subplots()` удобнее для чтения.

## Самостоятельное задание 1. Сравнение серий измерений

В каталоге [data/series](data/series/README.md) лежат несколько файлов `.txt`: по одному числу в строке, длина серий различается. Напишите `series_analysis.py` рядом с этим конспектом.

1. Через `Path.iterdir()` найдите только обычные `.txt`-файлы. Обрабатывайте их в отсортированном по имени порядке; `README.md` пропускайте.
2. Загрузите каждую серию через `np.loadtxt()`. Для каждого файла вычислите количество значений, минимум, максимум, среднее и стандартное отклонение, а также количество значений выше среднего этой серии.
3. Определите, у какого файла наибольшее среднее и у какого наименьшее стандартное отклонение. Сохраните текстовый отчёт в `results/series_report.txt` в кодировке UTF-8. Указывайте имя файла рядом с каждым результатом.
4. Создайте одну фигуру и одну область графика через `fig, ax = plt.subplots()`. На общей области нарисуйте все серии через `ax.plot()`: по горизонтали — индекс элемента, по вертикали — значение. Добавьте подписи осей, заголовок, сетку и легенду с именами файлов. Сохраните изображение в `results/series.png`.

При повторном запуске программа должна обновлять отчёт и изображение, а не добавлять новые данные к старому отчёту. Длины серий различаются: для каждой создавайте собственный массив индексов подходящей длины.

## Самостоятельное задание 2. Тригонометрия по файлам

В каталоге [data/angles](data/angles/README.md) лежат файлы с углами в градусах, по одному значению в строке. Напишите `angles_analysis.py` рядом с этим конспектом.

1. Через `Path.iterdir()` найдите `.txt`-файлы и обработайте их в отсортированном по имени порядке. Для каждого файла загрузите углы через `np.loadtxt()`, переведите их в радианы и вычислите синус и косинус.
2. Для каждого набора сохраните два текстовых файла: `results/angles/<имя_без_расширения>_sin.txt` и `results/angles/<имя_без_расширения>_cos.txt`. Используйте `Path.stem` и `np.savetxt()`. Каталог результатов создайте программой.
3. Для каждого входного файла посчитайте максимальный угол и число значений синуса строго больше `0.6`. Запишите эти результаты и имя файла с наибольшим таким количеством в `results/angles_report.txt` в кодировке UTF-8.
4. Для каждого набора создайте отдельную фигуру через `fig, ax = plt.subplots()`: проведите линии синуса и косинуса на плотной сетке углов от 0° до 180°, а поверх добавьте через `ax.scatter()` точки функций для углов из текущего файла. Добавьте подписи, легенду и сетку. Сохраните рисунок в `results/angles/<имя_без_расширения>.png`.

Следите, чтобы значения синуса и косинуса считались от радиан, а по горизонтали на рисунке отображались градусы. При повторном запуске выходные файлы должны обновляться.

## Документация

- [NumPy для начинающих](https://numpy.org/doc/stable/user/absolute_beginners.html).
- [`numpy.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) и [`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html).
- [Matplotlib: Figure, Axes и два стиля работы](https://matplotlib.org/stable/users/explain/quick_start.html).
- [Пример `plot` в галерее Matplotlib](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html).
- [Справка по `Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html) и [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html).
