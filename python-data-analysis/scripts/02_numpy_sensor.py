import numpy as np

temperature = np.array([
    23.4,
    23.8,
    24.1,
    24.7,
    25.0,
    24.8
])

print("Sensor readings:")
print(temperature)

print("Mean:", np.mean(temperature))
print("Minimum:", np.min(temperature))
print("Maximum:", np.max(temperature))
print("Standard deviation:", np.std(temperature))