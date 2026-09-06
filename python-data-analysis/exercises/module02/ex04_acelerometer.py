import numpy as np

acceleration = np.array([
    0.2,
    0.1,
    9.7
])

magnitude = np.linalg.norm(acceleration)

print(f"Acceleration magnitude: {magnitude:.2f} m/s²")

imu_data = np.array([
    [0.1,  0.2, 9.7],
    [0.2,  0.1, 9.8],
    [0.4,  0.3, 9.6],
    [1.2,  0.8, 9.3],
    [2.1,  1.5, 8.9]
])

print(imu_data.shape)