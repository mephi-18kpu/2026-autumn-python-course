from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

base_dir = Path(__file__).resolve().parent
series_dir = base_dir.parent / "hw3" / "data" / "series"
results_dir = base_dir / "results"
results_dir.mkdir(exist_ok=True)

files = sorted([p for p in series_dir.iterdir() if p.suffix == ".txt" and p.name != "README.md"])

report = []
max_mean, min_std = -float("inf"), float("inf")
max_file, min_file = "", ""

fig, ax = plt.subplots(figsize=(8, 5))

for f in files:
    v = np.loadtxt(f)
    n, mn, mx, avg, std = v.size, np.min(v), np.max(v), np.mean(v), np.std(v)
    above = np.sum(v > avg)

    report.append(f"Файл: {f.name}\n  • Кол-во: {n}\n  • Мин: {mn}\n  • Макс: {mx}\n  • Среднее: {avg:.2f}\n  • Ст. отклонение: {std:.2f}\n- Выше среднего: {above}\n")

    if avg > max_mean:
        max_mean, max_file = avg, f.name
    if std < min_std:
        min_std, min_file = std, f.name

    ax.plot(np.arange(n), v, label=f.name, marker="o", markersize=3)

report.append(f"Итоги:\nМакс. среднее: {max_file}\nМин. ст. отклонение: {min_file}")
(results_dir / "series_report.txt").write_text("\n".join(report), encoding="utf-8")

ax.set_title("Сравнение серий")
ax.grid(True)
ax.legend()
fig.savefig(results_dir / "series.png", dpi=150)
plt.close(fig)
