import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

sensor_a = rng.normal(10, 0.2, 1000)
sensor_b = rng.normal(10, 1.0, 1000)

plt.figure(figsize=(10, 5))

plt.hist(sensor_a, bins=40, alpha=0.6,
         density=True, label="Sensor A")

plt.hist(sensor_b, bins=40, alpha=0.6,
         density=True, label="Sensor B")

plt.xlabel("Measured Position (m)")
plt.ylabel("Probability Density")
plt.title("Sensor Measurement Uncertainty")
plt.legend()
plt.grid(alpha=0.3)
plt.show()