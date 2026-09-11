import numpy as np

acceleration = np.array([
    0.1,
    0.2,
    9.7
])

acc_mag = np.linalg.norm(acceleration)
print("Acceleration magnitude:", acc_mag)

imu = np.array([
    [0.1, 0.2, 9.7],
    [0.2, 0.1, 9.8],
    [0.3, 0.2, 9.6],
    [1.5, 0.8, 9.4],
    [2.5, 1.6, 8.9]
])

imu_mean = np.mean(imu, axis=0)
print("IMU mean acceleration:", imu_mean)
imu_std = np.std(imu, axis=0)
print("IMU standard deviation of acceleration:", imu_std)
imu_mag = np.linalg.norm(imu, axis=1)
print("IMU acceleration magnitudes:", imu_mag)