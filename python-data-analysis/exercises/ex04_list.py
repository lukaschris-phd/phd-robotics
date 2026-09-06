# import pandas as pd

sensor_data = [
    {
        "time": 0,
        "temperature": 23.5,
        "distance": 120
    },
    {
        "time": 1,
        "temperature": 23.8,
        "distance": 105
    },
    {
        "time": 2,
        "temperature": 24.1,
        "distance": 87
    }
]

# df = pd.DataFrame(sensor_data)

# for reading in sensor_data:
#     print(
#         reading["time"],
#         reading["temperature"],
#         reading["distance"]
#     )

# print(df)
# print("\nSummary:")
# print(df.describe())

for reading in sensor_data:
    print(
        f"Time: {reading['time']} s | "
        f"Temp: {reading['temperature']} C | "
        f"Distance: {reading['distance']} cm"
    )