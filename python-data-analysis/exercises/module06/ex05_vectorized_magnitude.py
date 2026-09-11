import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/sample/robot_imu.csv"
)

# Perhitungan magnitudo percepatan menggunakan metode manual
df["acc_magnitude_manual"] = np.sqrt(
    df["ax"]**2 +
    df["ay"]**2 +
    df["az"]**2
)
print(df["acc_magnitude_manual"])

# Sama dengan
acc = df[["ax", "ay", "az"]].to_numpy()
df["acc_magnitude_numpy"] = np.linalg.norm(acc, axis=1)
print(df["acc_magnitude_numpy"])

# Cek dengan assert
assert np.allclose(df["acc_magnitude_manual"], df["acc_magnitude_numpy"]), \
    "ERROR: Magnitude calculations do not match!"
print("Magnitude calculations match!")
