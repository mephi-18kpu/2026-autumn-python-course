from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

base_dir = Path(__file__).resolve().parent
angles_dir = base_dir.parent / "hw3" / "data" / "angles"
results_dir = base_dir / "results" / "angles"
results_dir.mkdir(parents=True, exist_ok=True)

files = sorted([p for p in angles_dir.iterdir() if p.suffix == ".txt" and p.name != "README.md"])

report = []
max_file, max_count = "", -1

curve = np.linspace(0, 180, 181)
rad = np.deg2rad(curve)
sin_c, cos_c = np.sin(rad), np.cos(rad)

for f in files:
    deg = np.loadtxt(f)
    r = np.deg2rad(deg)
    sin_v, cos_v = np.sin(r), np.cos(r)

    np.savetxt(results_dir / f"{f.stem}_sin.txt", sin_v, fmt="%.6f")
    np.savetxt(results_dir / f"{f.stem}_cos.txt", cos_v, fmt="%.6f")

    gt_06 = np.sum(sin_v > 0.6)
    report.append(f"Файл: {f.name}\n  • Макс. угол: {np.max(deg) if deg.size else 0}\n  • sin > 0.6: {gt_06}\n")

    if gt_06 > max_count:
        max_count, max_file = gt_06, f.name

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(curve, sin_c, label="sin (теор)", color="tab:blue")
    ax.plot(curve, cos_c, label="cos (теор)", color="tab:orange")
    ax.scatter(deg, sin_v, label="sin (файл)", color="tab:red", zorder=5)
    ax.scatter(deg, cos_v, label="cos (файл)", color="tab:purple", zorder=5)

    ax.set_title(f"Тригонометрия: {f.stem}")
    ax.grid(True)
    ax.legend()
    fig.savefig(results_dir / f"{f.stem}.png", dpi=150)
    plt.close(fig)

report.append(f"Итоги:\nБольше всего sin > 0.6 в файле: {max_file} ({max_count})")
(base_dir / "results" / "angles_report.txt").write_text("\n".join(report), encoding="utf-8")
