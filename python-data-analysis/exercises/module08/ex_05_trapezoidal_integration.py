import pandas as pd
import numpy as np

df = pd.DataFrame({
    "time": [0, 1, 2, 3, 4],
    "velocity": [0, 1, 2, 3, 4]
})

delta_t = np.diff(df["time"])

delta_x = df["velocity"][:-1] * delta_t

position = np.concatenate(
    ([0], np.cumsum(delta_x))
)

distance = np.trapezoid(
    df["velocity"],
    df["time"]
)

print("distance:", distance)