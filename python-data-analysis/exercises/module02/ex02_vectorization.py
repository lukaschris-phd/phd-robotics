import numpy as np

# distance_cm = np.array([
#     150,
#     110,
#     75,
#     42,
#     18,
#     12
# ])

# distance_m = distance_cm /100

# print(distance_m)

temperatures = np.array([
    23.5, 24.1, 25.7, 27.2, 28.5, 30.1
])

temp_over = np.sum(temperatures >=27)
temp_mid = np.sum((temperatures < 27) & (temperatures >=24))
temp_low = np.sum(temperatures < 24)
print("COOL   : ", temp_low)
print("NORMAL : ", temp_mid)
print("HOT    : ", temp_over)