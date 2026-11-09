"""Вычисление синуса и косинуса для наборов углов из файлов."""

# System imports
from pathlib import Path

# External imports
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


lesson_directory = Path(__file__).resolve().parent
data_directory = lesson_directory / "data" / "angles"
results_directory = lesson_directory / "results"
angles_results_directory = results_directory / "angles"
angles_results_directory.mkdir(parents=True, exist_ok=True)

input_files = sorted(
    path for path in data_directory.iterdir()
    if path.is_file() and path.suffix == ".txt"
)

if not input_files:
    raise FileNotFoundError(f"В каталоге нет .txt-файлов: {data_directory}")

dense_angles = np.linspace(0, 180, 361)
dense_radians = np.deg2rad(dense_angles)
dense_sine = np.sin(dense_radians)
dense_cosine = np.cos(dense_radians)

report_lines = ["ОТЧЁТ ПО НАБОРАМ УГЛОВ", ""]
summary = []

for input_path in input_files:
    angles_degrees = np.loadtxt(input_path, dtype=float)
    angles_degrees = np.atleast_1d(angles_degrees)

    if angles_degrees.size == 0:
        raise ValueError(f"Файл не содержит углов: {input_path.name}")

    angles_radians = np.deg2rad(angles_degrees)
    sine_values = np.sin(angles_radians)
    cosine_values = np.cos(angles_radians)

    stem = input_path.stem
    np.savetxt(
        angles_results_directory / f"{stem}_sin.txt",
        sine_values,
        fmt="%.8f",
    )
    np.savetxt(
        angles_results_directory / f"{stem}_cos.txt",
        cosine_values,
        fmt="%.8f",
    )

    maximum_angle = float(np.max(angles_degrees))
    sine_above_threshold = int(np.count_nonzero(sine_values > 0.6))
    summary.append((input_path.name, maximum_angle, sine_above_threshold))

    report_lines.extend([
        f"Файл: {input_path.name}",
        f"Максимальный угол: {maximum_angle:g} градусов",
        f"Количество значений синуса строго больше 0.6: {sine_above_threshold}",
        "",
    ])

    fig, ax = plt.subplots()
    ax.plot(dense_angles, dense_sine, label="Синус")
    ax.plot(dense_angles, dense_cosine, label="Косинус")
    ax.scatter(angles_degrees, sine_values, label="Синус для углов из файла")
    ax.scatter(angles_degrees, cosine_values, label="Косинус для углов из файла")
    ax.set_xlabel("Угол, градусы")
    ax.set_ylabel("Значение функции")
    ax.set_title(f"Синус и косинус: {input_path.stem}")
    ax.grid(True)
    ax.legend()
    fig.savefig(angles_results_directory / f"{stem}.png", dpi=150)
    plt.close(fig)

highest_count_file, _, highest_count = max(
    summary,
    key=lambda item: item[2],
)
report_lines.extend([
    f"Наибольшее количество значений синуса > 0.6: {highest_count}",
    f"Файл с наибольшим количеством: {highest_count_file}",
])
(results_directory / "angles_report.txt").write_text(
    "\n".join(report_lines) + "\n",
    encoding="utf-8",
)

print(f"Обработано файлов: {len(summary)}")
print(f"Отчёт сохранён: {results_directory / 'angles_report.txt'}")
print(f"Графики и значения сохранены в: {angles_results_directory}")
