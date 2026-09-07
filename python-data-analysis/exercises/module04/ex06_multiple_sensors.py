import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")

# fig, axes = plt.subplots(
#     2,
#     # 2 rows
#     1,
#     # 1 column
#     figsize=(8, 7),
#     sharex=True
#     # berbagi sumbu x yang sama
# )

# axes[0].plot(
#     df["timestamp"],
#     df["temperature"]
# )

# axes[0].set_ylabel("Temperature (°C)")

# axes[1].plot(
#     df["timestamp"],
#     df["humidity"]
# )

# axes[1].set_xlabel("Time (s)")
# axes[1].set_ylabel("Humidity (%)")

# plt.tight_layout()
# plt.show()

# =======================================
# Buat satu figure dengan 3 vertically stacked subplots

fig, axes = plt.subplots(
    3,
    # 3 rows
    1,
    # 1 column
    figsize=(8, 7),
    sharex=True
    # berbagi sumbu x yang sama
)

axes[0].plot(
    df["timestamp"],
    df["temperature"]
)

axes[0].set_ylabel("Temperature (°C)")

axes[1].plot(
    df["timestamp"],
    df["distance"]
)

axes[1].set_ylabel("Distance (m)")

axes[2].plot(
    df["timestamp"],
    df["battery"]
)

axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Battery Level (%)")

plt.tight_layout()
plt.show()