import numpy as np

velocity = np.array([3.0, 4.0])
forward = np.array([1.0, 0.0])

projection = np.dot(velocity, forward) / np.linalg.norm(forward)
print("Projection of velocity onto forward :", projection)