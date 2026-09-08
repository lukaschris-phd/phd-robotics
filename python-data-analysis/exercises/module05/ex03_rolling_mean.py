import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

df["distance_rolling_mean3"] = (
    df["distance"]
    .rolling(
        window=3,
        min_periods=1
    )
    .mean()
)

df["distance_rolling_mean5"] = (
    df["distance"]
    .rolling(
        window=5,
        min_periods=1
    )
    .mean()
)

df["distance_rolling_mean7"] = (
    df["distance"]
    .rolling(
        window=7,
        min_periods=1
    )
    .mean()
)

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Raw Distance"
)
ax.plot(
    df["timestamp"],
    df["distance_rolling_mean3"],
    marker="o",
    label="Rolling Mean Distance Window = 3"
)
ax.plot(
    df["timestamp"],
    df["distance_rolling_mean5"],
    marker="o",
    label="Rolling Mean Distance Window = 5"
)
ax.plot(
    df["timestamp"],
    df["distance_rolling_mean7"],
    marker="o",
    label="Rolling Mean Distance Window = 7"
)

ax.set_xlabel("Time (s)")
ax.set_ylabel("Value")
ax.set_title("Sensor Data")
ax.grid(True)
ax.legend()

fig.tight_layout()
plt.show()

# Observation:
# The smoothest rolling mean is the one with the largest window size, which is 7. 
# The larger the window size, the more data points are averaged together, 
# resulting in a smoother curve that reduces noise and fluctuations in the data.
# The disadvantage of using a larger window size is that it can also reduce 
# the responsiveness of the rolling mean to changes in the data,
# potentially masking important trends or patterns that may be present in the raw data.