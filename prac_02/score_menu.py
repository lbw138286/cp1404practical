import random

def main():
    score = get_score()
    while True:
        MENU = """\nMenu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Goodbye.")
            break
        else:
            print("Invalid option. Please choose again.")

def determine_result(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif 50 < score < 90:
        return "Passable"
    elif 0 <= score <= 50:
        return "Bad"
    else:
        return "Invalid score"

def get_score():
    while True:
        score_input = input("Enter score (0-100): ")
        if score_input.replace('.', '', 1).isdigit() and score_input.count('.') < 2:
            score = float(score_input)
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        else:
            print("Invalid input. Please enter a numeric value.")

def show_stars(score):
    stars = '*' * int(score)
    print(stars)

main()
