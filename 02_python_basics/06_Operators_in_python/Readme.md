# Operators in Python

Operators in Python, which are symbols or combinations of symbols that perform operations on variables and values. Understanding operators is crucial for working with expressions and performing calculations in Python.

## What are Operators?

- **Operators** are special symbols that instruct Python to perform computations or logical manipulations on values or variables.
- Python provides various types of operators, each serving a distinct purpose in programming logic.

## List of Common Operators in Python

### 1. **Arithmetic Operators**

Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, and division.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Adds two values | `10 + 5` → `15` |
| `-` | Subtracts the second value from the first | `10 - 5` → `5` |
| `*` | Multiplies two values | `10 * 5` → `50` |
| `/` | Divides the first value by the second | `10 / 3` → `3.3333...` |
| `%` | Returns the remainder after division | `10 % 3` → `1` |
| `**` | Raises the first value to the power of the second | `2 ** 3` → `8` |
| `//` | Performs floor division (rounds down) | `10 // 3` → `3` |

#### Example:
```python
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
print(a // b) # Output: 3
```

### 2. **Comparison Operators**

Comparison operators compare two values and return a boolean (`True` or `False`).

| Operator | Description | Example |
|----------|-------------|---------|
| `<` | Checks if the first value is less than the second | `5 < 3` → `False` |
| `<=` | Checks if the first value is less than or equal to the second | `5 <= 5` → `True` |
| `>` | Checks if the first value is greater than the second | `5 > 3` → `True` |
| `>=` | Checks if the first value is greater than or equal to the second | `5 >= 5` → `True` |
| `==` | Checks if two values are equal | `5 == 5` → `True` |
| `!=` | Checks if two values are not equal | `5 != 3` → `True` |

#### Example:
```python
a = 5
b = 3

print(a < b)   # Output: False
print(a <= b)  # Output: False
print(a > b)   # Output: True
print(a >= b)  # Output: True
print(a == b)  # Output: False
print(a != b)  # Output: True
```

### 3. **Logical Operators**

Logical operators are used to perform logical operations on boolean values.

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Returns `True` if both conditions are true | `True and False` → `False` |
| `or` | Returns `True` if at least one condition is true | `True or False` → `True` |
| `not` | Reverses the logical state | `not True` → `False` |

#### Example:
```python
x = True
y = False

print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
```

### 4. **Bitwise Operators**

Bitwise operators perform operations at the binary level.

| Operator | Description | Example |
|----------|-------------|---------|
| `&` | Performs bitwise AND | `5 & 3` → `1` |
| `|` | Performs bitwise OR | `5 | 3` → `7` |
| `^` | Performs bitwise XOR | `5 ^ 3` → `6` |
| `~` | Performs bitwise NOT | `~5` → `-6` |
| `<<` | Performs bitwise left shift | `5 << 1` → `10` |
| `>>` | Performs bitwise right shift | `5 >> 1` → `2` |

#### Example:
```python
a = 5  # 101 in binary
b = 3  # 011 in binary

print(a & b)  # Output: 1  (001 in binary)
print(a | b)  # Output: 7  (111 in binary)
print(a ^ b)  # Output: 6  (110 in binary)
print(~a)     # Output: -6 (bitwise NOT of 5)
print(a << 1) # Output: 10 (Left shift: 1010 in binary)
print(a >> 1) # Output: 2  (Right shift: 010 in binary)
```

### 5. **Assignment Operators**

Assignment operators are used to assign values to variables.

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Assigns a value | `x = 10` |
| `+=` | Adds and assigns | `x += 5` (equivalent to `x = x + 5`) |
| `-=` | Subtracts and assigns | `x -= 5` (equivalent to `x = x - 5`) |
| `*=` | Multiplies and assigns | `x *= 5` |
| `/=` | Divides and assigns | `x /= 5` |
| `//=` | Floor divides and assigns | `x //= 5` |

#### Example:
```python
x = 10
x += 5
print(x)  # Output: 15

x *= 2
print(x)  # Output: 30
```

## Summary

Python provides a wide range of operators that allow for mathematical calculations, logical operations, comparisons, and more. Mastering these operators is essential for writing efficient and powerful Python code. The `@` operator, introduced in Python 3, is used for matrix multiplication, further expanding Python’s capabilities in handling complex mathematical computations.

