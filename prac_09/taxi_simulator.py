from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    bill = 0.0
    print("Let's drive!")

    while True:
        print(f"Bill to date: ${bill:.2f}")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
        if choice == 'q':
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == 'd':
            bill = drive_taxi(current_taxi, bill)
        else:
            print("Invalid option")

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis, current_taxi):
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return current_taxi
    except ValueError:
        print("Invalid taxi choice")
        return current_taxi

def drive_taxi(current_taxi, bill):
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return bill
    try:
        distance = float(input("Drive how far? "))
        if distance <= 0:
            print("Distance must be positive")
            return bill
        current_taxi.start_fare()
        distance_driven = current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        return bill + trip_cost
    except ValueError:
        print("Invalid distance")
        return bill
main()