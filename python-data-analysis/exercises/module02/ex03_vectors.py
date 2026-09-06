import numpy as np

position = np.array([3, 4])

magnitude = np.linalg.norm(position)

print(magnitude)

robot_position = np.array([2, 3])
target_position = np.array([8, 11])

difference = target_position - robot_position

print(difference)

distance = np.linalg.norm(
    target_position - robot_position
)

print(distance)

A = np.array([0, 0])
B = np.array([3, 4])
C = np.array([6, 8])
D = np.array([10, 8])

distance_AB = np.linalg.norm(B-A)
distance_BC = np.linalg.norm(C-B)
distance_CD = np.linalg.norm(D-C)

print("Distance A -> B =", distance_AB)
print("Distance B -> C =", distance_BC)
print("Distance C -> D =", distance_CD)
print("Total distance covered =",distance_AB + distance_BC + distance_CD)