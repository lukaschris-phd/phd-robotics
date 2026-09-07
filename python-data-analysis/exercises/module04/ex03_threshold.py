import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")

plt.plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Distance"
)

threshold = 50
below_threshold = df["distance"] < threshold

plt.axhline(
    y=threshold,
    linestyle="--",
    label="Obstacle Threshold"
)

plt.xlabel("Time (s)")
plt.ylabel("Distance (cm)")
plt.title("Obstacle Distance Monitoring")
plt.legend()
plt.grid()
plt.tight_layout()

plt.show()

first_crossing = df[df["distance"] < threshold].iloc[0]

x = first_crossing["timestamp"]
y = first_crossing["distance"]

print(f"First crossing of the threshold at time {x} seconds with distance {y} cm.")