"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    subject_data = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            subject_data.append(parts)
    return subject_data


def display_subject_details(data):
    for subject in data:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")
main()
