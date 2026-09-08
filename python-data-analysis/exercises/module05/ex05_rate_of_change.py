import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

delta_distance = df["distance"].diff()
delta_time = df["timestamp"].diff()

df["distance_rate"] = (
    delta_distance / delta_time
)

max_positive_rate = df["distance_rate"].max()
idx_max_positive_rate = df["distance_rate"].idxmax()
max_negative_rate = df["distance_rate"].min()
idx_max_negative_raet = df["distance_rate"].idxmin()

print("Largest positive rate :", max_positive_rate, "di indeks :", idx_max_positive_rate)
print("Largest negative rate :", max_negative_rate, "di indeks :", idx_max_negative_raet)