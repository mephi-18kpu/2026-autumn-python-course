from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
root_dir = base_dir.parent.parent.parent
data_dir = root_dir / "code-examples" / "Модули и pathlib" / "data"

results_dir = base_dir / "results"
results_dir.mkdir(exist_ok=True)

files = sorted(
    p for p in data_dir.iterdir()
    if p.is_file() and p.suffix == ".txt"
)

report_lines = []
stats = []

fig, ax = plt.subplots(figsize=(10, 6))

for file_path in files:
    data = np.loadtxt(file_path)
    count = data.size
    minimum = np.min(data)
    maximum = np.max(data)
    mean = np.mean(data)
    std = np.std(data)
    above_mean = np.sum(data > mean)

    stats.append({
        "name": file_path.name,
        "mean": mean,
        "std": std,
    })

    report_lines.append(f"Файл: {file_path.name}")
    report_lines.append(f"  Количество значений: {count}")
    report_lines.append(f"  Минимум: {minimum}")
    report_lines.append(f"  Максимум: {maximum}")
    report_lines.append(f"  Среднее: {mean:.4f}")
    report_lines.append(f"  Стандартное отклонение: {std:.4f}")
    report_lines.append(f"  Значений выше среднего: {above_mean}")
    report_lines.append("")

max_mean_file = max(stats, key=lambda x: x["mean"])
min_std_file = min(stats, key=lambda x: x["std"])

report_lines.append(f"Наибольшее среднее: {max_mean_file['name']} ({max_mean_file['mean']:.4f})")
report_lines.append(f"Наименьшее стандартное отклонение: {min_std_file['name']} ({min_std_file['std']:.4f})")

report_path = results_dir / "series_report.txt"
report_path.write_text("\n".join(report_lines), encoding="utf-8")

for file_path in files:
    data = np.loadtxt(file_path)
    indices = np.arange(data.size)
    ax.plot(indices, data, label=file_path.name, marker="o", markersize=3)

ax.set_xlabel("Индекс элемента")
ax.set_ylabel("Значение")
ax.set_title("Сравнение серий измерений")
ax.grid(True)
ax.legend()

plot_path = results_dir / "series.png"
fig.savefig(plot_path, dpi=150, bbox_inches="tight")
plt.close(fig)
