# Task 1: Write the user's name to a file
name = input("Please enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Task 2: Read the name from the file and print it
with open('name.txt', 'r') as file:
    name = file.read()
    print(f"Your name is {name}")

# Task 3: Read the first two numbers from numbers.txt and print their sum
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    total = num1 + num2
    print("Sum of the first two numbers in numbers.txt:", total)

# Task 4: Read all numbers from numbers.txt and print their total
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print("Total sum of all numbers in numbers.txt:", total)
