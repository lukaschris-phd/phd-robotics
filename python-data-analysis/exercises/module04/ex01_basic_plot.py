import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")

# Time vs Temperature plot
plt.plot(df["timestamp"], df["temperature"])
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Over Time")
plt.grid()
plt.tight_layout()
plt.show()

# Time vs Humidity plot
plt.plot(df["timestamp"], df["humidity"])
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.title("Humidity Over Time")
plt.grid()
plt.tight_layout()
plt.show()

# Time vs Distance plot
plt.plot(df["timestamp"], df["distance"])
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Distance Over Time")
plt.grid()
plt.tight_layout()
plt.show()

# Time vs Battery plot
plt.plot(df["timestamp"], df["battery"])
plt.xlabel("Time (s)")
plt.ylabel("Battery Level (%)")
plt.title("Battery Level Over Time")
plt.grid()
plt.tight_layout()
plt.show()

