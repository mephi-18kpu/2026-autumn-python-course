from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
data_dir = base_dir / "data" / "series"
res_dir = base_dir / "results"
res_dir.mkdir(exist_ok=True)

files = []
for f in data_dir.iterdir():
    if f.is_file() and f.suffix == ".txt":
        files.append(f)
files = sorted(files)

fig, ax = plt.subplots()
report = ""

max_mean = -999.0
max_mean_file = ""
min_std = 999999.0
min_std_file = ""

for f in files:
    arr = np.loadtxt(f)
    cnt = len(arr)
    mn = np.min(arr)
    mx = np.max(arr)
    mean = np.mean(arr)
    std = np.std(arr)
    above_mean = np.count_nonzero(arr > mean)

    if mean > max_mean:
        max_mean = mean
        max_mean_file = f.name

    if std < min_std:
        min_std = std
        min_std_file = f.name

    report += f"Файл: {f.name}\n"
    report += f"Количество: {cnt}\n"
    report += f"Минимум: {mn}, Максимум: {mx}\n"
    report += f"Среднее: {mean:.2f}, Ст.отклонение: {std:.2f}\n"
    report += f"Значений выше среднего: {above_mean}\n\n"

    idx = np.arange(len(arr))
    ax.plot(idx, arr, label=f.name)

report += f"Наибольшее среднее: {max_mean_file}\n"
report += f"Наименьшее ст.отклонение: {min_std_file}\n"

with open(res_dir / "series_report.txt", "w", encoding="utf-8") as f_out:
    f_out.write(report)

ax.set_xlabel("Индекс")
ax.set_ylabel("Значение")
ax.set_title("Серии измерений")
ax.grid(True)
ax.legend()
fig.savefig(res_dir / "series.png")
plt.show()
