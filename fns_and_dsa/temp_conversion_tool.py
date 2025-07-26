# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    # Using the global variable (read-only)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    # Using the global variable (read-only)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temp = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
