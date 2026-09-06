import numpy as np

# position = np.array([1, 0])

# theta = np.radians(90)

# rotation_matrix = np.array([
#     [np.cos(theta), -np.sin(theta)],
#     [np.sin(theta),  np.cos(theta)]
# ])

# new_position = rotation_matrix @ position

# print(np.round(new_position, 10))

point = np.array([2, 1])

def rotate_point(point, angle_degree):
    theta = np.radians(angle_degree)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    return rotation_matrix @ point   

print(rotate_point(point, 90))
print(rotate_point(point, 180))
print(rotate_point(point, 270))