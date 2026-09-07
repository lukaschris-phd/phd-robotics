import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")

# plt.figure(figsize=(8, 5))

# Time vs Temperature plot
# plt.plot(
#     df["timestamp"],
#     df["temperature"],
#     marker="x",
#     linestyle="-",
#     label="Temperature"
# )

# plt.xlabel("Time (s)")
# plt.ylabel("Temperature (°C)")
# plt.title("Robot Temperature Sensor")
# plt.legend()
# plt.grid()
# plt.tight_layout()

# plt.show()

# Intepretation: The temperature plot shows that the robot's temperature sensor is functioning properly, 
# as the temperature readings are uprising within a normal range and show expected fluctuations over time.

# Time vs Battery plot
plt.plot(
    df["timestamp"],
    df["battery"],
    marker="o",
    linestyle="-",
    label="Battery Level"
)

plt.xlabel("Time (s)")
plt.ylabel("Battery Level (%)")
plt.title("Robot Battery Level")
plt.legend()
plt.grid()
plt.tight_layout()

plt.show()

# Intepretation: The battery level plot indicates that the robot's battery is discharging over time, 
# which is expected during operation. The gradual decrease in battery level suggests 
# that the robot is consuming power as it performs its tasks.