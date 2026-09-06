sensor_data = [
    {"time": 0, "distance": 150, "battery": 12.6},
    {"time": 1, "distance": 120, "battery": 12.3},
    {"time": 2, "distance": 80,  "battery": 12.0},
    {"time": 3, "distance": 45,  "battery": 11.8},
    {"time": 4, "distance": 25,  "battery": 11.5},
    {"time": 5, "distance": 15,  "battery": 11.2}
]

def robot_action(distance):
    if distance < 20:
        return "STOP"
    elif distance < 50:
        return "SLOW"
    else:
        return "MOVE"

for reading in sensor_data:

    action = robot_action(reading["distance"])

    print(
        f'Time: {reading["time"]} s | '
        f'Distance: {reading["distance"]} cm | '
        f'Battery: {reading["battery"]} V | '
        f'Action: {action}'
    )