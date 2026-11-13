import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(r"C:\Python\2026-autumn-python-course\code-examples\NumPy и Matplotlib")
data_dir = base_path / "data" / "angles"
results_dir = base_path / "results" / "angles"

results_dir.mkdir(exist_ok=True, parents=True)

txt_files = []
for file_path in data_dir.iterdir():
    if file_path.is_file() and file_path.suffix == ".txt":
        txt_files.append(file_path)

txt_files.sort()

report_text = ""
max_count_06 = -1
best_file = ""

for file_path in txt_files:
    angles_deg = np.loadtxt(file_path)

    angles_rad = np.radians(angles_deg)

    sin_vals = np.sin(angles_rad)
    cos_vals = np.cos(angles_rad)

    name_base = file_path.stem

    sin_path = results_dir / (name_base + "_sin.txt")
    cos_path = results_dir / (name_base + "_cos.txt")

    np.savetxt(sin_path, sin_vals)
    np.savetxt(cos_path, cos_vals)

    max_angle = np.max(angles_deg)

    count_greater = 0
    for val in sin_vals:
        if val > 0.6:
            count_greater = count_greater + 1

    if count_greater > max_count_06:
        max_count_06 = count_greater
        best_file = file_path.name

    report_text = report_text + "Файл: " + file_path.name + "\n"
    report_text = report_text + "  Максимальный угол: " + str(round(max_angle, 2)) + "\n"
    report_text = report_text + "  Количество синусов > 0.6: " + str(count_greater) + "\n"

    fig, ax = plt.subplots()

    x_dense_deg = np.linspace(0, 180, 300)  # 300 точек для плавных линий
    x_dense_rad = np.radians(x_dense_deg)

    ax.plot(x_dense_deg, np.sin(x_dense_rad), label="Синус (линия)")
    ax.plot(x_dense_deg, np.cos(x_dense_rad), label="Косинус (линия)")

    ax.scatter(angles_deg, sin_vals, color="red", label="Синус (точки)")
    ax.scatter(angles_deg, cos_vals, color="blue", label="Косинус (точки)")

    ax.set_xlabel("Угол (градусы)")
    ax.set_ylabel("Значение")
    ax.set_title("Тригонометрия: " + file_path.name)
    ax.grid(True)
    ax.legend()

    png_path = results_dir / (name_base + ".png")
    fig.savefig(png_path)

    plt.close(fig)

report_text = report_text + "\nРезультат:\n"
report_text = report_text + "Файл с наибольшим количеством синусов > 0.6: " + best_file + "\n"

report_file = open(results_dir / "report.txt", "w", encoding="utf-8")
report_file.write(report_text)
report_file.close()

print("Файлы сохранены в", results_dir)