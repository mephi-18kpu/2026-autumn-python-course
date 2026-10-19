from pathlib import Path
def main() -> None:
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    results_dir = base_dir / "results"
    results_dir.mkdir(exist_ok=True)
    target_dirs = [data_dir / "series", data_dir / "angles"]
    report_lines = []
    total_lines_all = 0

    absolute_largest_file = None
    absolute_largest_count = -1
    absolute_largest_content = ""

    for dir_path in target_dirs:
        if not dir_path.is_dir():
            continue

        report_lines.append(f"Каталог: {dir_path.name}")

        files = sorted([
            p for p in dir_path.iterdir()
            if p.is_file() and p.suffix.lower() == ".txt" and p.name.lower() != "readme.md"
        ])

        dir_largest_file = None
        dir_largest_count = -1

        for file_path in files:
            text = file_path.read_text(encoding="utf-8")

            non_empty_lines = [line.strip() for line in text.splitlines() if line.strip()]
            count = len(non_empty_lines)
            total_lines_all += count

            first_line = non_empty_lines[0] if count > 0 else "нет"
            last_line = non_empty_lines[-1] if count > 0 else "нет"

            report_lines.append(f"Файл: {file_path.name}")
            report_lines.append(f"Непустых строк: {count}")
            report_lines.append(f"Первая строка: {first_line}")
            report_lines.append(f"Последняя строка: {last_line}")

            if count > dir_largest_count:
                dir_largest_count = count
                dir_largest_file = file_path

            if count > absolute_largest_count:
                absolute_largest_count = count
                absolute_largest_file = file_path
                absolute_largest_content = text

        if dir_largest_file:
            report_lines.append(
                f"Самый большой файл в каталоге {dir_path.name}: "
                f"{dir_largest_file.name} ({dir_largest_count} строк)\n"
            )
        else:
            report_lines.append(f"В каталоге {dir_path.name} нет подходящих файлов.\n")

    report_lines.append(f"Общее количество непустых строк: {total_lines_all}")
    if absolute_largest_file:
        report_lines.append(
            f"Самый большой файл во всём наборе: {absolute_largest_file.name} "
            f"({absolute_largest_count} строк)"
        )

    report_path = results_dir / "files_report.txt"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    if absolute_largest_file:
        largest_path = results_dir / "largest_file.txt"
        largest_path.write_text(absolute_largest_content, encoding="utf-8")

    print("Анализ файлов успешно завершён. Результаты сохранены в папку 'results'.")


if __name__ == "__main__":
    main()
