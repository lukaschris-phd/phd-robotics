import pandas as pd
import numpy as np

# df = pd.read_csv("data/sensor_readings.csv")
# df = pd.read_csv("data/sensor_readings_missing.csv")
df = pd.read_csv("data/sensor_readings_out.csv")

print(df)
print(df.shape)
print(df.info())
print(df.describe())

# # Accessing a specific column
# temperature = df["temperature"]
# print(temperature)

# # Accessing multiple columns
# selected_columns = df[["temperature", "humidity"]]
# print(selected_columns)

# # Filter
# filtered_data = df[df["temperature"] >= 27]
# print("\nFiltered Data (Temperature >= 27):")
# print(filtered_data)
# print(f"Terdapat {filtered_data.shape[0]} baris data yang memenuhi kondisi")

# filtered_distance = df[df["distance"] < 50]
# print("\nFiltered Data (Distance < 50):")
# print(filtered_distance)
# print(f"Terdapat {filtered_distance.shape[0]} baris data yang memenuhi kondisi")

# filtered_battery = df[df["battery"] <= 11.5]
# print("\nFiltered Data (Battery <= 11.5):")
# print(filtered_battery)
# print(f"Terdapat {filtered_battery.shape[0]} baris data yang memenuhi kondisi")

# multiple_conditions1 = df[(df["temperature"] >= 27) & (df["distance"] < 50)]
# print("\nFiltered Data (Temperature >= 27 AND Distance < 50):")
# print(multiple_conditions1)
# print(f"Terdapat {multiple_conditions1.shape[0]} baris data yang memenuhi kondisi")

# multiple_conditions2 = df[(df["distance"] < 30) | (df["battery"] < 11)]
# print("\nFiltered Data (Distance < 30 OR Battery < 11):")
# print(multiple_conditions2)
# print(f"Terdapat {multiple_conditions2.shape[0]} baris data yang memenuhi kondisi")

# df["temperature_status"] = np.where(
#     df["temperature"] >= 27,
#     "HOT",
#     "NORMAL"
# )

# print("\nData with Temperature Status:")
# print(df)

# df["obstacle"] = df["distance"] < 50
# print("\nData with Obstacle Column:")
# print(df)

# df["low_battery"] = df["battery"] < 11
# print("\nData with Low Battery Column:")
# print(df)

# =============================== Missing data
# print("\nMissing Data Information:")
# print(df.isna())
# print("\nMissing Data Count:")
# print(df.isna().sum())

# median_temperature = df["temperature"].median()
# df["temperature"] = df["temperature"].fillna(median_temperature)
# print("\nData after Filling Missing Temperature Values:")
# print(df)
# print(df.isna().sum())

# median_humidity = df["humidity"].median()
# df["humidity"] = df["humidity"].fillna(median_humidity)
# print("\nData after Filling Missing Humidity Values:")
# print(df)
# print(df.isna().sum())

# distance_interpolated = df["distance"].interpolate()
# df["distance"] = distance_interpolated
# print("\nData after Interpolating Missing Distance Values:")
# print(df)
# print(df.isna().sum())

# df["distance_m"] = df["distance"] / 100
# print("\nData with Distance in Meters:")
# print(df)

# =============================== Outlier
valid_temperature = df["temperature"].between(-20, 60)
df.loc[~valid_temperature, "temperature"] = np.nan
print("\nData after Handling Temperature Outliers:")
print(df)
# langsung diganti median
df["temperature"] = df["temperature"].fillna(
    df["temperature"].median()
)
print("\nData after Filling Temperature Outliers with Median:")
print(df)

valid_humidity = df["humidity"].between(0, 100)
df.loc[~valid_humidity, "humidity"] = np.nan
print("\nData after Handling Humidity Outliers:")
print(df)
# langsung diganti median
df["humidity"] = df["humidity"].fillna(
    df["humidity"].median()
)
print("\nData after Filling Humidity Outliers with Median:")
print(df)

valid_distance = df["distance"].ge(0)
df.loc[~valid_distance, "distance"] = np.nan
print("\nData after Handling Distance Outliers:")
print(df)
# langsung diganti interpolasi
df["distance"] = df["distance"].interpolate()
print("\nData after Interpolating Distance Outliers:")
print(df)