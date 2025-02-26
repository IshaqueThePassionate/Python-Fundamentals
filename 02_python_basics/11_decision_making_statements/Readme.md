# Understanding Decision Statements in Python

This document explains how decision statements work in Python. Decision statements allow your program to execute different code blocks based on certain conditions. In this guide, we cover the fundamentals of conditional tests and the various types of decision statements available, including simple `if` statements, `if-else` statements, `if-elif-else` chains, and nested `if` statements.

## Understanding Conditional Tests

Conditional tests evaluate expressions to either `True` or `False`. Python uses these Boolean results to determine which blocks of code to execute.

### What is a Conditional Test?

A conditional test is an expression that returns either `True` or `False`. These tests are the foundation of decision making in Python programs.

### Types of Conditional Tests

1. **Equality Tests (`==`):**
   - Checks if two values are equal.
   - Example: `5 == 5` returns `True`; `5 == 4` returns `False`.

2. **Inequality Tests (`!=`):**
   - Checks if two values are not equal.
   - Example: `5 != 4` returns `True`; `5 != 5` returns `False`.

3. **Greater Than and Less Than Tests (`>`, `<`):**
   - Compares two values.
   - Example: `7 > 5` returns `True`; `3 < 2` returns `False`.

4. **Greater Than or Equal To and Less Than or Equal To Tests (`>=`, `<=`):**
   - Checks if one value is greater than or equal to, or less than or equal to another.
   - Example: `5 >= 5` returns `True`; `3 <= 4` returns `True`.

5. **Boolean Tests (`and`, `or`, `not`):**
   - Combines multiple conditions.
   - `and`: Both conditions must be true.
   - `or`: At least one condition must be true.
   - `not`: Inverts the Boolean value.
   - Example: `(5 > 3) and (2 < 4)` returns `True`; `(5 > 3) and (2 > 4)` returns `False`.

### Ignoring Case in Conditional Tests

When comparing strings, conditional tests are case-sensitive. Use the `.lower()` method to ignore case differences.

```python
name = 'Alice'
print(name == 'alice')         # Returns False (case-sensitive)
print(name.lower() == 'alice') # Returns True (ignoring case)
```

## Simple `if` Statements

An `if` statement tests a condition. If the condition is true, the corresponding block of code is executed; if it is false, the block is skipped.

### Example: Checking Voting Eligibility

```python
age = 19

if age >= 18:
    print("You are old enough to vote!")
```

## `if-else` Statements

An `if-else` statement provides an alternative block of code that executes when the condition is false.

### Example: Voting Eligibility with Feedback

```python
age = 17

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
```

## `if-elif-else` Chains

When you have multiple conditions to check, use an `if-elif-else` chain. Python evaluates each condition in order and executes the first block where the condition is true.

### Example: Amusement Park Ticket Pricing

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
```

## Nested `if` Statements

Nested `if` statements are `if` statements within another `if` block. This structure allows you to check for multiple related conditions.

### Example: Admission Eligibility and Special Ticket Offers

```python
age = 21

if age >= 18:
    if age > 20:
        print("You are eligible for a special adult ticket.")
    else:
        print("You are eligible to vote!")
else:
    print("You are too young to vote.")
```

## Additional Real-World Use Cases

1. **Login Systems:** Check if the username and password match stored values.
2. **E-commerce:** Determine if a user qualifies for free shipping (e.g., `cart_total > 50` and `location == 'domestic'`).
3. **Game Development:** Check a player's status (e.g., `health > 0` and `level >= 5`).

