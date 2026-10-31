from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    data_dir = Path("data/angles")
    angles_results_dir = Path("results/angles")
    report_path = Path("results/angles_report.txt")

    angles_results_dir.mkdir(parents=True, exist_ok=True)

    txt_files = []
    if data_dir.exists():
        for file in data_dir.iterdir():
            if file.is_file() and file.suffix == '.txt':
                txt_files.append(file)

    txt_files.sort(key=lambda x: x.name)

    if not txt_files:
        print(f"В директории {data_dir} не найдено .txt файлов.")
        return

    max_sin_count = -1
    max_sin_count_file = ""

    report_lines = []

    grid_degrees = np.linspace(0, 180, 500)
    grid_radians = np.radians(grid_degrees)
    grid_sin = np.sin(grid_radians)
    grid_cos = np.cos(grid_radians)

    for file_path in txt_files:
        stem = file_path.stem

        angles_deg = np.loadtxt(file_path)

        if angles_deg.ndim == 0:
            angles_deg = np.array([angles_deg])

        angles_rad = np.radians(angles_deg)
        sin_values = np.sin(angles_rad)
        cos_values = np.cos(angles_rad)

        np.savetxt(angles_results_dir / f"{stem}_sin.txt", sin_values)
        np.savetxt(angles_results_dir / f"{stem}_cos.txt", cos_values)

        max_angle = np.max(angles_deg)
        count_sin_above_06 = np.sum(sin_values > 0.6)

        if count_sin_above_06 > max_sin_count:
            max_sin_count = count_sin_above_06
            max_sin_count_file = file_path.name

        report_lines.append(
            f"Файл: {file_path.name}\n"
            f"  Максимальный угол: {max_angle}°\n"
            f"  Количество значений sin > 0.6: {count_sin_above_06}\n"
            f"{'-' * 40}\n"
        )

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(grid_degrees, grid_sin, label="Идеальный sin(x)", color="blue", alpha=0.5, linestyle="--")
        ax.plot(grid_degrees, grid_cos, label="Идеальный cos(x)", color="red", alpha=0.5, linestyle="--")

        ax.scatter(angles_deg, sin_values, color="darkblue", zorder=3, label="Точки sin из файла")
        ax.scatter(angles_deg, cos_values, color="darkred", zorder=3, label="Точки cos из файла")

        ax.set_xlabel("Угол (в градусах)")
        ax.set_ylabel("Значение функции")
        ax.set_title(f"Анализ углов из файла: {file_path.name}")
        ax.set_xlim(0, 180)
        ax.set_ylim(-1.1, 1.1)
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.legend()

        plt.tight_layout()
        plt.savefig(angles_results_dir / f"{stem}.png", dpi=150)
        plt.close(fig)

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("Анализ углов и тригонометрических штук\n\n")
        f.writelines(report_lines)
        f.write("Сводные результаты\n")
        f.write(f"Файл с наибольшим числом значений sin > 0.6: {max_sin_count_file} ({max_sin_count} шт.)\n")

    print("Анализ углов окончен")
    print(f"Текстовый отчет сохранен в: {report_path}")
    print(f"Компоненты и графики сохранены в папку: {angles_results_dir}")

if __name__ == "__main__":
    main()
