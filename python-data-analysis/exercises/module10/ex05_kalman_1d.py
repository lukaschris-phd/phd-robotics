import numpy as np
import matplotlib.pyplot as plt

measurements = np.array([
    10.2, 9.9, 10.1, 10.0, 9.8, 10.1
])

x = 9.0       # Initial estimate
P = 4.0       # Initial uncertainty
Q = 0.01      # Process noise variance
R = 0.09      # Measurement noise variance

estimates = []
variances = []
gains = []

for z in measurements:

    # PREDICT
    x_prior = x
    P_prior = P + Q

    # UPDATE
    K = P_prior / (P_prior + R)

    x = x_prior + K * (z - x_prior)
    P = (1 - K) * P_prior

    estimates.append(x)
    variances.append(P)
    gains.append(K)

plt.figure(figsize=(10, 5))
plt.plot(measurements, "o--", label="Measurement")
plt.plot(estimates, "o-", label="Kalman Estimate")
plt.axhline(10.0, linestyle=":", label="True Position")

plt.xlabel("Measurement Index")
plt.ylabel("Position (m)")
plt.legend()
plt.grid()
plt.show()

# Adding variance and Kalman Gain plots
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(variances, "o-", label="Variance (P)")
plt.xlabel("Measurement Index")
plt.ylabel("Variance (m²)")
plt.legend()
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(gains, "o-", label="Kalman Gain (K)")
plt.xlabel("Measurement Index")
plt.ylabel("Kalman Gain")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()  

# Summary:
# The Kalman Filter iteratively updates the estimate of the position based on 
# noisy measurements.
# The variance decreases over time, 
# indicating increased confidence in the estimate.
