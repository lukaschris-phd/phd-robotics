import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv(
    "data/sample/robot_imu.csv"
)

ACC_DEV_THRESHOLD = 0.5
GYRO_THRESHOLD = 5.0
GRAVITY = 9.81

# Dataset Information
print("IMU MOTION ANALYZER")
print("=" * 30)
print("Readings           :", len(df))
print("Duration           :", df["timestamp"].iloc[-1] - df["timestamp"].iloc[0], "s")
print("Sampling interval  :", f"{df['timestamp'].diff().mean():.3f}", "s")
print("Sampling frequency :", 1 / df["timestamp"].diff().mean(), "Hz")

# Accelerometer magnitude
acc = df[["ax", "ay", "az"]].to_numpy()
df["acc_magnitude"] = np.linalg.norm(acc, axis=1)
df["acc_magnitude_manual"] = np.sqrt(
    df["ax"]**2 +
    df["ay"]**2 +
    df["az"]**2
)
assert np.allclose(df["acc_magnitude_manual"], df["acc_magnitude"]), \
    "ERROR: Magnitude calculations do not match!"
print("Magnitude calculations match!")

# Gyroscope magnitude
gyro = df[["gx", "gy", "gz"]].to_numpy()
df["gyro_magnitude"] = np.linalg.norm(gyro, axis=1)

df["acc_deviation"] = (
    df["acc_magnitude"] - GRAVITY
).abs() 

# Motion candidate 
df["motion_candidate"] = (
    (df["acc_deviation"] > ACC_DEV_THRESHOLD) |
    (df["gyro_magnitude"] > GYRO_THRESHOLD)
)
print("Motion candidate readings :", df["motion_candidate"].sum())
timestamp_first_motion_candidate = df.loc[df["motion_candidate"].idxmax(), "timestamp"]
print("First candidate timestamp :", timestamp_first_motion_candidate,"s")
timestamp_last_motion_candidate = df.loc[df["motion_candidate"].iloc[::-1].idxmax(), "timestamp"]
print("Last candidate timestamp  :", timestamp_last_motion_candidate,"s")

# Accelerometer Figure
fig1, axes1 = plt.subplots(
    3,
    1,
    figsize=(9, 8),
    sharex=True
)

axes1[0].plot(
    df["timestamp"],
    df["ax"],
    label="AX"
)

axes1[1].plot(
    df["timestamp"],
    df["ay"],
    label="AY"
)

axes1[2].plot(
    df["timestamp"],
    df["az"],
    label="AZ"
)

fig2, axes2 = plt.subplots(
    3,
    1,
    figsize=(9, 8),
    sharex=True
)

axes2[0].plot(
    df["timestamp"],
    df["gx"],
    label="GX"
)

axes2[1].plot(
    df["timestamp"],
    df["gy"],
    label="GY"
)

axes2[2].plot(
    df["timestamp"],
    df["gz"],
    label="GZ"
)

for ax in axes1:
    ax.legend()
    ax.set_ylabel("Acceleration (m/s²)")
    ax.grid(True)

for ax2 in axes2:
    ax2.legend()
    ax2.set_ylabel("Angular Velocity (°/s)")
    ax2.grid(True)

fig3, axes3 = plt.subplots(
    2,
    1,
    figsize=(9, 8),
    sharex=True
)

axes3[0].plot(
    df["timestamp"],
    df["acc_magnitude"],
    label="ACC Magnitude",
)
axes3[0].set_ylabel("Acceleration (m/s²)")
axes3[1].plot(
    df["timestamp"],
    df["gyro_magnitude"],
    label="GYRO Magnitude",
)
axes3[1].set_ylabel("Angular Velocity (°/s)")

for ax3 in axes3:
    ax3.legend()
    ax3.grid(True)

# Motion candidate figure
fig4, ax4 = plt.subplots(
    1,
    1,
    figsize=(9, 4)
)

mask = df["motion_candidate"] == True

ax4.plot(
    df["timestamp"],
    df["acc_deviation"],
    label="Acceleration Magnitude Deviation"
)

ax4.scatter(
    df.loc[mask, "timestamp"],
    df.loc[mask, "acc_deviation"],
    color="red",
    marker="x",
    label="Motion Candidates"
)

ax4.axhline(
    y=ACC_DEV_THRESHOLD,
    linestyle="--",  
    label="Acceleration Deviation Threshold"
)
ax4.set_ylabel("Acceleration Deviation (m/s²)")
ax4.legend()
ax4.grid(True)

plt.xlabel("Timestamp")
plt.tight_layout()

fig1.savefig(
    "figures/module06/fig1_accelerometer_xyz.png",
    dpi=300
)
fig2.savefig(
    "figures/module06/fig2_gyroscope_xyz.png",
    dpi=300
)
fig3.savefig(
    "figures/module06/fig3_magnitude.png",
    dpi=300
)
fig4.savefig(
    "figures/module06/fig4_motion_candidates.png",
    dpi=300
)

plt.show()

# Interpretation 
#
# 1. What does accelerometer magnitude represent?
# It represents the overall acceleration experienced by the IMU,
# including both the gravitational and dynamic components.
#
# 2. Why can a stationary IMU still show approximately
#    9.81 m/s²?
# This is because even when stationary, the accelerometer measures 
# the gravitational acceleration acting on it.
#
# 3. What does gyroscope magnitude represent?
# Gyroscope magnitude represents the overall rotational speed of the IMU.
#
# 4. Why does gyro magnitude NOT directly represent angle?
# Because it measures angular velocity, not the absolute angle.
# Angle change can be estimated by integrating angular velocity over time.
#
# 5. What does acc_deviation measure?
# acc_deviation measures how far the acceleration magnitude is from the expected
# gravitational magnitude.
#
# 6. Why is abs(acc_magnitude - 9.81)
#    NOT true gravity removal?
# Because we do the operation on magnitude, not on gravitational vector.
#
# 7. What does motion_candidate mean in this exercise?
# Motion_candidate is a reading where either acceleration deviation exceeds the threshold.
# or gyroscope magnitude exceeds their respective thresholds.
#
# 8. What are the limitations of this analysis?
# This is a simple threshold-based detector using synthetic data.
# The thresholds are arbitrary training values, and the method does not account
# for sensor noise, bias, orientation, gravity-vector estimation,
# or real robot ground truth.