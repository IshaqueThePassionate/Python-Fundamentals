# 1. Using parentheses () for grouping expressions

result = (2 + 3) * 4  # Parentheses group the expression
print(result)  # Output: 20


# 2. Using square brackets [] for lists and indexing

numbers = [1, 2, 3, 4, 5]  # Creating a list
print(numbers[0])  # Accessing the first element, Output: 1


# 3. Using curly braces {} for dictionaries and sets

student = {"name": "Ali", "age": 18}  # Creating a dictionary
print(student["name"])  # Output: Ali

unique_values = {1, 2, 2, 3, 4}  # Creating a set (removes duplicates)
print(unique_values)  # Output: {1, 2, 3, 4}


# 4. Using colons : in dictionaries and loops

ages = {"Ahmed": 20, "Sara": 22}  # Dictionary with key-value pairs
for key, value in ages.items():
    print(key, "is", value, "years old")  
# Output:
# Ahmed is 20 years old
# Sara is 22 years old


# 5. Using commas , to separate items in lists and function arguments

colors = ["red", "blue", "green"]  # List with multiple items
print(colors)  # Output: ['red', 'blue', 'green']


# 6. Using the dot . for floating-point numbers

pi = 3.14  # Floating-point value
print(pi)  # Output: 3.14


# 7. Using the assignment operator =

x = 10  # Assigning a value to x
y = x + 5  # Performing arithmetic and assignment
print(y)  # Output: 15


# 8. Using semicolon ; for multiple statements (not recommended)

a = 5; b = 10; print(a + b)  # Output: 15


# 9. Using the backslash \ for line continuation

long_text = "This is a very long sentence that we " \
            "can split across multiple lines."
print(long_text)
# Output: This is a very long sentence that we can split across multiple lines.
