import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/sample/robot_imu.csv"
)

gyro = df[["gx", "gy", "gz"]].to_numpy()
gyro_magnitude = np.linalg.norm(gyro, axis=1)
print(gyro_magnitude)