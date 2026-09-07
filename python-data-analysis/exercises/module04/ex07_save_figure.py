import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")

plt.figure(figsize=(8, 5))

#Time vs Temperature plot
plt.plot(
    df["timestamp"],
    df["temperature"],
    marker="x",
    linestyle="-",
    label="Temperature"
)

plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Robot Temperature Sensor")
plt.legend()
plt.grid()
plt.tight_layout()

plt.savefig(
    "figures/temperature_over_time.png",
    dpi=300
)

plt.savefig(
    "figures/temperature_over_time.pdf",
)

plt.show()