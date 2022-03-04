# Author: CRS 03/04/22
def build_vehicle(vehicle_type, axels, doors, color, wheels, price_range):
    return("This care is a " + vehicle_type + " with " + wheels + " wheels, " + axels + " axels, " + doors + " doors, is " + color + ", and is roughly $" + price_range + ".")


vehicle_type = input("What type of vehicle would you like?")
axels = input("How many axels would you like?")
doors = input("How many doors would you like?")
color = input("What color would you like?")
wheels = input("How many wheels would you like?")
price_range = input("What is you price range for your vehicle?")

print(build_vehicle(vehicle_type, axels, doors, color, wheels, price_range))
