# def cm_to_meter(distance_cm):
#     return  distance_cm / 100

# distance = cm_to_meter(150)

# print(distance)

# =============================================

# def robot_action(distance):

#     if distance < 20:
#         return "STOP"

#     elif distance < 50:
#         return "SLOW"

#     else:
#         return "MOVE"

# distances = [150, 80, 45, 15]

# for distance in distances:
#     action = robot_action(distance)
#     print(f"{distance} cm -> {action}")

# =============================================

def battery_status(voltage):

    if voltage >= 12.0:
        return("FULL")
    elif voltage >= 11.0:
        return("NORMAL")
    elif voltage >= 10.0: 
        return("LOW")
    else: 
        return("CRITICAL")

voltages = [12.6, 12.1, 11.5, 10.7, 9.8]

for voltage in voltages:
    action = battery_status(voltage)
    print(f"{voltage} -> {action}")