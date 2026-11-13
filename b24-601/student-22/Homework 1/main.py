import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(r"C:\Python\2026-autumn-python-course\code-examples\NumPy и Matplotlib")
data_dir = base_path / "data" / "series"
results_dir = base_path / "results"

results_dir.mkdir(exist_ok=True)

txt_files = []

for file_path in data_dir.iterdir():
    if file_path.is_file() and file_path.name.endswith(".txt"):
        txt_files.append(file_path)

txt_files.sort()

max_mean = -999999.0
max_mean_file = ""
min_std = 999999.0
min_std_file = ""

report_text = ""

fig, ax = plt.subplots()

for file_path in txt_files:
    data = np.loadtxt(file_path)

    count = len(data)
    minimum = np.min(data)
    maximum = np.max(data)
    mean_val = np.mean(data)
    std_val = np.std(data)

    above_mean = 0
    for number in data:
        if number > mean_val:
            above_mean = above_mean + 1

    if mean_val > max_mean:
        max_mean = mean_val
        max_mean_file = file_path.name

    if std_val < min_std:
        min_std = std_val
        min_std_file = file_path.name

    report_text = report_text + "Файл: " + file_path.name + "\n"
    report_text = report_text + "  Количество: " + str(count) + "\n"
    report_text = report_text + "  Минимум: " + str(round(minimum, 2)) + "\n"
    report_text = report_text + "  Максимум: " + str(round(maximum, 2)) + "\n"
    report_text = report_text + "  Среднее: " + str(round(mean_val, 2)) + "\n"
    report_text = report_text + "  Станд. отклонение: " + str(round(std_val, 2)) + "\n"
    report_text = report_text + "  Значений выше среднего: " + str(above_mean) + "\n"

    x_axis = []
    for i in range(count):
        x_axis.append(i)

    ax.plot(x_axis, data, label=file_path.name)

report_text = report_text + "\nРезультаты:\n"
report_text = report_text + "Наибольшее среднее: " + max_mean_file + "\n"
report_text = report_text + "Наименьшее станд. отклонение: " + min_std_file + "\n"

report_file_path = results_dir / "series_report.txt"
file = open(report_file_path, "w", encoding="utf-8")
file.write(report_text)
file.close()

ax.set_xlabel("Индекс элемента")
ax.set_ylabel("Значение")
ax.set_title("Сравнение серий измерений")
ax.grid(True)
ax.legend()

image_path = results_dir / "series.png"
plt.savefig(image_path)

plt.show()