import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/sample/robot_imu.csv"
)

ACC_DEV_THRESHOLD = 0.5
GYRO_THRESHOLD = 5.0
GRAVITY = 9.81

acc = df[["ax", "ay", "az"]].to_numpy()
df["acc_magnitude"] = np.linalg.norm(acc, axis=1)

df["acc_deviation"] = (
    df["acc_magnitude"] - GRAVITY
).abs()

gyro = df[["gx", "gy", "gz"]].to_numpy()
df["gyro_magnitude"] = np.linalg.norm(gyro, axis=1)
df["gyro_deviation"] = df["gyro_magnitude"].abs()

df["motion_candidate"] = (
    (df["acc_deviation"] > ACC_DEV_THRESHOLD) |
    (df["gyro_deviation"] > GYRO_THRESHOLD)
)

total_motion_candidates = df["motion_candidate"].sum()
print("Total motion candidates:", total_motion_candidates)

first_motion_candidate_index = df.index[df["motion_candidate"]].tolist()[0]
timestamp_first_motion_candidate = df.loc[first_motion_candidate_index, "timestamp"]
print("First motion candidate timestamp:", timestamp_first_motion_candidate)

last_motion_candidate_index = df.index[df["motion_candidate"]].tolist()[-1]
timestamp_last_motion_candidate = df.loc[last_motion_candidate_index, "timestamp"]
print("Last motion candidate timestamp:", timestamp_last_motion_candidate)
