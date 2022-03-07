# Author: CRS 03/07/22
# Define factorial
def factorial(number):
    # Set variables
    total = 1
    element = 1
    # Create if else statement to check if number can be multiplied
    if number >= 1:
        for element in range(1, number + 1):
            total *= element
            element += 1
        return total
    elif number < 1:
        print("Number must be greater than 0.")
        # Test
print(factorial(5))