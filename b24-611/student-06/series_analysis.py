from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def main():
    data_dir = Path("data/series")
    results_dir = Path("results")

    results_dir.mkdir(parents=True, exist_ok=True)

    txt_files = []
    if data_dir.exists():
        for file in data_dir.iterdir():
            if file.is_file() and file.suffix == '.txt' and file.name != 'README.md':
                txt_files.append(file)

    txt_files.sort(key=lambda x: x.name)

    if not txt_files:
        print(f"В директории {data_dir} не найдено подходящих .txt файлов.")
        return

    max_mean = -float('inf')
    max_mean_file = ""

    min_std = float('inf')
    min_std_file = ""

    individual_reports = []

    fig, ax = plt.subplots(figsize=(10, 6))

    for file_path in txt_files:
        data = np.loadtxt(file_path)
        if data.ndim == 0:
            data = np.array([data])

        count = len(data)
        vmin = np.min(data)
        vmax = np.max(data)
        vmean = np.mean(data)
        vstd = np.std(data)
        above_mean_count = np.sum(data > vmean)

        if vmean > max_mean:
            max_mean = vmean
            max_mean_file = file_path.name

        if vstd < min_std:
            min_std = vstd
            min_std_file = file_path.name

        file_report = (
            f"Файл: {file_path.name}\n"
            f"  Количество значений: {count}\n"
            f"  Минимум: {vmin}\n"
            f"  Максимум: {vmax}\n"
            f"  Среднее значение: {vmean:.4f}\n"
            f"  Стандартное отклонение: {vstd:.4f}\n"
            f"  Количество значений выше среднего: {above_mean_count}\n"
            f"{'-' * 40}\n"
        )
        individual_reports.append(file_report)
        x_indices = np.arange(count)
        ax.plot(x_indices, data, label=file_path.name)
    report_path = results_dir / "series_report.txt"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("Анализ серий данных\n\n")
        f.writelines(individual_reports)
        f.write("Сводные результаты\n")
        f.write(f"Наибольшее среднее значение: {max_mean:.4f} (Файл: {max_mean_file})\n")
        f.write(f"Наименьшее стандартное отклонение: {min_std:.4f} (Файл: {min_std_file})\n")

    ax.set_xlabel("Индекс элемента")
    ax.set_ylabel("Значение")
    ax.set_title("Графики серий данных")
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend()

    image_path = results_dir / "series.png"
    plt.tight_layout()
    plt.savefig(image_path, dpi=150)
    plt.close(fig)

    print(f"Анализ успешно завершен!")
    print(f"Отчет сохранен в: {report_path}")
    print(f"График сохранен в: {image_path}")

if __name__ == "__main__":
    main()
