import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")

# # Temperature vs Humidity scatter plot
# plt.scatter(
#     df["temperature"],
#     df["humidity"]
# )

# plt.xlabel("Temperature (°C)")
# plt.ylabel("Humidity (%)")
# plt.title("Temperature vs Humidity")

# Battery vs Distance scatter plot
plt.scatter(
    df["battery"],
    df["distance"]
)

plt.xlabel("Battery Level (%)")
plt.ylabel("Distance (cm)")
plt.title("Battery Level vs Distance")

plt.grid()
plt.tight_layout()

plt.show()