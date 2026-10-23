from pathlib import Path

if __name__ == "__main__":
    papka_skripta = Path(__file__).resolve().parent
    papka_series = papka_skripta / "data" / "series"
    papka_angles = papka_skripta / "data" / "angles"
    papka_results = papka_skripta / "results"

    papka_series.mkdir(parents=True, exist_ok=True)
    papka_angles.mkdir(parents=True, exist_ok=True)
    papka_results.mkdir(parents=True, exist_ok=True)

    if not list(papka_series.glob("*.txt")):
        (papka_series / "sensor_a.txt").write_text("10\n12\n\n15\n", encoding="utf-8")
        (papka_series / "sensor_b.txt").write_text("5\n5\n5\n", encoding="utf-8")
        (papka_series / "README.md").write_text("Описание данных", encoding="utf-8")

    if not list(papka_angles.glob("*.txt")):
        (papka_angles / "angles_1.txt").write_text("0\n30\n\n45\n90\n", encoding="utf-8")
        (papka_angles / "angles_2.txt").write_text("10\n50\n80\n120\n150\n180\n", encoding="utf-8")
        (papka_angles / "README.md").write_text("Описание данных", encoding="utf-8")

    stroki_otcheta = []
    obshchee_kolichestvo_strok = 0
    maks_strok_voobshche = -1
    fayl_maks_voobshche = None
    soderzhimoe_maks_fayla = ""

    katalogi_dlya_obhoda = [papka_series, papka_angles]

    for katalog in katalogi_dlya_obhoda:
        stroki_otcheta.append(f"=== Каталог: {katalog.name} ===")
        maks_strok_v_kataloge = -1
        fayl_maks_v_kataloge = ""

        fayly_txt = sorted([f for f in katalog.iterdir() if f.is_file() and f.suffix == ".txt"])

        for fayl in fayly_txt:
            tekst = fayl.read_text(encoding="utf-8")
            vse_stroki = tekst.splitlines()
            neputye_stroki = [s for s in vse_stroki if s.strip()]

            kolichestvo = len(neputye_stroki)
            pervaya = neputye_stroki[0] if kolichestvo > 0 else "—"
            poslednyaya = neputye_stroki[-1] if kolichestvo > 0 else "—"

            stroka_otcheta = (f"Файл: {fayl.name} | Непустых строк: {kolichestvo} | "
                              f"Первая: {pervaya} | Последняя: {poslednyaya}")
            stroki_otcheta.append(stroka_otcheta)

            obshchee_kolichestvo_strok += kolichestvo

            if kolichestvo > maks_strok_v_kataloge:
                maks_strok_v_kataloge = kolichestvo
                fayl_maks_v_kataloge = fayl.name

            if kolichestvo > maks_strok_voobshche:
                maks_strok_voobshche = kolichestvo
                fayl_maks_voobshche = fayl
                soderzhimoe_maks_fayla = tekst

        stroki_otcheta.append(f"Файл с наибольшим количеством строк в каталоге: {fayl_maks_v_kataloge}")
        stroki_otcheta.append("")

    stroki_otcheta.append("=== Общие результаты ===")
    stroki_otcheta.append(f"Общее количество непустых строк во всех файлах: {obshchee_kolichestvo_strok}")
    stroki_otcheta.append(f"Файл с наибольшим количеством строк: {fayl_maks_voobshche.name}")
    stroki_otcheta.append(f"Количество строк в нём: {maks_strok_voobshche}")

    put_otcheta = papka_results / "files_report.txt"
    put_otcheta.write_text("\n".join(stroki_otcheta), encoding="utf-8")

    if fayl_maks_voobshche is not None:
        put_bolshogo_fayla = papka_results / "largest_file.txt"
        put_bolshogo_fayla.write_text(soderzhimoe_maks_fayla, encoding="utf-8")

    print("Готово! Результаты сохранены в папке results.")
