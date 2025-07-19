# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for printing stars in a row
    for col in range(size):
        print("*", end="")  # Print stars on the same line
    print()  # Move to the next line after each row
    row += 1  # Move to the next row
