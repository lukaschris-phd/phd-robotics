import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    "data/sample/robot_distance_sensor.csv"
)

print("ROBOT DISTANCE SIGNAL ANALYZER")
print("=================================")
print("")
print("TIME SERIES")
print("Total readings     :", len(df))
print("Duration           :", df["timestamp"].max() - df["timestamp"].min(),"s")
print("Sampling interval  :", df["timestamp"].diff().median(),"s")
print("Sampling frequency :", 1 / df["timestamp"].diff().median(),"Hz")
print("")
print("Mean distance      :", df["distance"].mean())
print("Median distance    :", df["distance"].median())
print("Minimum distance   :", df["distance"].min())
print("Maximum distance   :", df["distance"].max())
print("Standard deviation :", df["distance"].std())

df["distance_smooth"] = (
    df["distance"]
    .rolling(
        window=5,
        min_periods=1
    )
    .mean()
)
print("")
print(df)

delta_distance = df["distance"].diff()
delta_time = df["timestamp"].diff()

df["distance_rate"] = (
    delta_distance / delta_time
)

max_positive_rate = df["distance_rate"].max()
idx_max_positive_rate = df["distance_rate"].idxmax()
max_negative_rate = df["distance_rate"].min()
idx_max_negative_raet = df["distance_rate"].idxmin()

print("")
print("Largest decrease :", max_positive_rate, "cm/s at :", idx_max_positive_rate, "s")
print("Largest increase :", max_negative_rate, "cm/s at :", idx_max_negative_raet, "s")

spike_threshold = 30

df["distance_change"] = df["distance"].diff()
df["abs_change"] = df["distance_change"].abs()

candidate_spike = (df["abs_change"] > spike_threshold).sum()

print("")
print(df[["distance_change", "abs_change"]])
print("")
print("Candidate spike changes :", candidate_spike)

df["distance_normalized"] = (
    (df["distance"] - df["distance"].min()) / (df["distance"].max()-df["distance"].min())
)

assert np.isclose(df["distance_normalized"].min(), 0), \
    "ERROR: minimum normalization result is not 0"

assert np.isclose(df["distance_normalized"].max(), 1), \
    "ERROR: maximum normalization result is not 1"

print("✓ Normalization success!")

fig1, ax1 = plt.subplots(figsize=(9, 5))

ax1.plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Raw"
)
ax1.plot(
    df["timestamp"],
    df["distance_smooth"],
    marker="o",
    label="Smooth"
)

ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Distance (cm)")
ax1.grid(True)
ax1.legend()
ax1.set_title("RAW vs. SMOOTHED")
fig1.tight_layout()

fig2, ax2 = plt.subplots(figsize=(9, 5))

ax2.plot(
    df["timestamp"],
    df["distance_rate"]
)

ax2.axhline(
    y=0,
    linestyle="--",
)

ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Distance Rate")
ax2.grid(True)
ax2.set_title("RATE OF CHANGE")
fig2.tight_layout()

# y=0 is useful for knowing how far the spike deviates

fig3, ax3 = plt.subplots(figsize=(9, 5))

ax3.plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Raw"
)
ax3.scatter(
    df["timestamp"],
    df["distance_change"],
    marker="x",
)

first_point = df[df["abs_change"] > spike_threshold].iloc[0]
x_f2 = first_point["timestamp"]
y_f2 = first_point["distance"]

ax3.annotate(
    f"First crossing at {x_f2:.2f}s, {y_f2:.2f}cm",
    xy=(x_f2, y_f2),
    xytext=(x_f2 + 1, y_f2 - 40),
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=10
)

ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Distance (cm)")
ax3.grid(True)
ax3.legend()
ax3.set_title("CANDIDATE SPIKES")
fig3.tight_layout()

df["rolling_std"] = (
    df["distance"]
    .rolling(
        window=5,
        min_periods=1
    )
    .std()
)

fig4, ax4 = plt.subplots(figsize=(9, 5))

ax4.plot(
    df["timestamp"],
    df["rolling_std"],
    marker="o",
    linestyle="-",
)

ax4.set_xlabel("Time (s)")
ax4.set_ylabel("Rolling Standard Deviation")
ax4.grid(True)
ax4.set_title("ROLLING VARIABILITY")
fig4.tight_layout()

largest_std = df["rolling_std"].max()
index_largest_std = df["rolling_std"].idxmax()

print("Largest rolling standard deviation:", largest_std)
print("Timestamp of largest rolling standard deviation:", index_largest_std)

fig1.savefig(
    "figures/module05/raw_vs_smoothed.png",
    dpi=300
)
fig2.savefig(
    "figures/module05/rate_of_change.png",
    dpi=300
)
fig3.savefig(
    "figures/module05/candidate_spikes.png",
    dpi=300
)
fig4.savefig(
    "figures/module05/rolling_variability.png",
    dpi=300
)

plt.show()

# =====================================================
# INTERPRETATION
# =====================================================
#
# 1. Raw signal:
# From the start, the raw signal data was quite different.
#
# 2. Smoothing:
# Smoothing with a rolling mean of 5 is able to make the data smooth and reduce spikes.
#
# 3. Rate of change:
# The rate of change graph shows deviations from normal values.
#
# 4. Candidate spikes:
# Candidate spikes can be identified 
# by calculating the distance change that exceeds the specified threshold.
#
# 5. Rolling variability:
# Data spikes cause spikes in data calculations.
# Rolling variability helps the data return to smoothness. 
#
# 6. Limitations:
# Threshold limits can be adjusted or set according to the data.