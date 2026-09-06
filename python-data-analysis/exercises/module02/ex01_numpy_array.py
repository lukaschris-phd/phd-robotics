import numpy as np

temperatures = np.array([
    23.5,
    24.1,
    25.7,
    27.2,
    28.5,
    30.1
])

distances = np.array([
    150,
    110,
    75,
    42,
    18,
    12
])

print("Number of readings  : ", np.size(temperatures))
print("Average temperature : ", np.mean(temperatures))
print("Minimum temperature : ", np.min(temperatures))
print("Maximum temperature : ", np.max(temperatures))
print("\n")
print("Average distance    : ", np.mean(distances))
print("Minimum distance    : ", np.min(distances))
print("Maximum distance    : ", np.max(distances))