"""
Estimated time: 15min
Real time: 22min
"""
from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 10000.00)
    expect_age_gibson = 100
    expect_age_another_guitar = 11
    real_age_gibson = gibson.get_age()
    real_age_another_guitar = another_guitar.get_age()
    print(f"{gibson.name} get_age() - Expected {expect_age_gibson}. Got {real_age_gibson}.")
    print(f"{another_guitar.name} get_age() - Excepted {expect_age_another_guitar}. Got {real_age_another_guitar}.")
    expect_vintage_gibson = True
    expect_vintage_another_guitar = False
    real_vintage_gibson = gibson.is_vintage()
    real_vintage_another_guitar = another_guitar.is_vintage()
    print(f"{gibson.name} is_vintage() - Expected {expect_vintage_gibson}. Got {real_vintage_gibson}.")
    print(
        f"{another_guitar.name} is_vintage() - Expected {expect_vintage_another_guitar}. Got {real_vintage_another_guitar}.")

main()
#