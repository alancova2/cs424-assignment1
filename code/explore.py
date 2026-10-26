import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("processed_data/observations_clean.csv")
os.makedirs("figures", exist_ok=True)

np.random.seed(424)
 
spaces = ["Daley 2nd Floor", "Daley 4th Floor", "Student Center Lounge",
          "CS Lounge", "CS Office Hours"]
space_colors = {
    "Daley 2nd Floor": "#D85A30",
    "Daley 4th Floor": "#0F6E56",
    "Student Center Lounge": "#534AB7",
    "CS Lounge": "#BA7517",
    "CS Office Hours": "#888780",
}

def jitter(values, amount):
    return np.array(values, dtype=float) + np.random.uniform(-amount, amount, len(values))

def add_legend(ax):
    dots = []
    for name in spaces:
        dots.append(plt.Line2D([], [], marker="o", linestyle="", color=space_colors[name], label=name))
    ax.legend(handles=dots, fontsize=8, frameon=False)

# Chart 1 noise vs group/solo with no jitter
fig, ax = plt.subplots(figsize=(6, 4.5))
for name in spaces:
    part = df[df["location"] == name]
    ax.scatter(part["group_solo"], part["noise_level"], color=space_colors[name], s=40)
ax.set_xlabel("Group/solo rating (1 = all solo, 5 = mostly groups)")
ax.set_ylabel("Noise level (1-5)")
ax.set_title("Noise vs. group mix (no jitter)")
add_legend(ax)
fig.tight_layout()
fig.savefig("figures/01_noise_vs_group_no_jitter.png", dpi=150)
plt.close(fig)

# Chart 2 same as chart 1 but with jitter
fig, ax = plt.subplots(figsize=(6, 4.5))
for name in spaces:
    part = df[df["location"] == name]
    x = jitter(part["group_solo"], 0.12)
    y = jitter(part["noise_level"], 0.12)
    ax.scatter(x, y, color=space_colors[name], s=45, alpha=0.8)
ax.set_xlabel("Group/solo rating (1 = all solo, 5 = mostly groups)")
ax.set_ylabel("Noise level (1-5)")
ax.set_title("Noise vs. group mix (jittered)")
add_legend(ax)
fig.tight_layout()
fig.savefig("figures/02_noise_vs_group_jitter.png", dpi=150)
plt.close(fig)

# Chart 3 noise with every visit
fig, ax = plt.subplots(figsize=(7, 4))
for i in range(len(spaces)):
    name = spaces[i]
    part = df[df["location"] == name]
    x = jitter([i] * len(part), 0.1)
    y = jitter(part["noise_level"], 0.08)
    ax.scatter(x, y, color=space_colors[name], s=45, alpha=0.8)
ax.set_xticks(range(len(spaces)))
ax.set_xticklabels([s.replace(" ", "\n", 1) for s in spaces], fontsize=8)
ax.set_ylabel("Noise level (1-5)")
ax.set_title("Noise level in each visit, by space")
fig.tight_layout()
fig.savefig("figures/03_noise_by_space.png", dpi=150)
plt.close(fig)

# Chart 4 head count vs my occupancy rating
fig, ax = plt.subplots(figsize=(6, 4.5))
for name in spaces:
    part = df[df["location"] == name]
    y = jitter(part["occupancy_level"], 0.08)
    ax.scatter(part["head_count_mid"], y, color=space_colors[name], s=45, alpha=0.8)
ax.set_xlabel("Head count (middle of my min-max estimate)")
ax.set_ylabel("Occupancy rating (1-5)")
ax.set_title("Same crowd, different rating?")
add_legend(ax)
fig.tight_layout()
fig.savefig("figures/04_headcount_vs_occupancy.png", dpi=150)
plt.close(fig)

# Chart 5 occupancy across the six rounds, one line per space
df["when"] = pd.to_datetime(df["date"] + " " + df["time"])
round_start = df.groupby("round")["when"].min()
round_labels = round_start.dt.strftime("%a\n%H:%M")
 
fig, ax = plt.subplots(figsize=(7, 4))
for name in spaces:
    part = df[df["location"] == name].sort_values("round")
    ax.plot(part["round"], part["occupancy_level"], marker="o", color=space_colors[name], label=name)
ax.set_xticks(round_labels.index)
ax.set_xticklabels(round_labels, fontsize=8)
ax.set_xlabel("Round (in time order, gaps are not to scale)")
ax.set_ylabel("Occupancy rating (1-5)")
ax.set_title("Occupancy by round")
ax.legend(loc="upper right", fontsize=6, frameon=False)
fig.tight_layout()
fig.savefig("figures/05_occupancy_by_round.png", dpi=150)
plt.close(fig)

# Chart 6 how many visits were a "good bet" for a quiet seat
df["good_bet"] = (df["noise_level"] <= 2) & (df["occupancy_level"] <= 3)
good_bets = df.groupby("location")["good_bet"].sum()
good_bets = good_bets.reindex(spaces)
 
fig, ax = plt.subplots(figsize=(7, 4))
bar_colors = [space_colors[s] for s in spaces]
ax.bar(range(len(spaces)), good_bets.values, color=bar_colors)
ax.set_xticks(range(len(spaces)))
ax.set_xticklabels([s.replace(" ", "\n", 1) for s in spaces], fontsize=8)
ax.set_ylim(0, 6)
ax.set_ylabel("Visits that were a good bet (out of 6)")
ax.set_title("Quiet (noise <= 2) and not too full (occupancy <= 3)")
fig.tight_layout()
fig.savefig("figures/06_good_bet_by_space.png", dpi=150)
plt.close(fig)

print("Saved 6 charts to the figures folder")
