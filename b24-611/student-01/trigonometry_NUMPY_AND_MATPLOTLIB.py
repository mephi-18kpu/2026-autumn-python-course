from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    papka_skripta = Path(__file__).resolve().parent
    papka_dannyh = papka_skripta / "data" / "angles"
    papka_rezultatov = papka_skripta / "results" / "angles"

    papka_dannyh.mkdir(parents=True, exist_ok=True)
    papka_rezultatov.mkdir(parents=True, exist_ok=True)

    if not list(papka_dannyh.glob("*.txt")):
        (papka_dannyh / "angles_1.txt").write_text("0\n30\n45\n90\n", encoding="utf-8")
        (papka_dannyh / "angles_2.txt").write_text("10\n50\n80\n120\n150\n180\n", encoding="utf-8")

    fayly_txt = sorted([f for f in papka_dannyh.iterdir() if f.is_file() and f.suffix == ".txt"])

    stroki_otcheta = []
    maks_kolichestvo = -1
    imya_maks_kolichestva = ""

    for fayl in fayly_txt:
        ugol_gradusy = np.loadtxt(fayl)
        ugol_radiany = np.deg2rad(ugol_gradusy)

        sinus = np.sin(ugol_radiany)
        kosinus = np.cos(ugol_radiany)

        imya_bazovoe = fayl.stem

        put_sinus = papka_rezultatov / f"{imya_bazovoe}_sin.txt"
        put_kosinus = papka_rezultatov / f"{imya_bazovoe}_cos.txt"

        np.savetxt(put_sinus, sinus, fmt="%.4f")
        np.savetxt(put_kosinus, kosinus, fmt="%.4f")

        maks_ugol = np.max(ugol_gradusy)
        kolichestvo_bolshe = np.sum(sinus > 0.6)

        stroka = (f"Файл: {fayl.name} | Макс. угол: {maks_ugol:.1f}° | "
                  f"Кол-во sin > 0.6: {kolichestvo_bolshe}")
        stroki_otcheta.append(stroka)

        if kolichestvo_bolshe > maks_kolichestvo:
            maks_kolichestvo = kolichestvo_bolshe
            imya_maks_kolichestva = fayl.name

        fig, ax = plt.subplots(figsize=(8, 4))

        setka_gradusov = np.linspace(0, 180, 181)
        setka_radianov = np.deg2rad(setka_gradusov)

        ax.plot(setka_gradusov, np.sin(setka_radianov), label="Синус (теория)", color="tab:blue")
        ax.plot(setka_gradusov, np.cos(setka_radianov), label="Косинус (теория)", color="tab:orange")

        ax.scatter(ugol_gradusy, sinus, label="Синус (измерения)", color="darkblue", zorder=5)
        ax.scatter(ugol_gradusy, kosinus, label="Косинус (измерения)", color="darkred", zorder=5)

        ax.set_xlabel("Угол, градусы")
        ax.set_ylabel("Значение функции")
        ax.set_title(f"Тригонометрия: {fayl.name}")
        ax.grid(True)
        ax.legend()

        put_grafika = papka_rezultatov / f"{imya_bazovoe}.png"
        fig.savefig(put_grafika, dpi=150)
        plt.close(fig)

    stroki_otcheta.append("")
    stroki_otcheta.append(f"Файл с наибольшим количеством sin > 0.6: {imya_maks_kolichestva}")

    put_otcheta = papka_skripta / "results" / "angles_report.txt"
    put_otcheta.write_text("\n".join(stroki_otcheta), encoding="utf-8")
