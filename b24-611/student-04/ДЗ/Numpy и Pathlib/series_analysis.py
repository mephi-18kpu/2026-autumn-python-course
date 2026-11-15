"""Анализ серий измерений из каталога data/series."""

# System imports
from pathlib import Path

# External imports
import matplotlib
matplotlib.use("Agg")  # без GUI: только сохранение файлов
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "series"
RESULTS_DIR = BASE_DIR / "results"


def collect_txt_files(directory: Path) -> list[Path]:
    """Обычные .txt-файлы каталога в алфавитном порядке."""
    return sorted(
        (
            path
            for path in directory.iterdir()
            if path.is_file() and path.suffix.lower() == ".txt"
        ),
        key=lambda path: path.name,
    )


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    files = collect_txt_files(DATA_DIR)

    if not files:
        print("Нет .txt-файлов для обработки.")
        return

    report_lines = ["Отчёт по сериям измерений", "=" * 28, ""]

    best_mean_name = None
    best_mean_value = None
    best_std_name = None
    best_std_value = None

    fig, ax = plt.subplots(figsize=(8, 4))

    for path in files:
        raw = np.loadtxt(path)
        # np.loadtxt для одной строки вернёт 0-d массив — приводим к 1-d.
        values = np.atleast_1d(raw).astype(float)

        count = values.size
        minimum = float(np.min(values))
        maximum = float(np.max(values))
        mean = float(np.mean(values))
        std = float(np.std(values))
        above_mean = int(np.sum(values > mean))

        report_lines.append(f"Файл: {path.name}")
        report_lines.append(f"  Количество значений: {count}")
        report_lines.append(f"  Минимум: {minimum}")
        report_lines.append(f"  Максимум: {maximum}")
        report_lines.append(f"  Среднее: {mean:.6f}")
        report_lines.append(f"  Стандартное отклонение: {std:.6f}")
        report_lines.append(f"  Значений выше среднего: {above_mean}")
        report_lines.append("")

        # файл с наибольшим средним
        if best_mean_value is None or mean > best_mean_value:
            best_mean_value = mean
            best_mean_name = path.name

        # файл с наименьшим стандартным отклонением
        if best_std_value is None or std < best_std_value:
            best_std_value = std
            best_std_name = path.name

        # индексы под длину текущей серии
        indices = np.arange(values.size)
        ax.plot(
            indices,
            values,
            label=path.name,
            marker="o",
            markersize=3,
        )

    report_lines.append("Итоги")
    report_lines.append("-" * 6)
    report_lines.append(
        f"Наибольшее среднее: {best_mean_name} ({best_mean_value:.6f})"
    )
    report_lines.append(
        f"Наименьшее стандартное отклонение: "
        f"{best_std_name} ({best_std_value:.6f})"
    )

    report_path = RESULTS_DIR / "series_report.txt"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    ax.set_xlabel("Индекс элемента")
    ax.set_ylabel("Значение")
    ax.set_title("Сравнение серий измерений")
    ax.grid(True)
    ax.legend()

    image_path = RESULTS_DIR / "series.png"
    fig.savefig(image_path, dpi=150)
    plt.close(fig)

    print(f"Отчёт сохранён: {report_path}")
    print(f"График сохранён: {image_path}")


if __name__ == "__main__":
    main()
