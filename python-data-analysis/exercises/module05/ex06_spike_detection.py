import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

spike_threshold = 30

df["change"] = df["distance"].diff()
df["abs_change"] = df["change"].abs()

mask = df["abs_change"] <= spike_threshold

fig, ax = plt.subplots(
    3, 1, 
    figsize=(10, 7), 
    sharex = True
)

ax[0].plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Distance"
)

ax[1].plot(
    df["timestamp"],
    df["change"],
    marker="o",
)

ax[0].set_ylabel("Distance Readings")
ax[0].grid(True)

ax[1].set_ylabel("Change")
ax[1].grid(True)

ax[2].set_xlabel("Time (s)")
ax[2].set_ylabel("Absolute Change")
ax[2].grid(True)

ax[2].scatter(
    df.loc[mask, "timestamp"],
    df.loc[mask, "abs_change"],
    color="red",
    marker="x",
    label="Spike"
)

plt.show()