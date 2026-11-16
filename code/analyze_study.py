import os
import pandas as pd
import matplotlib.pyplot as plt

COLORS = {"static": "#2a6fdb", "interactive": "#e07b00"}
ORDER = ["static", "interactive"]

df = pd.read_csv("study_data/results.csv")
df = df.dropna(subset=["correct", "time_seconds"])
df["correct"] = df["correct"].astype(int)
people = df["participant_id"].nunique()
print(f"{people} participants, {len(df)} answers\n")

print("Accuracy and time by version")
summary = df.groupby("condition").agg(
    accuracy=("correct", "mean"),
    mean_time=("time_seconds", "mean"),
    median_time=("time_seconds", "median"),
    n=("correct", "size"),
).reindex(ORDER)
print(summary.round(2), "\n")

print("By task")
by_task = df.groupby(["task", "condition"]).agg(
    accuracy=("correct", "mean"),
    median_time=("time_seconds", "median"),
    n=("correct", "size"),
).round(2)
print(by_task, "\n")

print("By which version came first")
print(df.groupby(["order", "condition"])["time_seconds"].mean().round(1).unstack(), "\n")

per = df.groupby(["participant_id", "condition"]).agg(
    accuracy=("correct", "mean"), time=("time_seconds", "mean")
).reset_index()
wide_t = per.pivot(index="participant_id", columns="condition", values="time").dropna()
wide_a = per.pivot(index="participant_id", columns="condition", values="accuracy").dropna()

try:
    from scipy.stats import wilcoxon
    for name, w in (("time", wide_t), ("accuracy", wide_a)):
        diff = w["interactive"] - w["static"]
        if (diff != 0).any():
            r = wilcoxon(w["interactive"], w["static"])
            print(f"Wilcoxon signed-rank on {name}: p = {r.pvalue:.3f} (n = {len(w)})")
        else:
            print(f"No difference in {name} for any participant.")
except ImportError:
    print("Install scipy (pip install scipy) to get p-values.")

os.makedirs("figures", exist_ok=True)
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

fig, ax = plt.subplots(figsize=(5, 4))
acc = summary["accuracy"] * 100
bars = ax.bar(ORDER, acc, color=[COLORS[c] for c in ORDER], width=0.5)
for b, v in zip(bars, acc):
    ax.text(b.get_x() + b.get_width() / 2, v + 2, f"{v:.0f}%", ha="center")
ax.set_ylim(0, 110)
ax.set_ylabel("Answers correct (%)")
ax.set_title("Accuracy by version")
fig.tight_layout()
fig.savefig("figures/study_accuracy.png", dpi=200)

fig, ax = plt.subplots(figsize=(5, 4))
for pid, row in wide_t.iterrows():
    ax.plot([0, 1], [row["static"], row["interactive"]], color="#999999", lw=1, zorder=1)
for i, c in enumerate(ORDER):
    ax.scatter([i] * len(wide_t), wide_t[c], color=COLORS[c], s=45, zorder=2)
    ax.hlines(wide_t[c].mean(), i - 0.2, i + 0.2, color="black", lw=2, zorder=3)
ax.set_xticks([0, 1])
ax.set_xticklabels(ORDER)
ax.set_xlim(-0.4, 1.4)
ax.set_ylim(0, None)
ax.set_ylabel("Average time per question (seconds)")
ax.set_title("Time by version (black line = average)")
fig.tight_layout()
fig.savefig("figures/study_time.png", dpi=200)
print("\nSaved figures/study_accuracy.png and figures/study_time.png")
