import pandas as pd
import numpy as np

df = pd.read_csv("data/sample/raw_iot_sensor.csv")
df_clean = df.copy()

print(df_clean.shape)
print(df_clean.info())
print(df_clean.head(5))
print(df_clean.describe())

print("\nDATA QUALITY REPORT")
print("===============================")
print("Total rows          :", df_clean.shape[0])
print("Missing temperature :", df_clean["temperature"].isna().sum())
print("Missing humidity    :", df_clean["humidity"].isna().sum())
print("Missing distance    :", df_clean["distance"].isna().sum())
print("Missing battery     :", df_clean["battery"].isna().sum())
print("\n")
print("Invalid temperature :", df_clean[(df_clean["temperature"] < -20) | (df_clean["temperature"] > 60)].shape[0])
print("Invalid humidity    :", df_clean[(df_clean["humidity"] < 0) | (df_clean["humidity"] > 100)].shape[0])
print("Invalid distance    :", df_clean[(df_clean["distance"] >= 0)].shape[0])
print("Invalid battery     :", df_clean[(df_clean["battery"] < 0) | (df_clean["battery"] > 15)].shape[0])

# Handling temporary temperature missing values by filling them with the median of the respective columns
valid_temperature = df_clean["temperature"].between(-20, 60)
df_clean.loc[~valid_temperature, "temperature"] = np.nan
# langsung diganti medians
df_clean["temperature"] = df_clean["temperature"].fillna(
    df_clean["temperature"].median()
)
print(df_clean)

# Handling temporary humidity missing values by filling them with the median of the respective columns
valid_humidity = df_clean["humidity"].between(0, 100)
df_clean.loc[~valid_humidity, "humidity"] = np.nan
# langsung diganti medians
df_clean["humidity"] = df_clean["humidity"].fillna(
    df_clean["humidity"].median()
)
print(df_clean)

# Handling temporary distance missing values by filling them with the interpolated values of the respective columns
valid_distance = df_clean["distance"].ge(0)
df_clean.loc[~valid_distance, "distance"] = np.nan
# langsung diganti interpolasi
df_clean["distance"] = df_clean["distance"].interpolate()
print(df_clean)

# Feature engineering
df_clean["distance_m"] = df_clean["distance"] / 100
print("\nData with Distance in Meters:")
print(df_clean)

df_clean["obstacle"] = df_clean["distance"] < 50
print("\nData with Obstacle Column:")
print(df_clean)

df_clean["low_battery"] = df_clean["battery"] < 11
print("\nData with Low Battery Column:")
print(df_clean)

df_clean["tempe_status"] = np.where(
    df_clean["temperature"] >= 28,
    "HOT",
    "NORMAL"
)
print(df_clean)

# Sensor analysis
print("\nSensor Analysis")
print("Average temperature : ", np.mean(df_clean["temperature"]))
print("Average humidity    : ", np.mean(df_clean["humidity"]))
print("Average distance    : ", np.mean(df_clean["distance"]))
print("Minimum distance    : ", np.min(df_clean["distance"]))
print("Maximum temperature : ", np.max(df_clean["temperature"]))
print("\n")
print("Obstale detected     :", df_clean["obstacle"].sum())
print("Low battery readings :", df_clean["low_battery"].sum())

df_clean.to_csv(
    "data/sample/clean_iot_sensor.csv",
    index=False
)