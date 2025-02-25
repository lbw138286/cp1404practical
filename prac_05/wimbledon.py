"""
Wimbledon Data Processing
Writing Code: 90 minutes
Debugging: 30 minutes
Total: 120 minutes
"""
import csv
from collections import defaultdict

def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champion_counts = count_champions(data)
    countries = get_countries(data)
    display_results(champion_counts, countries)

def read_csv_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        data = [row for row in reader]
    return data

def count_champions(data):
    champion_counts = defaultdict(int)
    for row in data:
        champion = row[2]
        champion_counts[champion] += 1
    return champion_counts

def get_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)

def display_results(champion_counts, countries):
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_counts.items()):
        print(f"{champion} {count}")
    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(countries))
main()