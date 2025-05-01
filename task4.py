"""Ask the user to enter 5 temperatures (one each day), store them in a list using a loop, and print the average temperature."""
temperatures = []

for i in range(5):
    temp = float(input(f"enter temperature for day {i+1}: "))
    temperatures.append(temp)

average_temp = sum(temperatures) / len(temperatures)
print(f"average temperature: {average_temp}")
