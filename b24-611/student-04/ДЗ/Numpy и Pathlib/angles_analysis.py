"""Анализ углов из data/angles: синусы, косинусы, графики."""

# System imports
from pathlib import Path

# External imports
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# User imports

#############################################


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "angles"
RESULTS_DIR = BASE_DIR / "results"
ANGLES_RESULTS_DIR = RESULTS_DIR / "angles"


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
    ANGLES_RESULTS_DIR.mkdir(exist_ok=True)

    files = collect_txt_files(DATA_DIR)
    if not files:
        print("Нет .txt-файлов для обработки.")
        return

    report_lines = ["Отчёт по углам", "=" * 15, ""]

    best_count_name = None
    best_count_value = None

    # Плотная сетка для гладких кривых — считается один раз.
    dense_angles = np.linspace(0, 180, 181)
    dense_radians = np.deg2rad(dense_angles)
    dense_sin = np.sin(dense_radians)
    dense_cos = np.cos(dense_radians)

    for path in files:
        raw = np.loadtxt(path)
        angles = np.atleast_1d(raw).astype(float)
        radians = np.deg2rad(angles)
        sin_values = np.sin(radians)
        cos_values = np.cos(radians)

        stem = path.stem
        np.savetxt(
            ANGLES_RESULTS_DIR / f"{stem}_sin.txt",
            sin_values,
            fmt="%.6f",
        )
        np.savetxt(
            ANGLES_RESULTS_DIR / f"{stem}_cos.txt",
            cos_values,
            fmt="%.6f",
        )

        max_angle = float(np.max(angles))
        count_sin_above = int(np.sum(sin_values > 0.6))

        report_lines.append(f"Файл: {path.name}")
        report_lines.append(f"  Максимальный угол: {max_angle}")
        report_lines.append(f"  Значений sin > 0.6: {count_sin_above}")
        report_lines.append("")

        if best_count_value is None or count_sin_above > best_count_value:
            best_count_value = count_sin_above
            best_count_name = path.name

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(dense_angles, dense_sin, label="sin", color="tab:blue")
        ax.plot(dense_angles, dense_cos, label="cos", color="tab:orange")
        ax.scatter(
            angles,
            sin_values,
            color="tab:blue",
            zorder=3,
            label="sin (точки файла)",
        )
        ax.scatter(
            angles,
            cos_values,
            color="tab:orange",
            zorder=3,
            label="cos (точки файла)",
        )
        ax.set_xlabel("Угол, градусы")
        ax.set_ylabel("Значение функции")
        ax.set_title(f"Тригонометрия: {path.name}")
        ax.grid(True)
        ax.legend()

        fig.savefig(ANGLES_RESULTS_DIR / f"{stem}.png", dpi=150)
        plt.close(fig)

    report_lines.append("Итоги")
    report_lines.append("-" * 6)
    if best_count_name is not None:
        report_lines.append(
            f"Наибольшее число значений sin > 0.6: "
            f"{best_count_name} ({best_count_value})"
        )
    else:
        report_lines.append("Подходящих файлов нет.")

    report_path = RESULTS_DIR / "angles_report.txt"
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"Отчёт сохранён: {report_path}")
    print(f"Файлы сохранены в: {ANGLES_RESULTS_DIR}")


if __name__ == "__main__":
    main()
