import pandas as pd

df = pd.read_csv("observations.csv")

new_names = [
    "obs_id", "building", "location", "space_type", "posted_policy",
    "date", "day_of_week", "time", "occupancy_level", "noise_level",
    "group_solo", "head_count_min", "head_count_max", "minutes_to_record",
    "empty", "occupancy_notes", "noise_notes", "group_solo_notes",
]
if len(df.columns) != len(new_names):
    raise ValueError(f"Expected {len(new_names)} columns but found {len(df.columns)}")
df.columns = new_names
df = df.drop(columns="empty")

text_columns = ["building", "location", "space_type", "posted_policy","occupancy_notes", "noise_notes", "group_solo_notes"]
for col in text_columns:
    df[col] = df[col].fillna("").str.strip()

location_names = {
    "daley 2nd floor": "Daley 2nd Floor",
    "daley 4th floor": "Daley 4th Floor",
    "montgomery ward lounge": "Student Center Lounge",
    "2nd floor (lounge)": "CS Lounge",
    "2nd floor (office hour area)": "CS Office Hours",
}
space_types = {
    "Daley 2nd Floor": "Library",
    "Daley 4th Floor": "Library",
    "Student Center Lounge": "Lounge",
    "CS Lounge": "Lounge",
    "CS Office Hours": "Office Hour Area",
}

policy_names = {
    "quite zone": "Quiet zone",
    "quiet zone": "Quiet zone",
    "collaborative zone": "Collaborative zone",
    "no posted rule": "No posted rule",
}
df["location"] = df["location"].str.lower().map(location_names)
df["space_type"] = df["location"].map(space_types)
df["posted_policy"] = df["posted_policy"].str.lower().map(policy_names)
 
df["date"] = pd.to_datetime(df["date"])
df["day_of_week"] = df["date"].dt.day_name()

def make_24_hour(time_text):
    hour, minute = time_text.strip().split(":")
    hour = int(hour)
    if hour < 8:
        hour = hour + 12
    return f"{hour:02d}:{minute}"

df["time"] = df["time"].apply(make_24_hour)

df["head_count_mid"] = (df["head_count_min"] + df["head_count_max"]) / 2
df["when"] = pd.to_datetime(df["date"].dt.strftime("%Y-%m-%d") + " " + df["time"])
df = df.sort_values("when")
gap_is_big = df["when"].diff() > pd.Timedelta(minutes=45)
df["round"] = gap_is_big.cumsum() + 1

round_start = df.groupby("round")["when"].transform("min")
df["time_block"] = pd.cut(round_start.dt.hour, [0, 11, 14, 24], labels=["Morning", "Midday", "Afternoon"])
df = df.sort_values("obs_id")

if df[["location", "space_type", "posted_policy"]].isna().any().any():
    raise ValueError("A label was not recognized")
for col in ["occupancy_level", "noise_level", "group_solo"]:
    if not df[col].between(1, 5).all():
        raise ValueError(f"{col} has a value outside 1 to 5")
if (df["head_count_min"] > df["head_count_max"]).any():
    raise ValueError("A head count minimum is higher than its maximum")

df["date"] = df["date"].dt.strftime("%Y-%m-%d")
columns_to_keep = [
    "obs_id", "building", "location", "space_type", "posted_policy",
    "date", "day_of_week", "time", "round", "time_block",
    "occupancy_level", "noise_level", "group_solo",
    "head_count_min", "head_count_max", "head_count_mid", "minutes_to_record",
    "occupancy_notes", "noise_notes", "group_solo_notes",
]
df[columns_to_keep].to_csv("processed_data/observations_clean.csv", index=False)
print("Saved", len(df), "rows")
