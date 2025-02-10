# 1
name = input("What is your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# 2
file = open('name.txt', 'r')
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")

# 3
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
result = num1 + num2
print(result)

# 4
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())
print(total)
