temperatures = [
    23.5,
    23.8,
    24.0,
    24.7,
    25.1,
    26.2,
    27.5,
    29.1
]
average = sum(temperatures)/len(temperatures)

print(f"Number of readings   : {len(temperatures)}")
print(f"Minimum temperatures : {min(temperatures)}")
print(f"Maximum temperatures : {max(temperatures)}")
print(f"Average temperatures : {average:.2f}")

for temperature in temperatures:
        
    if temperature < 25:
        print(f"{temperature} -> NORMAL")
    elif temperature < 28:
        print(f"{temperature} -> WARM")
    else:
        print(f"{temperature} -> HOT")  

