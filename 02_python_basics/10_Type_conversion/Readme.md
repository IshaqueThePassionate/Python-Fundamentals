# Type Conversion in Python

This document explains how to convert values between different data types in Python. It covers both implicit and explicit conversion, including examples where user input is taken and converted.

## Overview

Type conversion is the process of converting a value from one data type to another. In Python, this can occur in two ways:
- **Implicit Conversion:** Python automatically converts data types during operations, such as converting an integer to a float during arithmetic.
- **Explicit Conversion:** You manually convert values using built-in functions like `int()`, `float()`, `str()`, and others.

## Implicit Type Conversion

Python performs implicit type conversion when it automatically changes one data type into another to avoid errors during operations. For example, when an integer and a float are used together in an arithmetic operation, the integer is automatically converted to a float.

### Example:
```python
a = 5       # integer
b = 2.5     # float
result = a + b   # 'a' is implicitly converted to float
print("Result of implicit conversion:", result)  # Output: 7.5
```

## Explicit Type Conversion

Explicit conversion is when you use a function to change the type of a value. This method provides full control over how the conversion is performed. Common functions include:

- `int()` – converts a value to an integer.
- `float()` – converts a value to a float.
- `str()` – converts a value to a string.
- `list()` and `tuple()` – convert iterables to a list or tuple.

### Examples:
```python
# Converting a string to an integer
num_str = "100"
num_int = int(num_str)
print("Converted string to integer:", num_int)  # Output: 100

# Converting a float to an integer (decimal part is truncated)
flt = 3.14
int_flt = int(flt)
print("Converted float to integer:", int_flt)   # Output: 3

# Converting an integer to a float
int_val = 10
flt_val = float(int_val)
print("Converted integer to float:", flt_val)   # Output: 10.0

# Converting a number to a string
number = 2021
str_number = str(number)
print("Converted number to string:", str_number)  # Output: "2021"

# Converting a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("Converted list to tuple:", my_tuple)      # Output: (1, 2, 3)
```

## Input Conversion Examples

When taking input from users, the value returned by the `input()` function is always a string. You can convert this input to another type as needed.

### Examples:
```python
# Converting user input to an integer
user_input = input("Enter an integer: ")
converted_int = int(user_input)
print("User input converted to integer:", converted_int)

# Converting user input to a float
user_input = input("Enter a floating-point number: ")
converted_float = float(user_input)
print("User input converted to float:", converted_float)
```


