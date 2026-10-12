import numpy as np

measurements = np.array([
    9.8, 10.2, 10.0, 9.9, 10.1
])

mean = np.mean(measurements)
variance = np.var(measurements)
std = np.std(measurements)

print(f"Mean     : {mean:.4f} m")
print(f"Variance : {variance:.4f} m²")
print(f"Std Dev  : {std:.4f} m")

sensor_a = [
    9.95, 9.98, 9.94, 9.93, 10.01, 10.05, 10.04, 10.07, 9.92, 9.96,
    10.02, 9.96, 9.98, 10.03, 9.99, 10.04, 10.08, 9.97, 10.06, 10.02
]

sensor_b = [
    11.60, 11.10, 9.40, 9.25, 10.75, 9.05, 10.95, 8.40, 10.60, 7.85,
    9.60, 10.25, 11.35, 10.15, 8.90, 9.85, 9.75, 10.40, 8.65, 12.15
]

mean_a = np.mean(sensor_a)
variance_a = np.var(sensor_a)
std_a = np.std(sensor_a)
mean_b = np.mean(sensor_b)
variance_b = np.var(sensor_b)
std_b = np.std(sensor_b)

print(f"Mean Dataset A     : {mean_a:.4f} m")
print(f"Variance Dataset A : {variance_a:.4f} m²")
print(f"Std Dev Dataset A  : {std_a:.4f} m")
print(f"Mean Dataset B     : {mean_b:.4f} m")
print(f"Variance Dataset B : {variance_b:.4f} m²")
print(f"Std Dev Dataset B  : {std_b:.4f} m")
