import csv
from prac_07.guitar import Guitar


def read_guitar(filename):
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_new_guitar(guitars):
    print("New guitar: ")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Year", "Cost"])
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = "guitars.csv"
    guitars = read_guitar(filename)
    display_guitars(guitars)
    guitars.sort()
    print("Sorted guitars:")
    display_guitars(guitars)
    add_new_guitar(guitars)
    save_guitars(filename, guitars)
    print("Guitars list: ")
    guitars = read_guitar(filename)
    display_guitars(guitars)


main()
#