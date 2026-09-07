import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/clean_iot_sensor.csv")
obstacle_data = df[df["obstacle"]]

print(df.info())
print("\n")

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

axes1[0].plot(
    df["timestamp"],
    df["temperature"],
    marker="o",
    linestyle="-",
)

axes1[0].set_ylabel("Temperature (°C)")
axes1[0].grid(True)

axes1[1].plot(
    df["timestamp"],
    df["humidity"],
    marker="o",
    linestyle="-",
)

axes1[1].set_xlabel("Time (s)")
axes1[1].set_ylabel("Humidity (%)")
axes1[1].grid(True)

# Figure 2
fig2, axes2 = plt.subplots(
    figsize=(8, 7)
)
axes2.plot(df["timestamp"], df["distance"], marker="o", linestyle="--")
axes2.scatter(
    obstacle_data["timestamp"],
    obstacle_data["distance"],
    marker="x",
    label="Obstacle"
)
axes2.set_title("Obstacle Detection")
axes2.legend()
axes2.set_xlabel("Time (s)")
axes2.set_ylabel("Distance (m)")
axes2.grid(True)

threshold = 50

axes2.axhline(
    y=threshold,
    linestyle="-",  
    label="Obstacle Threshold"
)

# Counting the number of times the distance is below the threshold
count = (df["distance"] < threshold).sum()

print("Obstacle readings:", count)
first_point1 = df[df["distance"] < threshold].iloc[0]
x_f2 = first_point1["timestamp"]
y_f2 = first_point1["distance"]

axes2.annotate(
    f"First crossing at {x_f2:.2f}s, {y_f2:.2f}m",
    xy=(x_f2, y_f2),
    xytext=(x_f2 + 1, y_f2 + 1),
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=10
)

# Figure 3
fig3, axes3 = plt.subplots(
    figsize=(8, 7)
)
axes3.plot(df["timestamp"], df["battery"], marker="o", linestyle="--")
batt_threshold = 11
mask = df["battery"] < batt_threshold

axes3.axhline(
    y=batt_threshold,
    linestyle="-",  
    label="11 V low-battery threshold"
)

axes3.scatter(
    df.loc[mask, "timestamp"],
    df.loc[mask, "battery"],
    color="red",
    marker="x",
    label="Low Battery"
)

axes3.axhspan(
    9,
    batt_threshold,
    color="red",
    alpha=0.1,
    label="Low Battery Zone"
)

first_point2 = df[df["battery"] < batt_threshold].iloc[0]
x_f3 = first_point2["timestamp"]
y_f3 = first_point2["battery"]

axes3.annotate(
    f"First crossing at {x_f3:.2f}s, {y_f3:.2f}V",
    xy=(x_f3, y_f3),
    xytext=(x_f3 + 0.5, y_f3 + 0.5),
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=10
)

axes3.set_title("Battery Level Monitoring")
axes3.set_xlabel("Time (s)")
axes3.set_ylabel("Battery Level (V)")
axes3.legend()
# Counting the number of times the battery voltage is below the threshold
count_battery = (df["battery"] < batt_threshold).sum()

print("Low battery readings:", count_battery)

# Figure 4
fig4, axes4 = plt.subplots(
    figsize=(8, 7)
)
axes4.scatter(df["temperature"], df["humidity"], marker="o", color="blue")
correlation = df["temperature"].corr(df["humidity"])
axes4.set_title("Temperature vs Humidity")
axes4.set_xlabel("Temperature (°C)")
axes4.set_ylabel("Humidity (%)")    
axes4.grid(True)
print("Temperature-Humidity Correlation :", correlation)

# Correlation value 0.908 indicates a strong positive correlation 
# between temperature and humidity, suggesting that as the temperature increases, 
# the humidity tends to increase as well.

fig1.savefig(
    "figures/environment_monitor.png",
    dpi=300
)

fig2.savefig(
    "figures/obstacle_detection.png",
    dpi=300
)

fig3.savefig(
    "figures/battery_monitor.png",
    dpi=300
)

fig4.savefig(
    "figures/temperature_humidity.png",
    dpi=300
)

plt.tight_layout()
plt.show()

# =====================================================
# INTERPRETATION
# =====================================================
#
# 1. Temperature:
# Temperature tends to fluctuate within a normal range and averagely increasing, 
# indicating that the robot's temperature sensor is functioning properly.
#
# 2. Humidity:
# Humidity tends to increase as the temperature increases, 
# which is expected in many environments.
#
# 3. Obstacle:
# There are 5 instances where the distance readings fall below the 50 cm threshold.
#
# 4. Battery:
# There are 4 instances where the battery voltage drops below the 11 V threshold, 
# indicating low battery conditions.
#
# 5. Temperature-Humidity relationship:
# There are positive correlation between temperature and humidity, 
# which means that as the temperature increases, the humidity tends to increase as well. 
# This relationship can be important for understanding environmental conditions 
# and their impact on the robot's performance.
#
# Limitations:
# Data is limited to a specific time frame and may not represent long-term trends.