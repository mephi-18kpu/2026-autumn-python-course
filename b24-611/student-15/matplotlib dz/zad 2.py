from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
root_dir = base_dir.parent.parent.parent
data_dir = root_dir / "code-examples" / "Модули и pathlib" / "data" / "angles"

results_dir = base_dir / "results" / "task2"
results_dir.mkdir(parents=True, exist_ok=True)

files = sorted(
    p for p in data_dir.iterdir()
    if p.is_file() and p.suffix == ".txt"
)

for file_path in files:
    angles_deg = np.loadtxt(file_path)
    angles_rad = np.radians(angles_deg)
    sin_vals = np.sin(angles_rad)
    cos_vals = np.cos(angles_rad)

    out_data = np.column_stack((angles_deg, sin_vals, cos_vals))
    out_file = results_dir / f"{file_path.stem}_results.txt"
    np.savetxt(out_file, out_data, fmt="%.4f", header="Angle_deg Sin Cos", comments="")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(angles_deg, sin_vals, label="sin(x)", marker="o")
    ax.plot(angles_deg, cos_vals, label="cos(x)", marker="s")

    ax.set_xlabel("Угол (градусы)")
    ax.set_ylabel("Значение")
    ax.set_title(f"Синус и косинус: {file_path.name}")
    ax.grid(True)
    ax.legend()

    plot_file = results_dir / f"{file_path.stem}_plot.png"
    fig.savefig(plot_file, dpi=150, bbox_inches="tight")
    plt.close(fig)
