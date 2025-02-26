# Control Flows - Loops

## What are Iterations or Loops?

Iterations, or loops, allow you to execute a block of code repeatedly. They are essential for reducing repetition, handling variable-sized input, automating tasks, and improving code efficiency. Instead of writing the same code many times, loops let you write it once and run it repeatedly.

## Why Do We Need Iterations with Loops?

- **Reduce Repetition:** Instead of writing multiple print statements, a loop can perform the task in a single, concise block.
- **Dynamic Behavior:** Loops can process items from a list or lines in a file regardless of how many items there are.
- **Automation:** They automate repetitive tasks, such as calculating values or processing user input.
- **Efficiency:** Loops make code easier to modify and maintain since changes need to be made in only one place.

## Types of Loops in Python

Python offers different kinds of loops:

| Sr.No. | Name of the Loop | Description |
|--------|------------------|-------------|
| 1      | While Loop       | Repeats a block of code while a condition remains True. The condition is checked before every iteration. |
| 2      | For Loop         | Iterates over a sequence (like a list, string, or range) a fixed number of times. |
| 3      | Nested Loops     | A loop inside another loop, used to handle multi-dimensional data or more complex iterations. |

## Loop Control Statements

Loop control statements change the flow of loops:

| Sr.No. | Control Statement | Description |
|--------|-------------------|-------------|
| 1      | Break             | Exits the loop immediately. |
| 2      | Continue          | Skips the rest of the code in the current iteration and moves to the next iteration. |
| 3      | Pass              | A placeholder that does nothing; useful when a statement is required syntactically. |

## The `range()` Function

The `range()` function generates a sequence of numbers. It is commonly used with loops.

- **Syntax:** `range(start, stop, step)`
  - **start:** Beginning of the sequence (default is 0).
  - **stop:** End of the sequence (not included in the output).
  - **step:** The increment between each number (default is 1).

### Example:
```python
print(list(range(10)))       # Generates numbers 0 to 9.
print(list(range(4, 9)))      # Generates numbers 4 to 8.
print(list(range(5, 25, 4)))   # Generates numbers starting at 5, increasing by 4 until less than 25.
```

**How It Works:**  
- The first example prints numbers from 0 up to 9.  
- The second example starts at 4 and prints up to 8.  
- The third example starts at 5 and adds 4 each time until the next number would be 25 or more.

## For Loops

For loops iterate over sequences like lists, strings, or ranges.

### Example: Printing a Multiplication Table
```python
# Multiplication table for 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
```

**Flow Explanation:**  
- The loop starts with `i = 1` and checks if `i` is less than 11.
- For each value of `i`, it calculates the product of 5 and `i` and prints the result.
- `i` is automatically incremented until it reaches 11, at which point the loop stops.

### Example: Iterating Over a List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}!")
```

**Flow Explanation:**  
- The loop iterates over each item in the list `fruits`.
- In each iteration, the variable `fruit` takes the value of the next item in the list.
- The print statement outputs a message including the current fruit.

### Example: Using `range()` to Loop Over Indices
```python
# Print even numbers from 2 to 20
for number in range(2, 21, 2):
    print(number)
```

**Flow Explanation:**  
- The `range()` function generates numbers starting at 2, ending before 21, in steps of 2.
- The loop iterates over each generated number and prints it.
- This produces all even numbers between 2 and 20.

## While Loops

While loops run as long as a specified condition is True.

### Example: Printing a Multiplication Table Using a While Loop
```python
number = 1
while number <= 10:
    print(f"5 x {number} = {5 * number}")
    number += 1
```

**Flow Explanation:**  
- The loop begins with `number = 1`.
- It checks if `number` is less than or equal to 10.
- If the condition is True, it prints the multiplication line and increments `number` by 1.
- This process repeats until `number` exceeds 10, then the loop stops.

### Example: User Input with a While Loop
```python
prompt = "Enter a number to get its square (or 'quit' to stop): "

while True:
    user_input = input(prompt)
    if user_input.lower() == 'quit':
        break
    number = int(user_input)
    print(f"The square of {number} is {number ** 2}")
```

**Flow Explanation:**  
- The loop continuously asks the user for input.
- If the user types "quit" (in any case), the condition triggers a `break` to exit the loop.
- Otherwise, the input is converted to an integer, and its square is computed and printed.
- The loop then repeats, prompting the user again.

### Example: Using `continue` in a While Loop
```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # Skip printing even numbers
    print(current_number)
```

**Flow Explanation:**  
- The loop starts with `current_number = 0`.
- In each iteration, it increments `current_number` by 1.
- If `current_number` is even (i.e., divisible by 2), the `continue` statement skips the print function and moves to the next iteration.
- Only odd numbers are printed until `current_number` reaches 10.

### Avoiding Infinite Loops
```python
x = 1
while x <= 5:
    print(x)
    x += 1  # Ensures the loop stops once x becomes greater than 5
```

**Flow Explanation:**  
- The loop prints the value of `x` as long as `x` is less than or equal to 5.
- The increment `x += 1` is crucial; without it, the condition would remain True indefinitely, resulting in an infinite loop.

## Nested Loops

Nested loops are loops within loops, useful for complex iterations like processing multi-dimensional data.

### Example: Multiplication Table Generator
```python
print("Welcome to the Multiplication Table Generator!")

while True:
    number = int(input("\nEnter a number for its multiplication table: "))
    print(f"\nMultiplication Table for {number}")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    
    continue_choice = input("\nDo you want to print another table? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Let's print another table!")
```

**Flow Explanation:**  
- The outer while loop continually asks the user for a number.
- Once a number is provided, the inner for loop generates and prints the multiplication table for that number.
- After printing, the program asks if the user wants to print another table.
- If the user types anything other than "yes", the loop breaks; otherwise, the process repeats.

### Example: Pyramid Pattern Generator
```python
print("Welcome to the Pyramid Pattern Generator!")

while True:
    height = int(input("\nEnter the height of the pyramid: "))
    print(f"\nPyramid of height {height}\n")
    for i in range(1, height + 1):
        # Print spaces for alignment
        print(" " * (height - i), end='')
        # Print stars to form the pyramid
        print("*" * (2 * i - 1))
    
    continue_choice = input("\nDo you want to create another pyramid? (yes/no): ").strip().lower()
    if continue_choice != 'yes':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Let's build another pyramid!")
```

**Flow Explanation:**  
- The outer while loop prompts the user for the desired pyramid height.
- The inner for loop prints each row of the pyramid:
  - It first prints a number of spaces to right-align the stars.
  - Then it prints an increasing number of stars to form the pyramid shape.
- After printing, the user is asked if they want to generate another pyramid.
- The loop repeats or terminates based on the user's input.

