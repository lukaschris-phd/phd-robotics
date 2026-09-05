import pandas as pd

data = {
    "time": [0, 1, 2, 3, 4],
    "temperature": [23.4, 23.8, 24.1, 24.7, 25.0],
    "humidity": [60, 61, 63, 62, 64],
    "distance": [120, 118, 115, 110, 105]
}

df = pd.DataFrame(data)

print(df)

print("\nSummary:")
print(df.describe())