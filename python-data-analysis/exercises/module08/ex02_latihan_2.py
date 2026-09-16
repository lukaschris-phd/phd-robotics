import pandas as pd

df = pd.DataFrame({
    "time": [0, 1, 2, 3, 4],
    "position": [0, 1, 4, 9, 16]
})

df["delta_position"] = df["position"].diff()
df["delta_time"] = df["time"].diff()
df["velocity"] = df["delta_position"] / df["delta_time"]

df["acceleration"] = df["velocity"].diff() / df["delta_time"]
print(df)