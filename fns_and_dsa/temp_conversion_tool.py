FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(f):
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(c):
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    user_input_temp = float(input("Enter the temperature to convert: "))
    user_input_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if user_input_unit == 'F':
        result = convert_to_celsius(user_input_temp)
        print(f"{user_input_temp}°F is {result:.2f}°C")
    elif user_input_unit == 'C':
        result = convert_to_fahrenheit(user_input_temp)
        print(f"{user_input_temp}°C is {result:.2f}°F")
    else:
        print("Invalid temperature unit. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
