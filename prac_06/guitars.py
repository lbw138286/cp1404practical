"""
Estimated time: 15min
Real time: 15min
"""
from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = []
    # name = input("Name: ")
    # year = input("Year: ")
    # cost = input("Cost: $")
    # guitars.append(Guitar(name, year, cost))
    Guitar("Gibson L-5 CES", 1922, 16035.40)
    Guitar("Line 6 JTV-59", 2010, 1512.9)
    Guitar("Fender Stratocaster", 2014, 765.40)
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()
#