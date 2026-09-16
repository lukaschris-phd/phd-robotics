import pandas as pd
import numpy as np

df = pd.DataFrame({
    "time": [0, 1, 2, 3, 4],
    "position": [0, 1, 4, 9, 16]
})

# df["delta_position"] = df["position"].diff()
# df["delta_time"] = df["time"].diff()
# df["velocity"] = df["delta_position"] / df["delta_time"]

# df["acceleration"] = df["velocity"].diff() / df["delta_time"]
# print(df)

x = np.array([0, 1, 4, 9, 16])

dx = np.diff(x)
grad = np.gradient(x)
print("dx:", dx)
print("grad:", grad)

# Interpretasi:
# Mengapa nilai dx dan grad berbeda?
# dx menghitung selisih diskrit antara elemen berturut-turut, 
# sehingga panjangnya berkurang satu dibanding array asli.
# grad menghitung gradien menggunakan metode pusat untuk elemen tengah 
# dan metode maju/mundur untuk elemen tepi, sehingga panjangnya sama dengan array asli.