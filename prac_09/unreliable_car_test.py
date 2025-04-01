from unreliable_car import UnreliableCar

def test_unreliable_car():
    car1 = UnreliableCar("Reliable-ish", 100, 90)
    successful_drives_1 = 0
    attempts = 100

    for _ in range(attempts):
        distance_driven = car1.drive(10)
        if distance_driven > 0:
            successful_drives_1 += 1

    assert 75 <= successful_drives_1 <= 100, \
        f"Expected 75-100 successful drives, got {successful_drives_1}"

    car2 = UnreliableCar("Unreliable", 100, 10)
    successful_drives_2 = 0

    for _ in range(attempts):
        distance_driven = car2.drive(10)
        if distance_driven > 0:
            successful_drives_2 += 1

    assert 0 <= successful_drives_2 <= 25, \
        f"Expected 0-25 successful drives, got {successful_drives_2}"

    initial_fuel = car2.fuel
    for _ in range(10):
        car2.drive(5)
    assert car2.fuel <= initial_fuel, "Fuel should not increase"
    print("All tests passed!")

if __name__ == "__main__":
    test_unreliable_car()