# Object Creation and Type Checking

# Creating an integer and a string object
x = 42            # 'x' is an integer object
y = "Hello"       # 'y' is a string object

print("x:", x, "Type:", type(x))
print("y:", y, "Type:", type(y))

# Demonstrating immutability with integers and strings

# For integers
x = 42                   # Original integer
original_x = x           # Preserve the original value
x = x + 1                # x now references a new integer (43)
print("Modified x:", x)
print("Original x:", original_x)

# For strings
y = "Hello"              # Original string
original_y = y           # Preserve the original value
y += " World"            # y now references a new string ("Hello World")
print("Modified y:", y)
print("Original y:", original_y)

# Using type() and isinstance() for type checking
print("Is x an int?", isinstance(x, int))
print("Is y a str?", isinstance(y, str))

# Numeric Data Types Examples

# Integer literals in different bases
decimal_int = 23
binary_int = 0b1010      # Binary literal
octal_int = 0o27         # Octal literal
hex_int = 0x1F           # Hexadecimal literal

print("Decimal integer:", decimal_int)
print("Binary integer:", binary_int)
print("Octal integer:", octal_int)
print("Hexadecimal integer:", hex_int)

# Floating-point numbers and scientific notation
float_num = 3.14159
sci_notation1 = 1e3      # 1e3 equals 1000
sci_notation2 = 2.5e-2   # 2.5e-2 equals 0.025

print("Floating-point number:", float_num)
print("Scientific notation (1e3):", sci_notation1)
print("Scientific notation (2.5e-2):", sci_notation2)

# Complex numbers
complex_num = 1 + 2j
print("Complex number:", complex_num)

# Using underscores in numeric literals for readability (Python 3.6+)
large_number = 100_000
readable_hex = 0x_FF_FF  # Underscores can be used in hex literals too
print("Large number with underscores:", large_number)
print("Hexadecimal with underscores:", readable_hex)

# String Examples

# Different ways to define strings
single_quoted = 'Hello'
double_quoted = "World"
triple_quoted = """This is a
multi-line string example."""

print("Single-quoted string:", single_quoted)
print("Double-quoted string:", double_quoted)
print("Triple-quoted string:\n", triple_quoted)

# Boolean Data Type Examples

# Boolean values and logical operations
is_python_fun = True
print("Boolean value:", is_python_fun)
print("Boolean with AND:", is_python_fun and False)
print("Boolean with NOT:", not is_python_fun)
Below is your modified README file with all emojis removed and a brief explanation provided immediately after each heading, without using the word "Definition":

---

# Variables and Other References in Python

This section explains how Python uses variables and references to access and manipulate data values within programs.

In this section, we examine how Python programs access and manipulate data through **references**. Understanding how variables and references work is essential for effective Python programming.

## References in Python

A reference in Python is a label or name that points to a specific object in memory, enabling dynamic and flexible data management.

- A **reference** is essentially a label that points to a value (object) in Python.
- **References** can appear as variables, attributes, or items.
- In Python, a reference itself does not have an intrinsic type; the type is determined by the object to which it currently points.
- Over the course of a program’s execution, a single reference may be associated with objects of different types.

### Example:
```python
value = 42       # 'value' is a reference to an integer object
value = "hello"  # 'value' now references a string object
```

## Variables in Python

Variables in Python are names that refer to objects. They are created by assignment and can be rebound to different objects as needed.

- In Python, variables are simply **references** to objects. Unlike some other programming languages, there are no explicit variable declarations.
- A variable comes into existence when it is **bound** to an object.
- Variables can be **rebound** to new objects, and they can also be **unbound**, meaning they no longer refer to any object.

### Binding and Rebinding

- **Binding:** The process of associating a variable with an object.
- **Rebinding:** Assigning a new object to a variable that already has a binding.

### Example:
```python
num = 10    # Binding: 'num' refers to the integer 10
num = 20    # Rebinding: 'num' now refers to the integer 20
```

Unbinding is the process of removing the association between a variable and an object, typically using the `del` statement.

### Example:
```python
item = 10   # 'item' refers to the integer 10
del item    # 'item' is now unbound; the name no longer exists
```

When a reference is unbound, the object it pointed to may be reclaimed by Python's garbage collector if no other references exist.

### Example:
```python
list_obj = [1, 2, 3]  # 'list_obj' refers to a list object
alias = list_obj      # 'alias' also refers to the same list object
del list_obj          # 'list_obj' is unbound, but the list remains because 'alias' still references it
```

## Naming Variables

Variable names in Python must follow the rules for identifiers and cannot be reserved keywords. Variables are categorized by their scope:

- **Global Variables:** Accessible throughout the entire module; they are attributes of the module.
- **Local Variables:** Accessible only within the function in which they are defined.

### Example:
```python
message = "Global Message"  # Global variable

def show_message():
    note = "Local Note"     # Local variable
    print("Inside function:", note)
    print("Inside function accessing global variable:", message)

show_message()          # Displays both local and global messages
print("Outside function:", message)
```

---

This section has covered the concepts of **variables** and **references** in Python, detailing how they are bound, rebound, and unbound. A clear grasp of these topics is essential for managing data and memory efficiently in Python programs.