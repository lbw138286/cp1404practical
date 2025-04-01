from silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 2)
hummer.drive(18)

expected_fare = 48.78
calculated_fare = hummer.get_fare()
assert abs(calculated_fare - expected_fare) < 0.01, f"Expected {expected_fare}, got {calculated_fare}"

print(hummer)
print(f"Fare: ${calculated_fare:.2f}")
