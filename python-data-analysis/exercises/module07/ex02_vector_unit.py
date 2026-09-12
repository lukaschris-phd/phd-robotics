import numpy as np

robot = np.array([2.0, 3.0])
target = np.array([8.0, 11.0])

displacement = target - robot
distance = np.linalg.norm(displacement)

print("Robot        :", robot)
print("Target       :", target)
print("Displacement :", displacement)
print("Distance     :", distance)

direction = displacement / np.linalg.norm(displacement)

print("Direction :", direction)
print("Magnitude :", np.linalg.norm(direction))

assert np.isclose(
    np.linalg.norm(direction),
    1.0
)

speed = 2.0
velocity = direction * speed

print("Velocity :", velocity)