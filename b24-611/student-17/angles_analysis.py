
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "angles"
RESULTS_DIR = BASE_DIR / "results"
ANGLES_DIR = RESULTS_DIR / "angles"

if not DATA_DIR.is_dir():
    raise FileNotFoundError(f"Папка с данными не найдена: {DATA_DIR}")

ANGLES_DIR.mkdir(parents=True, exist_ok=True)

files = sorted(
    (
        file for file in DATA_DIR.iterdir()
        if file.is_file() and file.suffix == ".txt"
    ),
    key=lambda file: file.name
)

if not files:
    raise ValueError("В папке data/angles нет файлов .txt")

report_data = []

for file in files:
    if file.stat().st_size == 0:
        print(f"Предупреждение: файл {file.name} пуст.")
        continue

    try:
        angles_deg = np.loadtxt(file, ndmin=1)
    except ValueError as error:
        print(f"Ошибка чтения {file.name}: {error}")
        continue

    if angles_deg.ndim != 1 or angles_deg.size == 0:
        print(f"Предупреждение: некорректные данные в {file.name}.")
        continue

    if not np.all(np.isfinite(angles_deg)):
        print(f"Предупреждение: файл {file.name} содержит NaN или Inf.")
        continue

    angles_rad = np.radians(angles_deg)
    sin_vals = np.sin(angles_rad)
    cos_vals = np.cos(angles_rad)

    stem = file.stem

    np.savetxt(ANGLES_DIR / f"{stem}_sin.txt", sin_vals)
    np.savetxt(ANGLES_DIR / f"{stem}_cos.txt", cos_vals)

    max_angle = np.max(angles_deg)
    count_above_06 = int(np.sum(sin_vals > 0.6))

    report_data.append({
        "name": file.name,
        "max_angle": max_angle,
        "count_above": count_above_06
    })

    fig, ax = plt.subplots()

    x_dense_deg = np.linspace(0, 180, 500)
    x_dense_rad = np.radians(x_dense_deg)

    ax.plot(
        x_dense_deg,
        np.sin(x_dense_rad),
        label="sin(x)",
        color="tab:blue"
    )
    ax.plot(
        x_dense_deg,
        np.cos(x_dense_rad),
        label="cos(x)",
        color="tab:orange"
    )

    ax.scatter(
        angles_deg,
        sin_vals,
        color="tab:blue",
        edgecolor="black",
        zorder=3,
        label="sin (данные)"
    )
    ax.scatter(
        angles_deg,
        cos_vals,
        color="tab:orange",
        edgecolor="black",
        zorder=3,
        label="cos (данные)"
    )

    ax.set_title(f"Тригонометрия: {file.name}")
    ax.set_xlabel("Угол (градусы)")
    ax.set_ylabel("Значение")
    ax.set_xlim(0, 180)
    ax.grid(True)
    ax.legend()

    fig.tight_layout()
    fig.savefig(ANGLES_DIR / f"{stem}.png", dpi=150)
    plt.close(fig)

if not report_data:
    raise ValueError("Не удалось обработать ни один файл с углами")

best_file = max(report_data, key=lambda item: item["count_above"])

report_path = RESULTS_DIR / "angles_report.txt"

with report_path.open("w", encoding="utf-8") as report:
    report.write("Анализ тригонометрических данных\n")
    report.write("=" * 40 + "\n\n")

    for item in report_data:
        report.write(f"Файл: {item['name']}\n")
        report.write(f"Максимальный угол: {item['max_angle']:.1f}\n")
        report.write(f"Количество sin > 0.6: {item['count_above']}\n")
        report.write("-" * 40 + "\n")

    report.write("\nИтог:\n")
    report.write(
        f"Наибольшее количество значений sin > 0.6 "
        f"в файле: {best_file['name']} "
        f"({best_file['count_above']} шт.)\n"
    )

print("Обработка завершена!")
print(f"Отчёт сохранён в: {report_path}")
print(f"Графики и текстовые файлы сохранены в: {ANGLES_DIR}")
