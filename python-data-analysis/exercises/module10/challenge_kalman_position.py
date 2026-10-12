import numpy as np

rng = np.random.default_rng(42)
# This rng is a random number generator instance that uses the PCG64 algorithm.
# It is initialized with a seed of 42 for reproducibility.

time = np.arange(0, 10.0, 0.1)
kalman_estimates = []

true_position = 1.5 * time

measurement_noise = rng.normal(
    0, 0.8, len(time)
)

measurements = true_position + measurement_noise

# Plotting the true position and measurements
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(time, true_position, label="True Position", color="blue")
plt.scatter(time, measurements, label="Measurements", color="orange", s=10)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("True Position vs Measurements")
plt.legend()
plt.grid()
plt.savefig(
    "figures/module10/true_pos_vs_measurements.png",
    dpi=300
)
plt.show()

# The sensor measurements not exactly match the true position 
# due to the added Gaussian noise, which simulates real-world 
# sensor inaccuracies.

x = 0.0
P = 4.0

velocity = 1.5
Q = 0.01
R = 0.64

dt = 0.1

# For each time step, we will perform 
# the predict and update steps of the Kalman filter.
for z in measurements:
    # PREDICT
    x_prior = x + velocity * dt
    P_prior = P + Q

    # UPDATE
    K = P_prior / (P_prior + R)

    x = x_prior + K * (z - x_prior)
    P = (1 - K) * P_prior
    kalman_estimates.append(float(np.asarray(x).item()))
    print(f"Measurement: {z:.2f}, Estimate: {x:.2f}, Variance: {P:.2f}, Kalman Gain: {K:.2f}")  

# Error and RMSE
measurement_errors = z - true_position
measurement_rmse = np.sqrt(np.mean(measurement_errors**2))
kalman_errors = x - true_position
kalman_rmse = np.sqrt(np.mean(kalman_errors**2))
print(f"Measurement RMSE   : {measurement_rmse:.2f} m")
print(f"Kalman Filter RMSE : {kalman_rmse:.2f} m")

# Position Estimation Figure
plt.figure(figsize=(10, 5))
plt.plot(time, true_position, label="True Position", color="blue")
plt.scatter(time, measurements, label="Measurements", color="orange", s=10)
plt.plot(time, kalman_estimates, label="Kalman Estimate", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Kalman Filter Position Estimation")
plt.legend()
plt.grid()
plt.savefig(
    "figures/module10/position_estimation.png",
    dpi=300
)
plt.show()

# Estimation Error Figure
plt.figure(figsize=(10, 5))
plt.plot(time, measurements - true_position, label="Measurement Error", color="orange")
plt.plot(time, np.array(kalman_estimates) - true_position, label="Kalman Filter Error", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Error (m)")
plt.title("Estimation Errors")
plt.legend()
plt.grid()
plt.savefig(
    "figures/module10/estimation_errors.png",
    dpi=300
)
plt.show()

# Kalman Diagnostics Figure
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(time, [P] * len(time), label="Variance (P)", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Variance (m²)")
plt.title("Kalman Filter Diagnostics")
plt.legend()
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(time, [K] * len(time), label="Kalman Gain (K)", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Kalman Gain")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(
    "figures/module10/kalman_diagnostics.png",
    dpi=300
)   
plt.show()

# Questions:
# 1. Why does the Kalman estimation tends to be stable than the raw measurements?
#    The Kalman filter combines the predictions from the model 
#    and the noisy measurements, weighting them based on their uncertainties. 
#    This results in a more stable and accurate estimate.
# 2. What will happen if R is increased from 0.64 to 4.0?
#    Increasing R means that the measurement noise is considered to be higher.
#    This will lead to a smaller Kalman Gain, meaning the filter will rely more on
#    the model prediction and less on the measurements, 
#    potentially making the estimate less responsive to actual
#    changes in the true position.
# 3. What will happen if Q is increased from 0.01 to 1.0?
#    Increasing Q means that the process noise is considered to be higher.
#    This will lead to a larger Kalman Gain, meaning the filter will rely more on
#    the measurements and less on the model prediction,
#    potentially making the estimate more responsive to actual changes in the true position,
#    but also more susceptible to noise in the measurements.
# 4. Is the Kalman Filter still accurate if the true velocity is not constant,
#    but the model keeps assuming a constant velocity? Why or why not?
#    The Kalman Filter may still provide reasonable estimates, but its accuracy will degrade
#    if the true velocity varies significantly from the assumed constant velocity.