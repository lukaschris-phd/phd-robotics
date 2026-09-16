import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample/robot_motion_calculus.csv")

# Sampling Information
print("MOTION INTEGRATION ANALYZER")
print("=" * 30)

print("Readings                  :", df.shape[0])
print("Duration                  :", df["time"].iloc[-1] - df["time"].iloc[0],"s")
print("Sampling interval         :", df["time"].diff().mean(),"s")
print("Sampling frequency        :", 1 / df["time"].diff().mean(),"Hz")

# Gyroscope Integration
df["dt"] = df["time"].diff().fillna(0)
df["delta_angle"] = (
    df["gz"] * df["dt"]
)
df["angle"] = df["delta_angle"].cumsum()
print("Angle Euler               :\n", df["angle"])

# Trapezoidal Angle Integration
df["delta_angle_trap"] = (
    (df["gz"] + df["gz"].shift(1)) / 2 * df["dt"]
)
df["angle_trap"] = df["delta_angle_trap"].cumsum()
print("Angle Trapezoidal         :\n", df["angle_trap"])

# Accelerometer Integration
df["delta_velocity"] = (
    df["ax"] * df["dt"]
)
df["velocity"] = df["delta_velocity"].cumsum()
print("Velocity Euler             :\n", df["velocity"])

# Position Estimate
df["delta_position"] = (
    df["velocity"] * df["dt"]
)
df["position"] = df["delta_position"].cumsum()
print("Position Estimate          :\n", df["position"])

# Bias Experiment
GYRO_BIAS = 0.5
ACC_BIAS = 0.05

df["gz_bias"] = df["gz"] + GYRO_BIAS
df["ax_bias"] = df["ax"] + ACC_BIAS

# Gyroscope Integration with Bias
df["delta_angle_bias"] = (
    df["gz_bias"] * df["dt"]
)
df["angle_bias"] = df["delta_angle_bias"].cumsum()
print("Angle Euler with Bias      :\n", df["angle_bias"])

# Accelerometer Integration with Bias
df["delta_velocity_bias"] = (
    df["ax_bias"] * df["dt"]
)
df["velocity_bias"] = df["delta_velocity_bias"].cumsum()
print("Velocity Euler with Bias   :\n", df["velocity_bias"])

# Position Estimate with Bias
df["delta_position_bias"] = (
    df["velocity_bias"] * df["dt"]
)
df["position_bias"] = df["delta_position_bias"].cumsum()
print("Position Estimate with Bias:\n", df["position_bias"])

assert df["time"].is_monotonic_increasing, "Time column is not monotonically increasing"
# assert (df["dt"].dropna() > 0).all(), "Sampling interval must be positive"

# Figure 1 - Gyro & Angle
fig1, ax1 = plt.subplots(
    2,
    1,
    figsize=(10, 8)
)
ax1[0].plot(df["time"], df["gz"], label="Gyro Z")
ax1[0].set_title("Gyroscope Z-axis")
ax1[0].set_xlabel("Time [s]")
ax1[0].set_ylabel("Angular Rate [rad/s]")
ax1[0].legend()

ax1[1].plot(df["time"], df["angle"], label="Angle Euler")
ax1[1].plot(df["time"], df["angle_trap"], label="Angle Trapezoidal")
ax1[1].set_title("Integrated Angle")
ax1[1].set_xlabel("Time [s]")
ax1[1].set_ylabel("Angle [rad]")
ax1[1].legend()

# Figure 2 - Acceleration -> Velocity 
fig2, ax2 = plt.subplots(
    2,
    1,
    figsize=(10, 8)
)
ax2[0].plot(df["time"], df["ax"], label="Accel X")
ax2[0].plot(df["time"], df["ax_bias"], label="Accel X with Bias")
ax2[0].set_title("Accelerometer X-axis")
ax2[0].set_xlabel("Time [s]")
ax2[0].set_ylabel("Acceleration [m/s²]")
ax2[0].legend()

