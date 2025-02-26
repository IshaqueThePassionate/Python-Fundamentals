# Decision Statements Examples in Python

# --- Simple if Statement ---

print("=== Simple if Statement ===")
voter_age = 19
if voter_age >= 18:
    print("You are old enough to vote!")


# --- if-else Statement ---

print("\n=== if-else Statement ===")
voter_age = 17
if voter_age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")


# --- if-elif-else Chain ---

print("\n=== if-elif-else Chain ===")
age = int(input("Enter your age for ticket pricing: "))
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


# --- Nested if Statements ---

print("\n=== Nested if Statements ===")
age = int(input("Enter your age for eligibility check: "))
if age >= 18:
    if age > 20:
        print("You are eligible for a special adult ticket.")
    else:
        print("You are eligible to vote!")
else:
    print("You are too young to vote.")


# --- Additional Example: Number Parity ---

print("\n=== Number Parity Check ===")
number = int(input("Enter a number to check if it is even or odd: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


our_age = 12

if our_age < 4:
    print("Your admission cost is $0.")
elif our_age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


marks = 85

if marks >= 90:
    print("You got an A grade! 🎉")
elif marks >= 75 and marks < 90:
    print("You got a B grade! 👍")
elif marks >= 60 and marks < 75:
    print("You got a C grade! 👌")
else:
    print("You need to improve. 📚")


mood = "energetic"

if mood == "happy":
    print("How about listening to some pop music? 🎤")
elif mood == "sad":
    print("Try some blues to feel those emotions! 🎷")
elif mood == "energetic":
    print("Rock music is your go-to! 🎸")
elif mood == "relaxed":
    print("Smooth jazz will be perfect for you. 🎹")
else:
    print("Discover some new indie tracks! 🎧")