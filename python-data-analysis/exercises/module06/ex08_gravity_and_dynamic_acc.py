import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/sample/robot_imu.csv"
)

GRAVITY = 9.81
acc = df[["ax", "ay", "az"]].to_numpy()
df["acc_magnitude"] = np.linalg.norm(acc, axis=1)

df["acc_deviation"] = (
    df["acc_magnitude"] - GRAVITY
).abs()

print("Acceleration deviation from gravity:")
print(df["acc_deviation"])