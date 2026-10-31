import numpy as np

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

# a. Add 2°C
corrected_temperature = temperature + 2
print("Corrected temperature:", corrected_temperature)

# b. Celsius to Fahrenheit
fahrenheit = ((9/5) * corrected_temperature )+ 32
print("Fahrenheit:", fahrenheit)

# c. Readings greater than 32°C
greater_than_32 = corrected_temperature[corrected_temperature > 32]
print("Readings greater than 32°C:", greater_than_32)

# d. Count readings greater than 32°C
count = np.sum(corrected_temperature > 32)
print("Number of readings exceeding 32°C:", count)
