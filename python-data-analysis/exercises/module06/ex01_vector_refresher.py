import numpy as np

a = np.array([2, 3, 6])

# Magnitude of the vector `a`
magnitude_manual = np.sqrt(
    a[0]**2 + a[1]**2 + a[2]**2
)

magnitude_numpy = np.linalg.norm(a)

print("Manual :", magnitude_manual)
print("NumPy  :", magnitude_numpy)

# Vector subtraction 
robot = np.array([2, 3])
target = np.array([8, 11])
direction = target - robot
distance = np.linalg.norm(direction)
print("Direction :", direction)
print("Distance  :", distance)

