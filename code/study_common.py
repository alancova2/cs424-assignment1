import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

SPACES = ["Daley 4th Floor", "Daley 2nd Floor", "Student Center Lounge", "CS Lounge", "CS Office Hours"]
SHORT = ["Daley 4th", "Daley 2nd", "Student Ctr", "CS Lounge", "CS Office"]
RULES = {"Daley 4th Floor": "quiet zone", "Daley 2nd Floor": "collaborative zone"}
GREEN = "#009E73"
GRAY = "#8a8a8a"


def load_data():
    return pd.read_csv("processed_data/observations_clean.csv")


def good_counts(df, noise_limit, crowd_limit):
    """How many of the 6 visits to each space had noise and crowd at or under the limits."""
    counts = []
    for space in SPACES:
        d = df[df["location"] == space]
        good = (d["noise_level"] <= noise_limit) & (d["occupancy_level"] <= crowd_limit)
        counts.append(int(good.sum()))
    return counts


def draw_bars(ax, counts, title, fontsize=8):
    """Horizontal bars, one for each space, with the count written at the end."""
    ax.barh(range(5), counts, color=GREEN)
    for i, c in enumerate(counts):
        ax.text(c + 0.1, i, str(c), va="center", fontsize=fontsize)
    ax.set_yticks(range(5))
    ax.set_yticklabels(SHORT, fontsize=fontsize)
    ax.invert_yaxis()
    ax.set_xlim(0, 7)
    ax.set_xticks([0, 2, 4, 6])
    ax.tick_params(axis="x", labelsize=fontsize)
    ax.set_title(title, fontsize=fontsize + 1)


def dot_panels(df, noise_limit=None, crowd_limit=None):
    """One small chart for each space with a dot for every visit.
    Noise is across, crowd is up, and dot size is the head count.
    If limits are given, a green box is drawn and dots inside it turn green."""
    fig, axes = plt.subplots(1, 5, figsize=(14, 3.4), sharex=True, sharey=True)
    for ax, space in zip(axes, SPACES):
        d = df[df["location"] == space]
        if noise_limit is not None:
            ax.add_patch(Rectangle((0.5, 0.5), noise_limit, crowd_limit, color=GREEN, alpha=0.15))
        seen = {}
        xs, ys, colors = [], [], []
        for row in d.itertuples():
            key = (row.noise_level, row.occupancy_level)
            seen[key] = seen.get(key, 0) + 1
            j = seen[key]
            xs.append(row.noise_level + ((j - 1) % 3 - 1) * 0.17)
            ys.append(row.occupancy_level + ((j - 1) // 3) * 0.17)
            inside = row.noise_level <= (noise_limit or 0) and row.occupancy_level <= (crowd_limit or 0)
            colors.append(GREEN if inside else GRAY)
        ax.scatter(xs, ys, s=20 + d["head_count_mid"] * 1.6, c=colors,
                   edgecolor="black", linewidth=0.5, alpha=0.85)
        ax.set_title(f"{space}\n{RULES.get(space, 'no posted rule')}", fontsize=9)
        ax.set_xlim(0.5, 5.5)
        ax.set_ylim(0.5, 5.5)
        ax.set_xticks(range(1, 6))
        ax.set_yticks(range(1, 6))
        ax.grid(alpha=0.3)
        ax.set_xlabel("Noise (1 to 5)")
    axes[0].set_ylabel("Crowd (1 to 5)")
    for people in [10, 50, 150]:
        axes[-1].scatter([], [], s=20 + people * 1.6, c="white", edgecolor="black", label=f"{people} people")
    axes[-1].legend(loc="upper left", fontsize=7, labelspacing=1.2, borderpad=0.8)
    fig.tight_layout()
    return fig


def limits_grid(df):
    """The static version's answer to the sliders: good bet counts for every
    combination of noise limit (rows) and crowd limit (columns) that the tasks can use."""
    fig, axes = plt.subplots(3, 3, figsize=(11, 8), sharex=True)
    for r, noise_limit in enumerate([1, 2, 3]):
        for c, crowd_limit in enumerate([2, 3, 4]):
            draw_bars(axes[r][c], good_counts(df, noise_limit, crowd_limit), f"Noise {noise_limit} or less, crowd {crowd_limit} or less")
    fig.tight_layout()
    return fig
