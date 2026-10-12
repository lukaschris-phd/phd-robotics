import numpy as np

dt = 0.5

F = np.array([
    [1, dt],
    [0, 1]
])

state = np.array([
    [10.0],
    [2.0]
])

predicted_state = F @ state

print(predicted_state)