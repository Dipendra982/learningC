# Initialize a variable to store the sum
total_sum = 0

# Create an infinite loop to take input numbers
while True:
    # Take input from the user
    num = input("Enter a number (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if num.lower() == 'q':
        break
    
    # Convert the input string to a float
    try:
        num = float(num)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
        continue
    
    # Add the number to the total sum
    total_sum += num
    
    # Print the current total sum
    print(f"Current sum: {total_sum}")

# Print the final sum
print(f"The final sum is: {total_sum}")
