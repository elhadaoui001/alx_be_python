# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Convert F to C
def convert_to_celsius(f):
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert C to F
def convert_to_fahrenheit(c):
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program
def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    elif unit == 'C':
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

# Run the main function
if __name__ == "__main__":
    main()
