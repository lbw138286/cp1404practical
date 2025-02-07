import random

def main():
    score = get_score()
    result = determine_result(score)
    print(f"Result: {result}")

    random_score = random.randint(0, 100)

    random_result = determine_result(random_score)
    print(f"Random score ({random_score}): {random_result}")

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
        score_input = input("Enter score: ")
        if score_input.replace('.', '', 1).isdigit() and score_input.count('.') < 2:
            return float(score_input)
        else:
            print("Invalid input. Please enter a numeric value.")

main()
