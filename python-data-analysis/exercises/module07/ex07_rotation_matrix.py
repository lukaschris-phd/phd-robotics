import numpy as np

theta = np.radians(90)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

v = np.array([1.0, 0.0])

v_rotated = R @ v

print(np.round(v_rotated, 10))

# Inverse Rotation
theta = np.radians(30)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

v_robot = np.array([2.0, 0.0])

v_world = R @ v_robot
v_recovered = R.T @ v_world

print("Robot     :", v_robot)
print("World     :", v_world)
print("Recovered :", v_recovered)

assert np.allclose(
    v_robot,
    v_recovered
)