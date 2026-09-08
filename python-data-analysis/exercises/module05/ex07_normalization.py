import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

df["normalized"] = (
    (df["distance"] - df["distance"].min()) / (df["distance"].max()-df["distance"].min())
)

df["normalized"] = df["normalized"].round(0)

print(df)

# Normalization can help remove noise and correct outliers. 
# However, if the data patterns are inconsistent, normalization risks removing valid data.