# Delimiters in Python

## Definition

A **delimiter** in Python is a symbol or a combination of symbols used to separate elements within a program. These delimiters help define expressions, lists, dictionaries, sets, function calls, and statements, ensuring proper syntax and logical structure within the code.

## Common Delimiters in Python

Python uses the following characters as delimiters:

| **Delimiter** | **Purpose/Usage**                                                                 |
|---------------|-----------------------------------------------------------------------------------|
| `()`          | Used for grouping expressions, function calls, and tuples.                        |
| `[]`          | Used for indexing, slicing, and list literals.                                    |
| `{}`          | Used for dictionary and set literals, as well as formatting strings.              |
| `,`           | Used to separate items in lists, tuples, dictionaries, function arguments, etc.   |
| `:`           | Used in dictionaries to separate keys and values, and in various statements like `for`, `if`, and function definitions. |
| `.`           | Used for accessing object attributes or methods, and for floating-point literals. |
| `=`           | Used for assignment.                                                              |
| `;`           | Used to separate multiple statements on a single line.                            |
| `@`           | Used for decorators.                                                              |

### Example Usage of Delimiters
```python
# Using parentheses for function calls
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!

# Using square brackets for lists and indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana

# Using curly braces for dictionaries
data = {"name": "Alice", "age": 25}
print(data["name"])  # Output: Alice
```

## Augmented Assignment Operators

Python also uses augmented assignment operators, which are a combination of a delimiter and an operation. These operators perform an operation and then assign the result to a variable.

| **Operator** | **Description**                                     |
|--------------|-----------------------------------------------------|
| `+=`         | Adds and assigns (e.g., `x += 2` is equivalent to `x = x + 2`). |
| `-=`         | Subtracts and assigns (e.g., `x -= 2` is equivalent to `x = x - 2`). |
| `*=`         | Multiplies and assigns (e.g., `x *= 2` is equivalent to `x = x * 2`). |
| `/=`         | Divides and assigns (e.g., `x /= 2` is equivalent to `x = x / 2`). |
| `//=`        | Floor divides and assigns (e.g., `x //= 2` is equivalent to `x = x // 2`). |
| `%=`         | Takes modulus and assigns (e.g., `x %= 2` is equivalent to `x = x % 2`). |
| `**=`        | Exponentiates and assigns (e.g., `x **= 2` is equivalent to `x = x ** 2`). |

### Example Usage of Augmented Assignment Operators
```python
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15

x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 30
```

## Special Characters and Their Uses

Certain characters have specific meanings as part of other tokens in Python:

| **Character** | **Special Meaning**                                                                 |
|---------------|-------------------------------------------------------------------------------------|
| `'`           | Surrounds string literals.                                                          |
| `"`           | Surrounds string literals.                                                          |
| `#`           | Starts a comment outside of a string.                                               |
| `\`           | Used at the end of a physical line to join the next line into a single logical line. Also acts as an escape character in strings. |

### Example:
```python
# This is a comment

text = "Hello, World!"  # Double quotes for string
path = 'C:\\Users\\Hashim\\Documents'  # Escape character in string
```

## Restrictions on Certain Characters

Some characters are not allowed in the main text of a Python program (except in comments or string literals):

- `$` and `?` are not valid in identifiers or expressions.
- All control characters (except whitespace) are restricted.
- In Python 2, all characters with ISO codes above 126 (non-ASCII characters, like accented letters) were not allowed in identifiers.


