"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    my_car = Car(150, "my car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    limo = Car(100, "limo")
    limo.add_fuel(20)
    print(f"Car has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)

main()
