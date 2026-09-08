import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

df["rolling_std"] = (
    df["distance"]
    .rolling(
        window=5,
        min_periods=1
    )
    .std()
)

# Figure 1
fig1, axes1 = plt.subplots(
    2,
    # 2 rows
    1,
    # 1 column
    figsize=(8, 7),
    sharex=True
    # berbagi sumbu x yang sama
)

fig1.suptitle("Robot Distance Sensor Rolling Standard Deviation")

axes1[0].plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    linestyle="-",
)

axes1[0].set_ylabel("Raw Distance (cm)")
axes1[0].grid(True)

axes1[1].plot(
    df["timestamp"],
    df["rolling_std"],
    marker="o",
    linestyle="-",
)

axes1[1].set_xlabel("Time (s)")
axes1[1].set_ylabel("Rolling Std (window=5)")
axes1[1].grid(True)

largest_std = df["rolling_std"].max()
index_largest_std = df["rolling_std"].idxmax()

print("Largest rolling standard deviation:", largest_std)
print("Index of largest rolling standard deviation:", index_largest_std)

plt.show()