ax2[1].plot(df["time"], df["velocity"], label="Velocity Euler")
ax2[1].plot(df["time"], df["velocity_bias"], label="Velocity Euler with Bias")
ax2[1].set_title("Integrated Velocity")
ax2[1].set_xlabel("Time [s]")
ax2[1].set_ylabel("Velocity [m/s]")
ax2[1].legend()

# Figure 3 - Position Drift
fig3, ax3 = plt.subplots(
    1,
    1,
    figsize=(10, 8)
)
ax3.plot(df["time"], df["position"], label="Position Clean")
ax3.plot(df["time"], df["position_bias"], label="Position with Accelerometer Bias")
ax3.set_title("Integrated Position")
ax3.set_xlabel("Time [s]")
ax3.set_ylabel("Position [m]")
ax3.legend()

# Figure 4 - Gyro Drift
fig4, ax4 = plt.subplots(
    1,
    1,
    figsize=(10, 8)
)
ax4.plot(df["time"], df["angle"], label="Angle Clean")
ax4.plot(df["time"], df["angle_bias"], label="Angle with Gyro Bias")
ax4.set_title("Gyroscope Integration Drift")
ax4.set_xlabel("Time [s]")
ax4.set_ylabel("Estimated Angle [rad]")
ax4.legend()

plt.tight_layout()
fig1.savefig(
    "figures/module08/gyro_angle.png",
    dpi=300
)
fig2.savefig(
    "figures/module08/accel_velocity.png",
    dpi=300
)
fig3.savefig(
    "figures/module08/position_drift.png",
    dpi=300
)
fig4.savefig(
    "figures/module08/gyro_drift.png",
    dpi=300
)
plt.show()
# Interpretation

# 1. What is a derivative in the context of robot motion?
# Derivative represents the rate of change of a quantity with respect to time. 
# In robot motion, it often refers to how velocity changes over time (acceleration) 
# or how position changes over time (velocity).
#
# 2. What is an integral in the context of robot motion?
# Integral represents the accumulation of a quantity over time.
# In robot motion, it often refers to how velocity accumulates to change position
# or how acceleration accumulates to change velocity.
#
# 3. Why does the first derivative sample often become NaN?
# The first derivative sample often becomes NaN because there is no previous data point 
# to compute the rate of change at the initial time step.
#
# 4. What is the difference between Euler and trapezoidal integration?
# Euler integration approximates the integral by using the current value of the function 
# multiplied by the time step.
# Trapezoidal integration improves accuracy by averaging the current and previous values 
# of the function over the time step.
#
# 5. Why can gyro integration estimate angle change?
# Gyro integration can estimate angle change because the gyroscope measures angular velocity.
# By integrating the angular velocity over time, we can obtain the change in angle.
#
# 6. Why does gyro bias cause drift?
# Gyro bias causes drift because even a small constant bias in angular velocity accumulates over time,
# leading to an increasing error in the estimated angle.
#
# 7. Why is accelerometer integration more difficult?
# Accelerometer integration is more difficult because it is sensitive to noise and bias.
# Small errors in acceleration measurements accumulate over time, 
# causing significant drift in velocity and position.
#
# 8. Why does double integration amplify error?
# Double integration amplifies error because any small error in acceleration is integrated twice: 
# first to velocity and then to position, leading to a rapidly growing error over time.

#
# 9. Why does acceleration not directly equal velocity?
# Acceleration is the rate of change of velocity, not velocity itself. 
# To obtain velocity from acceleration, one must integrate acceleration over time.
#
# 10. Why does numerical integration only approximate the true continuous motion?
# Numerical integration only approximates the true continuous motion 
# because it uses discrete time steps and finite differences.
# The smaller the time step, the closer the approximation to the true continuous motion, 
# but it can never be exact.
#
# 11. What are the limitations of this synthetic experiment?
# The experiment uses simplified synthetic motion and deliberately
# introduces constant sensor bias. Real IMU measurements may also
# contain random noise, time-varying bias, scale-factor error,
# temperature effects, gravity/orientation effects, and vibration.