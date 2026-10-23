from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    papka_skripta = Path(__file__).resolve().parent
    papka_dannyh = papka_skripta / "data" / "series"
    papka_rezultatov = papka_skripta / "results"

    papka_dannyh.mkdir(parents=True, exist_ok=True)
    papka_rezultatov.mkdir(parents=True, exist_ok=True)

    if not list(papka_dannyh.glob("*.txt")):
        (papka_dannyh / "series_1.txt").write_text("10\n12\n15\n", encoding="utf-8")
        (papka_dannyh / "series_2.txt").write_text("5\n5\n5\n5\n5\n", encoding="utf-8")
        (papka_dannyh / "series_3.txt").write_text("100\n20\n30\n40\n", encoding="utf-8")

    fayly_txt = sorted([f for f in papka_dannyh.iterdir() if f.is_file() and f.suffix == ".txt"])

    dannye_seriy = {}
    stroki_otcheta = []

    maks_srednee = -float("inf")
    imya_maks_srednee = ""
    min_otklonenie = float("inf")
    imya_min_otklonenie = ""

    for fayl in fayly_txt:
        znacheniya = np.loadtxt(fayl)
        kolichestvo = len(znacheniya)

        if kolichestvo == 0:
            continue

        minimum = np.min(znacheniya)
        maksimum = np.max(znacheniya)
        srednee = np.mean(znacheniya)
        otklonenie = np.std(znacheniya)

        vyshe_srednego = np.sum(znacheniya > srednee)

        dannye_seriy[fayl.name] = znacheniya

        stroka = (f"Файл: {fayl.name} | Кол-во: {kolichestvo} | "
                  f"Мин: {minimum:.2f} | Макс: {maksimum:.2f} | "
                  f"Среднее: {srednee:.2f} | Отклонение: {otklonenie:.2f} | "
                  f"Выше среднего: {vyshe_srednego}")
        stroki_otcheta.append(stroka)

        if srednee > maks_srednee:
            maks_srednee = srednee
            imya_maks_srednee = fayl.name

        if otklonenie < min_otklonenie:
            min_otklonenie = otklonenie
            imya_min_otklonenie = fayl.name

    stroki_otcheta.append("")
    stroki_otcheta.append(f"Наибольшее среднее: {imya_maks_srednee}")
    stroki_otcheta.append(f"Наименьшее стандартное отклонение: {imya_min_otklonenie}")

    put_otcheta = papka_rezultatov / "series_report.txt"
    put_otcheta.write_text("\n".join(stroki_otcheta), encoding="utf-8")

    fig, ax = plt.subplots(figsize=(8, 4))

    for imya_fayla, znacheniya in dannye_seriy.items():
        indeksy = np.arange(len(znacheniya))
        ax.plot(indeksy, znacheniya, label=imya_fayla, marker="o", markersize=4)

    ax.set_xlabel("Индекс элемента")
    ax.set_ylabel("Значение")
    ax.set_title("Сравнение серий измерений")
    ax.grid(True)
    ax.legend()

    fig.savefig(papka_rezultatov / "series.png", dpi=150)
    plt.show()
