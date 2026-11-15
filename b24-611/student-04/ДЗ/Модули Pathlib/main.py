"""Обзор файлов данных в каталогах data/series и data/angles."""

# System imports
from pathlib import Path

# External imports

# User imports

#############################################


BASE_DIR = Path(__file__).resolve().parent
DIRECTORIES = [
    BASE_DIR / "data" / "series",
    BASE_DIR / "data" / "angles",
]

RESULTS_DIR = BASE_DIR / "results"
REPORT_PATH = RESULTS_DIR / "files_report.txt"
LARGEST_PATH = RESULTS_DIR / "largest_file.txt"


def collect_txt_files(directory: Path) -> list[Path]:
    """Обычные .txt-файлы каталога в стабильном порядке."""
    files = [
        path
        for path in directory.iterdir()
        if path.is_file() and path.suffix.lower() == ".txt"
    ]
    return sorted(files, key=lambda path: path.name)


def analyze_file(path: Path) -> tuple[int, str | None, str | None]:
    """Кол-во непустых строк, первая и последняя непустая строка."""
    text = path.read_text(encoding="utf-8")
    non_empty = [line.strip() for line in text.splitlines() if line.strip()]

    if not non_empty:
        return 0, None, None
    return len(non_empty), non_empty[0], non_empty[-1]


def main() -> None:
    RESULTS_DIR.mkdir(exist_ok=True)

    report: list[str] = []
    report.append("Отчёт по файлам данных")
    report.append("=" * 25)

    total_non_empty = 0
    largest_count = -1
    largest_path: Path | None = None
    largest_text = ""

    for directory in DIRECTORIES:
        report.append("")
        report.append(f"Каталог: {directory.name}")

        files = collect_txt_files(directory)

        if not files:
            report.append("  .txt-файлы не найдены.")
            continue

        best_in_dir: tuple[int, Path] | None = None

        for path in files:
            count, first, last = analyze_file(path)
            total_non_empty += count

            report.append(f"  Файл: {path.name}")
            report.append(f"    Непустых строк: {count}")
            report.append(f"    Первая: {first if first is not None else '—'}")
            report.append(f"    Последняя: {last if last is not None else '—'}")

            # файл-максимум внутри каталога; при равенстве — меньший по имени
            if best_in_dir is None or count > best_in_dir[0] or (
                count == best_in_dir[0] and path.name < best_in_dir[1].name
            ):
                best_in_dir = (count, path)

            # файл-максимум по всем каталогам; при равенстве — меньший по имени
            if (
                count > largest_count
                or (
                    count == largest_count
                    and largest_path is not None
                    and path.name < largest_path.name
                )
                or (count == largest_count and largest_path is None)
            ):
                largest_count = count
                largest_path = path

        if best_in_dir is not None:
            best_count, best_path = best_in_dir
            report.append(
                f"  Максимум в каталоге: {best_path.name} ({best_count})"
            )

    report.append("")
    report.append("Общие итоги")
    report.append("-" * 12)
    report.append(f"Всего непустых строк: {total_non_empty}")

    if largest_path is not None:
        largest_text = largest_path.read_text(encoding="utf-8")
        report.append(
            f"Файл с максимумом строк: {largest_path.name} "
            f"({largest_count})"
        )
        report.append(f"Сохранён как: {LARGEST_PATH.name}")
    else:
        report.append("Подходящих файлов не найдено.")

    REPORT_PATH.write_text("\n".join(report) + "\n", encoding="utf-8")
    LARGEST_PATH.write_text(largest_text, encoding="utf-8")


if __name__ == "__main__":
    main()
