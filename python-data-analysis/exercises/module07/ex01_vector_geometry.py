import numpy as np

robot = np.array([2.0, 3.0])
target = np.array([8.0, 11.0])

displacement = target - robot
distance = np.linalg.norm(displacement)

print("Robot        :", robot)
print("Target       :", target)
print("Displacement :", displacement)
print("Distance     :", distance)
