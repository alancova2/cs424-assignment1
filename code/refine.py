import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

df = pd.read_csv("processed_data/observations_clean.csv")
os.makedirs("images", exist_ok=True)
 
spaces = ["Daley 4th Floor", "Daley 2nd Floor", "Student Center Lounge", "CS Lounge", "CS Office Hours"]
rules = {"Daley 4th Floor": "quiet zone", "Daley 2nd Floor": "collaborative zone"}
GOOD = "#009E73"
GRAY = "#aaaaaa"

limits = [2, 3, 4]
shades = ["#a8dccb", "#4fb89a", "#006b52"]
fig, ax = plt.subplots(figsize=(8, 4.5))
bar_height = 0.25
for k, limit in enumerate(limits):
    counts = []
    for space in spaces:
        d = df[df["location"] == space]
        counts.append(((d["noise_level"] <= 2) & (d["occupancy_level"] <= limit)).sum())
    y = [i + (k - 1) * bar_height for i in range(len(spaces))]
    ax.barh(y, counts, height=bar_height, color=shades[k],
            label=f"crowd {limit} or less" + (" (my first choice)" if limit == 3 else ""))
    for yy, c in zip(y, counts):
        ax.text(c + 0.08, yy, str(c), va="center", fontsize=8)
ax.set_yticks(range(len(spaces)))
ax.set_yticklabels(spaces)
ax.invert_yaxis()
ax.set_xlim(0, 6.6)
ax.set_xlabel("Visits that were a good bet (out of 6), noise 2 or less")
ax.legend(loc="center right", fontsize=8)
ax.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig("images/iteration1_crowd_limits.png", dpi=150)
plt.close()


fig, axes = plt.subplots(1, 5, figsize=(14, 3.6), sharex=True, sharey=True)
for ax, space in zip(axes, spaces):
    d = df[df["location"] == space]
    ax.add_patch(Rectangle((0.5, 0.5), 2, 3, color=GOOD, alpha=0.15))
    seen = {}
    xs, ys = [], []
    for row in d.itertuples():
        key = (row.noise_level, row.occupancy_level)
        seen[key] = seen.get(key, 0) + 1
        j = seen[key]
        xs.append(row.noise_level + ((j - 1) % 3 - 1) * 0.17)
        ys.append(row.occupancy_level + ((j - 1) // 3) * 0.17)
    inside = (d["noise_level"] <= 2) & (d["occupancy_level"] <= 3)
    ax.scatter(xs, ys, s=20 + d["head_count_mid"] * 1.6, c=[GOOD if g else GRAY for g in inside], edgecolor="black", linewidth=0.5, alpha=0.85)
    ax.set_title(f"{space}\n{rules.get(space, 'no posted rule')} · {inside.sum()} of 6 good", fontsize=9)
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
plt.tight_layout()
plt.savefig("images/iteration2_every_visit.png", dpi=150)
plt.close()
print("Saved 2 images in images/")
