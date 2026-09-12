import numpy as np
import matplotlib.pyplot as plt

robot_heading_deg = 30.0

sensor_vectors = np.array([
    [1.0, 0.0],
    [2.0, 0.0],
    [1.0, 1.0],
    [0.0, 2.0],
    [-1.0, 1.0]
])

def rotation_matrix(angle_deg):
    angle_rad = np.radians(angle_deg)
    return np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])

v_robot = np.array([1.0, 0.0])
R = rotation_matrix(robot_heading_deg)
v_world = R @ v_robot
v_recovered = R.T @ v_world

print("Robot     :", v_robot)
print("World     :", v_world)
print("Recovered :", v_recovered)

assert np.allclose(
    v_robot,
    v_recovered
)

# Transform all sensor vectors from robot frame to world frame
sensor_vectors_world = (R @ sensor_vectors.T).T
print("Sensor vectors (world frame):")
print(sensor_vectors_world)

# Transform all sensor vectors back from world frame to robot frame
recovered_vectors = (R.T @ sensor_vectors_world.T).T
print("Sensor vectors (robot frame):")
print(recovered_vectors)

assert np.allclose(
    sensor_vectors,
    recovered_vectors
)

# Angle between sensor vectors a and b
a = sensor_vectors[1]
b = sensor_vectors[2]
cos_theta = (
    np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
)
cos_theta = np.clip(cos_theta, -1.0, 1.0)
theta_deg = np.degrees(np.arccos(cos_theta))

a_world = sensor_vectors_world[1]
b_world = sensor_vectors_world[2]
cos_theta_world = (
    np.dot(a_world, b_world) / (np.linalg.norm(a_world) * np.linalg.norm(b_world))
)
cos_theta_world = np.clip(cos_theta_world, -1.0, 1.0)
theta_deg_world = np.degrees(np.arccos(cos_theta_world))

print("Angle between a and b (degrees):", theta_deg)
print("Angle between a and b in world frame (degrees):", theta_deg_world)

fig1, ax = plt.subplots(
    1,1,figsize=(6, 6)
)
ax.quiver(0, 0, sensor_vectors[0,0], sensor_vectors[0,1], angles='xy', scale_units='xy', scale=1, color='r', label='Robot frame')
ax.quiver(0, 0, sensor_vectors_world[0,0], sensor_vectors_world[0,1], angles='xy', scale_units='xy', scale=1, color='g', label='World frame')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
fig1.savefig(
    "figures/module07/coordinate_transformation.png",
    dpi=300
)
plt.show()

# Interpretations
# 1. What is the difference between a vector and its magnitude?
# Vector: has both magnitude and direction
# Magnitude: the length of the vector
#
# 2. What is a unit vector and why is it useful?
# Unit vector: a vector with magnitude 1, used to represent direction without affecting magnitude
#
# 3. What does a positive, zero, or negative dot product
#    tell us about two vectors?
# Positive: vectors point in roughly the same direction
# Zero: vectors are perpendicular
# Negative: vectors point in roughly opposite directions
#
# 4. What does the angle-between-vectors formula calculate?
# It calculates the angle between two vectors in degrees.
#
# 5. What is vector projection?
# Vector projection is the operation of projecting one vector onto another, 
# resulting in a vector that lies along the direction of the second vector.
#
# 6. What is the difference between * and @ in NumPy?
# * performs element-wise multiplication
# @ performs matrix multiplication (dot product for vectors)
#
# 7. What does a rotation matrix do to a vector?
# A rotation matrix rotates a vector by a certain angle while preserving its magnitude.
#
# 8. Why does rotation preserve vector magnitude?
# Because rotation is an orthogonal transformation, which preserves the length of vectors.
#
# 9. What is a coordinate frame?
# A coordinate frame is a reference system used to define the position and orientation of objects in space.
#
# 10. Why can [1, 0] mean different directions in robot frame and world frame?
# Because the orientation of the robot frame may differ from the world frame, 
# so the same coordinates can point in different directions.
#
# 11. Why can R.T be used to reverse a pure rotation?
# Because the transpose of a rotation matrix is its inverse, which undoes the rotation.
#
# 12. Does rotating two vectors change the angle between them? Explain.
# Rotating two vectors does not change the angle between them because rotation 
# preserves the relative orientation of vectors.