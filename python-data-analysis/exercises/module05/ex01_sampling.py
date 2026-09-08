import pandas as pd

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

print(df.head())
print(df.shape)

print("TIME SERIES INFORMATION")
print("=================================")
print("Total readings     :", len(df))
print("Duration           :", df["timestamp"].max() - df["timestamp"].min(),"s")
print("Sampling interval  :", df["timestamp"].diff().median(),"s")
print("Sampling frequency :", 1 / df["timestamp"].diff().median(),"Hz")