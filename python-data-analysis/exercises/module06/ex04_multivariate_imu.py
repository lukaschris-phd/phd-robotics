import pandas as pd

df = pd.read_csv(
    "data/sample/robot_imu.csv"
)

print(df.head())
print(df.shape)
print(df.info())