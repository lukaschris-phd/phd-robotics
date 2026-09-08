import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Raw Distance"
)

ax.set_xlabel("Time (s)")
ax.set_ylabel("Distance (cm)")
ax.set_title("Raw Robot Distance Sensor")
ax.grid(True)
ax.legend()

fig.tight_layout()
plt.show()

# Observation:
# The raw distance sensor data shows a possible spike of noise and fluctuations, 
# which can make it difficult to analyze the underlying trends. 