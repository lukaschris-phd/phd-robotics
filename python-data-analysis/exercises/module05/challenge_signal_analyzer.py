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

ROLLING_WINDOW = 5

df["distance_smooth"] = (
    df["distance"]
    .rolling(
        window=ROLLING_WINDOW,
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
timestamp_positive_rate = df.loc[idx_max_positive_rate, "timestamp"]
max_negative_rate = df["distance_rate"].min()
idx_max_negative_rate = df["distance_rate"].idxmin()
timestamp_negative_rate = df.loc[idx_max_negative_rate, "timestamp"]

print("")
print("Largest increase :", max_positive_rate, "cm/s at :", timestamp_positive_rate, "s")
print("Largest decrease :", max_negative_rate, "cm/s at :", timestamp_negative_rate, "s")

SPIKE_THRESHOLD = 30

df["distance_change"] = df["distance"].diff()
df["abs_change"] = df["distance_change"].abs()


df["candidate_spike"] = (
    df["abs_change"] > SPIKE_THRESHOLD
)
candidate_spike_count = df["candidate_spike"].sum()

print("")
print(df[["distance_change", "abs_change"]])
print("")
print("Candidate spike changes :", candidate_spike_count)

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
ax2.set_ylabel("Distance Rate (cm/s)")
ax2.grid(True)
ax2.set_title("RATE OF CHANGE")
fig2.tight_layout()

# y=0 is a reference for rate:
# rate > 0 measured distance increasing
# rate = 0 no change between consecutive measurements
# rate < 0 measured distance decreasing

fig3, ax3 = plt.subplots(figsize=(9, 5))
spikes = df[df["candidate_spike"]]

ax3.plot(
    df["timestamp"],
    df["distance"],
    marker="o",
    label="Raw"
)
ax3.scatter(
    spikes["timestamp"],
    spikes["distance"],
    marker="x",
)

first_point = spikes.iloc[0]
x_f2 = first_point["timestamp"]
y_f2 = first_point["distance"]

ax3.annotate(
    f"First candidate spike at {x_f2:.2f}s, {y_f2:.2f}cm",
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

ROLLING_STD_WINDOW = 5

df["rolling_std"] = (
    df["distance"]
    .rolling(
        window=ROLLING_STD_WINDOW,
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
timestamp_idx_largest_std = df.loc[index_largest_std, "timestamp"]

print("Largest rolling standard deviation:", largest_std)
print("Timestamp of largest rolling standard deviation:", timestamp_idx_largest_std)

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
# From the beginning, the raw signal data has some values that looked different.
#
# 2. Smoothing:
# Smoothing with a rolling mean of 5 is able to make the data smooth and reduce spikes.
# But in general, smoothing can make signal to be less responsive/lag and can covers
# short events.
#
# 3. Rate of change:
# A negative value means the measured distance decreases 
# ompared to the previous measurement. 
# Conversely, a positive value means the measured distance 
# increases compared to the previous measurement.
#
# 4. Candidate spikes:
# To practice detecting unusual transition candidates, we can use threshold like
# abs_change > 30 or other particular number.
#
# 5. Rolling variability:
# Rolling standard deviation increases around regions containing large changes, 
# indicating greater local variability.
# Rolling variability measures local variability.
#
# 6. Limitations:
# 31 readings + 1 Hz sampling cannot generalize robot behavior or sensor performance.
# Normalization can only change data scale, and does not eliminate noise nor anomaly.