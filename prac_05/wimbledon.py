"""
Wimbledon Champions Data Processor
Writing Code: 20 minutes
Debugging: 15 minutes
Total: 35 minutes
"""
FILENAME = "wimbledon.csv"
def main():
    data = read_wimbledon_data(FILENAME)
    champion_counts, champion_countries = process_wimbledon_data(data)
    display_results(champion_counts, champion_countries)

def read_wimbledon_data(filename):
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()[1:]  # Skip header
    return [line.strip().split(",") for line in lines]

def process_wimbledon_data(data):
    champion_counts = {}
    champion_countries = set()
    for year, country, champion in data:
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
        champion_countries.add(country)
    return champion_counts, champion_countries

def display_results(champion_counts, champion_countries):
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_counts.items()):
        print(f"{champion} {wins}")
    print("\nThese", len(champion_countries), "countries have won Wimbledon:")
    print(", ".join(sorted(champion_countries)))
main()
