temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

first_reading = temperatures[0]
last_reading = temperatures[-1]

afternoon_peak = temperatures[3:6]
last_three_hours = temperatures[-3:]

print("First Reading:", first_reading)
print("Last Reading:", last_reading)
print("Afternoon Peak Readings:", afternoon_peak)
print("Last 3 Hours Readings:", last_three_hours)
