# Keywords in Python

## What are Keywords?

- **Keywords** are reserved words in Python that have special meanings and cannot be used as regular identifiers (like variable names or function names).
- Python's keywords consist only of **lowercase letters**, except for `True`, `False`, and `None`.

### Python v2 vs. Python v3

- **Python v2** has **31 keywords**.
- **Python v3** has **35 keywords**, including `False`, `True`, `None`, `async`, and `await`.

### Example of Invalid Identifiers:
```python
# Keywords cannot be used as identifiers
# if = 10  # ❌ Invalid: 'if' is a keyword
# def = 20  # ❌ Invalid: 'def' is a keyword
```

## Categories of Keywords

### 1. **Control Flow Keywords**
- `if`, `elif`, `else` – Conditional branching
- `for`, `while` – Looping constructs
- `break`, `continue`, `pass` – Loop control

### 2. **Function and Class Definition Keywords**
- `def` – Function definition
- `class` – Class definition
- `return` – Returns a value from a function

### 3. **Logical and Boolean Keywords**
- `and`, `or`, `not` – Logical operators
- `True`, `False`, `None` – Boolean values and null representation

### 4. **Exception Handling Keywords**
- `try`, `except`, `finally`, `raise`, `assert` – Error handling

### 5. **Asynchronous Programming Keywords**
- `async`, `await` – Asynchronous execution (Python 3.5+)

## Python v3 Keywords
```plaintext
and       as         assert    async     await    break
class     continue   def       del       elif     else
except    False      finally   for       from     global
if        import     in        is        lambda   None
nonlocal  not        or        pass      raise    return
True      try        while     with      yield
```

## Reserved Nature of Keywords
Python reserves certain words for specific functionalities. Trying to use them as identifiers will result in a **SyntaxError**.

### Example 1: Attempting to Use a Keyword as a Variable Name
```python
# Invalid example: 'for' is a reserved keyword
# for = 10  # ❌ SyntaxError: invalid syntax
```

### Example 2: Using Keywords Correctly in a Program
```python
# Using 'def' correctly to define a function
def my_function():
    return "This is a valid function definition."

# Using 'class' to define a class
class MyClass:
    pass

# Using 'if', 'else' in conditional statements
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

### Example 3: Keywords vs Identifiers
```python
# Valid identifier
my_var = 20  # 'my_var' is allowed

# Invalid identifier
# return = 50  # ❌ SyntaxError: invalid syntax (reserved keyword)
```