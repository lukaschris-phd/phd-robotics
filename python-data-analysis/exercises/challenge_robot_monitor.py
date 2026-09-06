sensor_data = [
    {"time": 0, "temperature": 23.5, "distance": 150, "battery": 12.6},
    {"time": 1, "temperature": 24.1, "distance": 110, "battery": 12.3},
    {"time": 2, "temperature": 25.7, "distance": 75,  "battery": 11.9},
    {"time": 3, "temperature": 27.2, "distance": 42,  "battery": 11.4},
    {"time": 4, "temperature": 28.5, "distance": 18,  "battery": 10.8},
    {"time": 5, "temperature": 30.1, "distance": 12,  "battery": 9.7}
]

def battery_status(battery):

    if battery >= 12.0:
        return("FULL")
    elif battery >= 11.0:
        return("NORMAL")
    elif battery >= 10.0: 
        return("LOW")
    else: 
        return("CRITICAL")

def robot_action(distance):
    if distance < 20:
        return "STOP"
    elif distance < 50:
        return "SLOW"
    else:
        return "MOVE"

def temperature_status(temperature):
    if temperature >= 27.0:
        return "HOT"
    elif temperature >= 24.0:
        return "NORMAL"
    else:
        return "COOL"

s = 0

for reading in sensor_data:

    batt_status = battery_status(reading["battery"])
    temp_status = temperature_status(reading["temperature"])
    action = robot_action(reading["distance"])
    
    if action == "STOP":
       s += 1

    print(
        "ROBOT SENSOR MONITOR\n"
        "==========================================\n\n"
        f"Time         : {reading["time"]} s\n"
        f"Temperature  : {reading["temperature"]} C [{temp_status}]\n"
        f"Distance     : {reading["distance"]} cm\n"
        f"Battery      : {reading["battery"]} V [{batt_status}]\n"
        f"Robot Action : {action}\n"
        "------------------------------------------\n\n"
    )

temperatures = [reading["temperature"] for reading in sensor_data]
avg_temp = sum(temperatures) / len(temperatures)

distances = [reading["distance"] for reading in sensor_data]
avg_dist = sum(distances) / len(distances)

min_dist = min(distances)
max_temp = max(temperatures)

print("SUMMARY\n")
print("==========================================\n")
print(f"Total readings      : {len(sensor_data)}")
print(f"Average temperature : {avg_temp:.2f} C")
print(f"Average distance    : {avg_dist:.2f} cm")
print(f"Minimum distance    : {min_dist} cm")
print(f"Maximum temperature : {max_temp} C")
print(f"Robot melakukan STOP sebanyak {s} kali")