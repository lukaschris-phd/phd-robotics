import numpy as np

imu_data = np.array([
    [0.10, 0.20, 9.70],
    [0.15, 0.18, 9.75],
    [0.20, 0.25, 9.68],
    [0.80, 0.60, 9.40],
    [1.50, 1.20, 9.10],
    [2.20, 1.80, 8.70],
    [0.30, 0.20, 9.65],
    [0.15, 0.10, 9.78]
])

dimensi = imu_data.shape

print("IMU MOTION ANALYZER")
print("========================================\n")
print("Dataset")

print("Readings :", dimensi[0])
print("Axes     :", dimensi[1])
print("Shape    :", dimensi)

print("\nAX Statistics")
print("Mean =", np.mean(imu_data[:,0]))
print("Min  =", np.min(imu_data[:,0]))
print("Max  =", np.max(imu_data[:,0]))
print("Std  =", np.std(imu_data[:,0]))

print("\nAY Statistics")
print("Mean =", np.mean(imu_data[:,1]))
print("Min  =", np.min(imu_data[:,1]))
print("Max  =", np.max(imu_data[:,1]))
print("Std  =", np.std(imu_data[:,1]))

print("\nAZ Statistics")
print("Mean =", np.mean(imu_data[:,2]))
print("Min  =", np.min(imu_data[:,2]))
print("Max  =", np.max(imu_data[:,2]))
print("Std  =", np.std(imu_data[:,2]))

acc_magnitude = np.linalg.norm(imu_data, axis=1)
print("\nAcceleration Magnitude\n", acc_magnitude)

condition = acc_magnitude > 9.9

# print(condition)

jumlah_true = np.sum(condition)
jumlah_false = condition.size - jumlah_true

print("\nMotion Analysis")
print("Stable readings :", jumlah_false)
print("Motion readings :", jumlah_true)