# Convert temprature from degree celsius to fahrenhite
# Read celsius as an input from the user

# conversion formula: (0°C × 9/5) + 32 = 32°F

Celsius = input("Please enter the temprature in degree celsius: \n")
Celsius = float(Celsius)
type(Celsius)
Fahrenhite = ((Celsius * 9 / 5) + 32)
print(f"The temprature in Fahrenhite is: {Fahrenhite}")