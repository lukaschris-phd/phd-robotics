import pandas as pd

df = pd.DataFrame({
    "time": [0.0, 0.1, 0.2, 0.3, 0.4],
    "gz": [0.0, 10.0, 10.0, 10.0, 0.0]
})

df["dt"] = df["time"].diff().fillna(0)

df["delta_angle"] = (
    df["gz"] * df["dt"]
)

df["angle"] = df["delta_angle"].cumsum()

print("angle:", df["angle"])