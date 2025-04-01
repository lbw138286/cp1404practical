from taxi import Taxi

# 1. Create a new taxi object, my_taxi, with name "Prius 1" and 100 units of fuel
my_taxi = Taxi("Prius 1", 100)

# 2. Drive the taxi 40 km
my_taxi.drive(40)

# 3. Print the taxi's details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# 4. Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# 5. Print the details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")