from pathlib import Path

import matplotlib

# Use a non-interactive backend so the script works in terminal-only environments.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def generate_bar_chart() -> Path:
    categories = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    values = [120, 150, 90, 180, 160]

    output_dir = Path(__file__).resolve().parents[1] / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "sales_bar_chart.png"

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(categories, values, color=["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F"])

    ax.set_title("Weekly Sales")
    ax.set_xlabel("Day")
    ax.set_ylabel("Amount")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f"{int(height)}", ha="center", va="bottom")

    fig.tight_layout()
    fig.savefig(output_file, dpi=150)
    plt.close(fig)
    return output_file


def main() -> None:
    output_file = generate_bar_chart()
    print(f"Bar chart saved to: {output_file}")


if __name__ == "__main__":
    main()
