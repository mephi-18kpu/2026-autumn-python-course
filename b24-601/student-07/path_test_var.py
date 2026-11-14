
from pathlib import Path

# Каталоги задаются относительно расположения этого .py-файла.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"

SUBDIRS = ("series", "angles")


def analyze_file(path: Path) -> dict:
    """Читает файл и собирает статистику по непустым строкам."""
    text = path.read_text(encoding="utf-8")

    nonempty_lines = [
        line for line in text.splitlines()
        if line.strip()
    ]

    return {
        "name": path.name,
        "path": path,
        "count": len(nonempty_lines),
        "first": nonempty_lines[0] if nonempty_lines else "",
        "last": nonempty_lines[-1] if nonempty_lines else "",
    }


def main() -> None:
    all_files = []
    directory_results = {}

    # Обрабатываем только обычные .txt-файлы.
    for dirname in SUBDIRS:
        directory = DATA_DIR / dirname
        file_results = []

        if directory.is_dir():
            for path in directory.iterdir():
                if not path.is_file():
                    continue
                if path.suffix.lower() != ".txt":
                    continue

                file_results.append(analyze_file(path))

        # Сортировка нужна, чтобы отчёт не зависел от порядка iterdir().
        file_results.sort(key=lambda item: item["name"])
        directory_results[dirname] = file_results
        all_files.extend(
            (dirname, item) for item in file_results
        )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    total_lines = sum(
        item["count"] for _, item in all_files
    )

    # Находим самый большой файл во всём наборе.
    # При равенстве выбираем по имени каталога и имени файла.
    largest = None
    if all_files:
        largest = min(
            all_files,
            key=lambda pair: (
                -pair[1]["count"],
                pair[0],
                pair[1]["name"],
            ),
        )

    report_lines = [
        "ОТЧЁТ ПО ТЕКСТОВЫМ ФАЙЛАМ",
        "=" * 40,
        "",
    ]

    # Отчёт по каждому каталогу и его файлам.
    for dirname in SUBDIRS:
        files = directory_results[dirname]

        report_lines.append(f"Каталог: data/{dirname}")
        report_lines.append("-" * 40)

        if not files:
            report_lines.append("Нет подходящих файлов.")
        else:
            for item in files:
                report_lines.extend([
                    f"Файл: {item['name']}",
                    f"Количество непустых строк: {item['count']}",
                    f"Первая непустая строка: {item['first'] or 'нет'}",
                    f"Последняя непустая строка: {item['last'] or 'нет'}",
                    "",
                ])

            # Победитель определяется по количеству строк,
            # а при равенстве — по имени файла.
            directory_largest = min(
                files,
                key=lambda item: (-item["count"], item["name"]),
            )

            report_lines.extend([
                "Файл с наибольшим количеством непустых строк "
                f"в каталоге: {directory_largest['name']}",
                f"Количество строк: {directory_largest['count']}",
            ])

        report_lines.append("")

    report_lines.extend([
        "=" * 40,
        f"Всего обработано файлов: {len(all_files)}",
        f"Всего непустых строк: {total_lines}",
    ])

    if largest is not None:
        largest_dir, largest_item = largest
        report_lines.extend([
            "Самый большой файл во всём наборе: "
            f"data/{largest_dir}/{largest_item['name']}",
            f"Количество непустых строк: {largest_item['count']}",
        ])

        # Сохраняем исходное содержимое, а не только непустые строки.
        original_text = largest_item["path"].read_text(
            encoding="utf-8"
        )
        (RESULTS_DIR / "largest_file.txt").write_text(
            original_text,
            encoding="utf-8",
        )
    else:
        report_lines.append(
            "Самый большой файл во всём наборе: нет файлов"
        )
        (RESULTS_DIR / "largest_file.txt").write_text(
            "",
            encoding="utf-8",
        )

    # Перезаписываем отчёт при каждом запуске.
    (RESULTS_DIR / "files_report.txt").write_text(
        "\n".join(report_lines) + "\n",
        encoding="utf-8",
    )

    print("Анализ завершён.")
    print(f"Отчёт: {RESULTS_DIR / 'files_report.txt'}")
    print(f"Самый большой файл: {RESULTS_DIR / 'largest_file.txt'}")


if __name__ == "__main__":
    main()
