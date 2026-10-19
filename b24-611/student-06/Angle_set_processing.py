from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "angles"
OUTPUT_DIR = BASE_DIR / "results" / "angles"
REPORT_PATH = BASE_DIR / "results" / "angles_report.txt"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

report_lines = []
max_sin_count = -1
max_sin_file = ""

if not DATA_DIR.exists():
    print(f"Ошибка: Директория {DATA_DIR} не найдена.")
    exit(1)

for file_path in sorted(DATA_DIR.iterdir()):
    if file_path.is_file() and file_path.suffix == ".txt":

        try:
            angles_deg = np.loadtxt(file_path)
            if angles_deg.ndim == 0:
                angles_deg = np.array([angles_deg])
        except Exception as e:
            print(f"Не удалось прочитать файл {file_path.name}: {e}")
            continue

        if angles_deg.size == 0:
            continue

        angles_rad = np.radians(angles_deg)
        sin_values = np.sin(angles_rad)
        cos_values = np.cos(angles_rad)

        file_stem = file_path.stem
        sin_file_path = OUTPUT_DIR / f"{file_stem}_sin.txt"
        cos_file_path = OUTPUT_DIR / f"{file_stem}_cos.txt"

        np.savetxt(sin_file_path, sin_values, fmt="%.6f")
        np.savetxt(cos_file_path, cos_values, fmt="%.6f")

        max_angle = np.max(angles_deg)
        sin_above_count = int(np.sum(sin_values > 0.6))

        report_lines.append(
            f"Файл: {file_path.name}\n"
            f"  Наибольший угол: {max_angle:.2f}°\n"
            f"  Количество углов с синусом > 0.6: {sin_above_count}\n"
        )

        if sin_above_count > max_sin_count:
            max_sin_count = sin_above_count
            max_sin_file = file_path.name

with open(REPORT_PATH, "w", encoding="utf-8") as report_file:
    report_file.write("=== ОТЧЕТ ПО АНАЛИЗУ УГЛОВ ===\n\n")

    report_file.write("--- Результаты по каждому набору ---\n")
    for line in report_lines:
        report_file.write(line + "\n")

    report_file.write("--- Сводные результаты ---\n")
    if report_lines and max_sin_count >= 0:
        report_file.write(
            f"Файл, в котором нашлось больше всего углов с синусом > 0.6: {max_sin_file} "
            f"({max_sin_count} шт.)\n"
        )
    else:
        report_file.write("Нет данных для анализа.\n")

print(f"Обработка завершена. Результаты сохранены в {OUTPUT_DIR.relative_to(BASE_DIR)}, "
      f"а отчет — в {REPORT_PATH.relative_to(BASE_DIR)}")
