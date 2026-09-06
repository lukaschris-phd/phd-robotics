import pandas as pd

sensor_data = {
    "time": [0, 1, 2, 3, 4],
    "temperature": [23.5, 24.1, 25.7, 27.2, 28.0],
    "humidity": [45, 50, 55, 60, 65],
    "distance": [150, 110, 75, 42, 20],
    "battery": [12.6, 12.3, 11.9, 11.4, 10.8]
}

df = pd.DataFrame(sensor_data)

print("Sensor 5 data pertama:")
print(df.head(5))

print("\nSensor 3 data terakhir:")
print(df.tail(3))

print("\nDataset Information:")
print(df.shape)
print(df.info())
print(df.describe())