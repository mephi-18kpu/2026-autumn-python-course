"""Статистический анализ нескольких серий измерений и общий график."""

# System imports
from pathlib import Path

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


lesson_directory = Path(__file__).resolve().parent
data_directory = lesson_directory / "data" / "series"
results_directory = lesson_directory / "results"
results_directory.mkdir(exist_ok=True)

input_files = sorted(
    path for path in data_directory.iterdir()
    if path.is_file() and path.suffix == ".txt"
)

if not input_files:
    raise FileNotFoundError(f"В каталоге нет .txt-файлов: {data_directory}")

report_lines = ["ОТЧЁТ ПО СЕРИЯМ ИЗМЕРЕНИЙ", ""]
series_data = []
total_values = 0
largest_mean_file = None
largest_mean = None
smallest_std_file = None
smallest_std = None

for input_path in input_files:
    values = np.loadtxt(input_path, dtype=float)
    values = np.atleast_1d(values)

    if values.size == 0:
        raise ValueError(f"Файл не содержит числовых значений: {input_path.name}")

    count = int(values.size)
    minimum = float(np.min(values))
    maximum = float(np.max(values))
    mean = float(np.mean(values))
    standard_deviation = float(np.std(values))
    above_mean_count = int(np.count_nonzero(values > mean))

    total_values += count
    series_data.append((input_path.name, values))

    report_lines.extend([
        f"Файл: {input_path.name}",
        f"Количество значений: {count}",
        f"Минимум: {minimum:.6f}",
        f"Максимум: {maximum:.6f}",
        f"Среднее: {mean:.6f}",
        f"Стандартное отклонение: {standard_deviation:.6f}",
        f"Значений выше среднего: {above_mean_count}",
        "",
    ])

    if largest_mean is None or mean > largest_mean:
        largest_mean = mean
        largest_mean_file = input_path.name

    if smallest_std is None or standard_deviation < smallest_std:
        smallest_std = standard_deviation
        smallest_std_file = input_path.name

report_lines.extend([
    f"Общее количество значений: {total_values}",
    f"Наибольшее среднее: {largest_mean:.6f} ({largest_mean_file})",
    f"Наименьшее стандартное отклонение: {smallest_std:.6f} ({smallest_std_file})",
])
(results_directory / "series_report.txt").write_text(
    "\n".join(report_lines) + "\n",
    encoding="utf-8",
)

fig, ax = plt.subplots()
for file_name, values in series_data:
    indices = np.arange(values.size)
    ax.plot(indices, values, label=file_name)

ax.set_xlabel("Индекс элемента")
ax.set_ylabel("Значение")
ax.set_title("Сравнение серий измерений")
ax.grid(True)
ax.legend()
fig.savefig(results_directory / "series.png", dpi=150)
plt.close(fig)

print(f"Обработано файлов: {len(series_data)}")
print(f"Всего значений: {total_values}")
print(f"Отчёт сохранён: {results_directory / 'series_report.txt'}")
print(f"График сохранён: {results_directory / 'series.png'}")
