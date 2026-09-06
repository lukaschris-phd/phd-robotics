import numpy as np

imu_data = np.array([
    [0.1, 0.2, 9.7],
    [0.2, 0.1, 9.8],
    [0.4, 0.3, 9.6],
    [1.2, 0.8, 9.3],
    [2.1, 1.5, 8.9]
])

print("Accelerometer Statistics")
print("\nAX")
print("Mean =", np.mean(imu_data[:,0]))
print("Min  =", np.min(imu_data[:,0]))
print("Max  =", np.max(imu_data[:,0]))
print("STD  =", np.std(imu_data[:,0]))
print("\nAY")
print("Mean =", np.mean(imu_data[:,1]))
print("Min  =", np.min(imu_data[:,1]))
print("Max  =", np.max(imu_data[:,1]))
print("STD  =", np.std(imu_data[:,1]))
print("\nAZ")
print("Mean =", np.mean(imu_data[:,2]))
print("Min  =", np.min(imu_data[:,2]))
print("Max  =", np.max(imu_data[:,2]))
print("STD  =", np.std(imu_data[:,2]))