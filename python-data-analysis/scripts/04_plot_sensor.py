import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5]
distance = [150, 140, 125, 110, 95, 80]

plt.plot(time, distance)

plt.xlabel("Time (seconds)")
plt.ylabel("Distance (cm)")
plt.title("Ultrasonic Sensor Reading")

plt.show()