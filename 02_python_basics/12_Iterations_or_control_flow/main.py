## Combined Code Examples for main.py

# Combined Loop Examples in Python

# --- For Loop Examples ---
print("=== For Loop Examples ===")
# Multiplication table for 5 using a for loop
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

print()  # Blank line for separation

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}!")

print()  # Blank line for separation

# Using range() to print even numbers from 2 to 20
for number in range(2, 21, 2):
    print(number)

# --- While Loop Examples ---
print("\n=== While Loop Examples ===")
# Multiplication table for 5 using a while loop
number = 1
while number <= 10:
    print(f"5 x {number} = {5 * number}")
    number += 1

print()  # Blank line for separation

# User input to calculate the square of a number
prompt = "Enter a number to get its square (or 'quit' to stop): "
while True:
    user_input = input(prompt)
    if user_input.lower() == 'quit':
        break
    number = int(user_input)
    print(f"The square of {number} is {number ** 2}")

print()  # Blank line for separation

# Using continue in a while loop to print odd numbers only
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# --- Nested Loop Examples ---
print("\n=== Nested Loop Examples ===")
# Multiplication Table Generator with user control
print("Welcome to the Multiplication Table Generator!")
while True:
    table_number = int(input("\nEnter a number for its multiplication table: "))
    print(f"\nMultiplication Table for {table_number}")
    for i in range(1, 11):
        print(f"{table_number} x {i} = {table_number * i}")
    
    continue_choice = input("\nDo you want to print another table? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting the Multiplication Table Generator. Thank you!")
        break

print()  # Blank line for separation

# Pyramid Pattern Generator with user control
print("Welcome to the Pyramid Pattern Generator!")
while True:
    height = int(input("\nEnter the height of the pyramid: "))
    print(f"\nPyramid of height {height}\n")
    for i in range(1, height + 1):
        print(" " * (height - i), end='')
        print("*" * (2 * i - 1))
    
    continue_choice = input("\nDo you want to create another pyramid? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting the Pyramid Pattern Generator. Thank you!")
        break
