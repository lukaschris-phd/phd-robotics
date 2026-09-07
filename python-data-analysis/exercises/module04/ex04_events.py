import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")

obstacle_data = df[df["obstacle"]]

plt.plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Distance"
)

plt.scatter(
    obstacle_data["timestamp"],
    obstacle_data["distance"],
    marker="x",
    label="Obstacle"
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
plt.title("Obstacle Detection")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()