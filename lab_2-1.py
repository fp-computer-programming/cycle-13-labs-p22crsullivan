# Author: CRS 03/04/22
# Define build_car function
def build_car(wheels, axels, doors, color):
    return("This care has " + wheels + " wheels, " + axels + " axels, " + doors + " doors, and is " + color + ".")

# Create variables for each part
wheels = input("What wheels would you like?")
axels = input("How many axels would you like?")
doors = input("How many doors would you like?")
color = input("What color would you like?")
# Test the code
print(build_car(wheels, axels, doors, color))
