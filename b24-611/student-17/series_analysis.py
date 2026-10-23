
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "series"
RESULTS_DIR = BASE_DIR / "results"

if not DATA_DIR.is_dir():
    raise FileNotFoundError(f"Папка с данными не найдена: {DATA_DIR}")

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

files = sorted(
    (
        file for file in DATA_DIR.iterdir()
        if file.is_file() and file.suffix == ".txt"
    ),
    key=lambda file: file.name
)

if not files:
    raise ValueError("В папке data/series нет файлов .txt")

statistics = []
fig, ax = plt.subplots()

for file in files:
    if file.stat().st_size == 0:
        print(f"Предупреждение: файл {file.name} пуст и будет пропущен.")
        continue

    try:
        data = np.loadtxt(file, ndmin=1)
    except ValueError as error:
        print(f"Ошибка чтения {file.name}: {error}")
        continue

    if data.ndim != 1:
        print(f"Предупреждение: файл {file.name} содержит не одну серию.")
        continue

    if data.size == 0:
        print(f"Предупреждение: файл {file.name} не содержит чисел.")
        continue

    if not np.all(np.isfinite(data)):
        print(f"Предупреждение: файл {file.name} содержит NaN или Inf.")
        continue

    count = len(data)
    minimum = np.min(data)
    maximum = np.max(data)
    mean = np.mean(data)
    std = np.std(data)
    above_mean = np.sum(data > mean)

    statistics.append({
        "name": file.name,
        "count": count,
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "std": std,
        "above_mean": above_mean
    })

    x = np.arange(count)
    ax.plot(x, data, label=file.name)

if not statistics:
    plt.close(fig)
    raise ValueError("Не удалось обработать ни одну серию")

max_mean = max(statistics, key=lambda s: s["mean"])
min_std = min(statistics, key=lambda s: s["std"])

report_path = RESULTS_DIR / "series_report.txt"

with report_path.open("w", encoding="utf-8") as report:
    report.write("Анализ серий измерений\n")
    report.write("=" * 40 + "\n\n")

    for s in statistics:
        report.write(f"Файл: {s['name']}\n")
        report.write(f"Количество: {s['count']}\n")
        report.write(f"Минимум: {s['min']:.4f}\n")
        report.write(f"Максимум: {s['max']:.4f}\n")
        report.write(f"Среднее: {s['mean']:.4f}\n")
        report.write(f"Стандартное отклонение: {s['std']:.4f}\n")
        report.write(f"Значений выше среднего: {s['above_mean']}\n")
        report.write("-" * 40 + "\n")

    report.write("\nИтоги:\n")
    report.write(
        f"Наибольшее среднее: {max_mean['name']} "
        f"({max_mean['mean']:.4f})\n"
    )
    report.write(
        f"Наименьшее стандартное отклонение: "
        f"{min_std['name']} ({min_std['std']:.4f})\n"
    )

ax.set_title("Сравнение серий измерений")
ax.set_xlabel("Индекс элемента")
ax.set_ylabel("Значение")
ax.grid(True)
ax.legend()

fig.tight_layout()
fig.savefig(RESULTS_DIR / "series.png", dpi=150)
plt.close(fig)

print("Анализ завершён!")
print(f"Отчёт: {report_path}")
print(f"График: {RESULTS_DIR / 'series.png'}")
