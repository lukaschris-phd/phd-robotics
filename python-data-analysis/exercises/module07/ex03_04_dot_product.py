import numpy as np

a = np.array([1.0, 0.0])

b1 = np.array([1.0, 0.0])
b2 = np.array([0.0, 1.0])
b3 = np.array([-1.0, 0.0])

print(np.dot(a, b1))
print(np.dot(a, b2))
print(np.dot(a, b3))

b = np.array([1.0, 1.0])

cos_theta = (
    np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
)
cos_theta = np.clip(cos_theta, -1.0, 1.0)
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print("Theta (radians) :", theta_rad)
print("Theta (degrees) :", theta_deg, "°")
