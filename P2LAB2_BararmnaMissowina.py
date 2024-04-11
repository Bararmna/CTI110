# Bararmna Missowina
# 4/11/2024
# P2LAB2
# Dictionaries
cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}
# Got keys
cars_keys = cars.keys()
print(cars_keys)
print(*cars_keys, sep = ", ")
# Got a car from users
cars_name = input("Enter a car: ")
#Got mpg for the cars
car_mpg = cars[cars_name]
print(f"the {cars_name} gets {car_mpg} mpg.")
# Got miles from user
miles_driven = float(input(f"How many miles will you drive the {cars_name}?"))
# Gallons of gas needed to drive
gallons_needed = miles_driven/car_mpg
 #display results
print(f"{gallons_needed: .2f} gallons of gas are needed to drive the {cars_name} {miles_driven} miles.")
                     
