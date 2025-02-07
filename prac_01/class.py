"""
get number of gift, number of student
gifts = number_of_gift // number_of_student
rest_gifts = number_of_gift % number_of_student
display "Every students get {gifts} gifts, {rest_gifts} gifts left."
"""
number_of_gift = int(input("Enter the number of the gifts:"))
number_of_student = int(input("Enter the number of the students:"))
gifts = number_of_gift // number_of_student
rest_gifts = number_of_gift % number_of_student
print(f"Every students get {gifts} gifts, {rest_gifts} gifts left.")



numbers = input("Enter the number:")
for i in range (1, numbers + 1):
    print(i, end=' ')

count = 5
get_the_number = int(input("Guess the number"))
while get_the_number != count:
    print("Guess again")
    get_the_number = int(input("Guess the number"))
    print("You are right")
if 0 < get_the_number < 10:
    print("Invalid number")


name = input("Enter your name:").upper()
while name == "":
    print("Name cannot be empty")
    name = input("Enter your name:").upper()
salary = float(input("Enter your salary:"))
while salary < 0:
    print("Salary cannot less than 0")
    salary = float(input("Enter your salary:"))
print(name)
print(f"{salary:.2f}")

total_age = 0
number_of_ages = int(input("Enter number of ages:"))
for i in range(number_of_ages):
    age = int(input("Enter age:"))
    total_age += age
average_age = total_age / number_of_ages
print(total_age)
print(average_age)


