import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Good bet for a quiet seat", layout="wide")
df = pd.read_csv("processed_data/observations_clean.csv")
 
spaces = ["Daley 4th Floor", "Daley 2nd Floor", "Student Center Lounge", "CS Lounge", "CS Office Hours"]

colors = {
    "Daley 4th Floor": "#0072B2",
    "Daley 2nd Floor": "#D55E00",
    "Student Center Lounge": "#009E73",
    "CS Lounge": "#CC79A7",
    "CS Office Hours": "#E69F00",
    "Other spaces": "#cccccc",
}

st.sidebar.header("Your limits")
max_noise = st.sidebar.slider("Most noise I will put up with", 1, 5, 2)
max_crowd = st.sidebar.slider("Most crowding I will put up with", 1, 5, 3)
 
st.sidebar.header("Highlight")
focus = st.sidebar.selectbox("Pick a space to highlight in every chart", ["None"] + spaces)

df["good"] = (df["noise_level"] <= max_noise) & (df["occupancy_level"] <= max_crowd)

def color_name(space):
    if focus == "None" or space == focus:
        return space
    return "Other spaces"
 
df["color_name"] = df["location"].apply(color_name)

def split_lines(text):
    words = str(text).split()
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) > 45:
            lines.append(line)
            line = ""
        line = line + word + " "
    lines.append(line)
    return "<br>".join(lines)
 
hover_text = []
for i, row in df.iterrows():
    text = "<b>" + row["location"] + "</b><br>"
    text += row["day_of_week"] + " " + row["date"] + " " + row["time"] + "<br>"
    text += "about " + str(round(row["head_count_mid"])) + " people<br>"
    text += "Crowd " + str(row["occupancy_level"]) + ", noise " + str(row["noise_level"]) + "<br>"
    text += "Crowd: " + split_lines(row["occupancy_notes"]) + "<br>"
    text += "Noise: " + split_lines(row["noise_notes"])
    hover_text.append(text)
df["hover_text"] = hover_text

rounds = df.groupby("round").agg(day=("day_of_week", "first"), start=("time", "min"))
round_names = {}
for number, row in rounds.iterrows():
    round_names[number] = row["day"][:3] + " " + row["start"]
df["round_label"] = df["round"].map(round_names)
round_order = [round_names[n] for n in sorted(round_names)]
 
st.title("Where is a good bet for a quiet seat?")
st.write("A visit is a good bet if its noise and crowd scores (1 to 5) are both at or under your limits. "
         "Move the sliders to change the bars. Hover over a dot to read my notes.")

counts = df.groupby("location")["good"].sum().reindex(spaces).reset_index()
counts["color_name"] = counts["location"].apply(color_name)
 
bars = px.bar(counts, x="good", y="location", orientation="h", color="color_name", color_discrete_map=colors, text="good", category_orders={"location": spaces})
bars.update_traces(hovertemplate="%{y}: %{x} of 6 visits<extra></extra>")
bars.update_layout(showlegend=False, xaxis_title="Visits that were a good bet (out of 6)", yaxis_title="", xaxis_range=[0, 6.5], height=300, margin=dict(t=30))
bars.update_yaxes(autorange="reversed")
 
st.subheader("Which space is a good bet?")
st.plotly_chart(bars, width="stretch")
 
left, right = st.columns(2)

rng = np.random.default_rng(1)
df["x_spot"] = df["group_solo"] + rng.uniform(-0.12, 0.12, len(df))
df["y_spot"] = df["noise_level"] + rng.uniform(-0.12, 0.12, len(df))
 
dots = px.scatter(df, x="x_spot", y="y_spot", size="head_count_mid", color="color_name", color_discrete_map=colors, custom_data=["hover_text"])
dots.update_traces(hovertemplate="%{customdata[0]}<extra></extra>")
dots.update_layout(xaxis_title="Solo (1) to groups (5)", yaxis_title="Noise (1 to 5)", legend_title="")
dots.update_xaxes(tickvals=[1, 2, 3, 4, 5], range=[0.5, 5.5])
dots.update_yaxes(tickvals=[1, 2, 3, 4, 5], range=[0.5, 5.5])
 
left.subheader("Noise and group mix")
left.plotly_chart(dots, width="stretch")

df["line_name"] = df["location"] + " " + df["day_of_week"]
df = df.sort_values("round")
 
lines = px.line(df, x="round_label", y="occupancy_level", color="color_name", line_group="line_name", markers=True, color_discrete_map=colors, custom_data=["hover_text"], category_orders={"round_label": round_order})
lines.update_traces(hovertemplate="%{customdata[0]}<extra></extra>")
lines.update_layout(xaxis_title="Round of visits", yaxis_title="Crowd (1 to 5)", legend_title="")
lines.update_yaxes(tickvals=[1, 2, 3, 4, 5], range=[0.5, 5.5])
 
right.subheader("Crowd over the day")
right.plotly_chart(lines, width="stretch")
