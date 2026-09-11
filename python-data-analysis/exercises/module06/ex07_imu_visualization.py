import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/sample/robot_imu.csv"
)

fig1, axes1 = plt.subplots(
    3,
    1,
    figsize=(9, 8),
    sharex=True
)

axes1[0].plot(
    df["timestamp"],
    df["ax"],
    label="AX"
)

axes1[1].plot(
    df["timestamp"],
    df["ay"],
    label="AY"
)

axes1[2].plot(
    df["timestamp"],
    df["az"],
    label="AZ"
)

fig2, axes2 = plt.subplots(
    3,
    1,
    figsize=(9, 8),
    sharex=True
)

axes2[0].plot(
    df["timestamp"],
    df["gx"],
    label="GX"
)

axes2[1].plot(
    df["timestamp"],
    df["gy"],
    label="GY"
)

axes2[2].plot(
    df["timestamp"],
    df["gz"],
    label="GZ"
)

for ax in axes1:
    ax.legend()
    ax.set_ylabel("Acceleration (m/s²)")
    ax.grid(True)

for ax2 in axes2:
    ax2.legend()
    ax2.set_ylabel("Angular Velocity (°/s)")
    ax2.grid(True)

plt.xlabel("Timestamp")
plt.tight_layout()
plt.show()

# Analysis:
# Accelerometer and gyroscope readings show larger changes during approximately 0.5-1.1 s