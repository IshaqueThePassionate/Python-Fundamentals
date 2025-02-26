# Identifiers in Python

In this section, we'll explore what **identifiers** are in Python and how to use them correctly. Identifiers are fundamental in Python as they represent variables, functions, classes, and other objects.

## What is an Identifier?

- An **identifier** is a name used to specify a variable, function, class, module, or any other object in Python.
- **Identifiers** help in naming various entities in your Python code, making it easier to reference them later.
- They provide structure and readability to code, enabling maintainability and consistency.

## Rules for Creating Identifiers

- An identifier must start with:
  - A letter (A-Z or a-z in Python 2).
  - An underscore `_`.
  - In Python 3, any character classified as a letter by Unicode can also be used to start an identifier.

- After the first character, an identifier can include:
  - Letters (A-Z, a-z).
  - Digits (0-9).
  - Underscores `_`.
  - In Python 3, Unicode characters classified as digits or combining marks are also allowed.

- **Case Sensitivity**: Identifiers are case-sensitive, meaning `studentName`, `StudentName`, and `STUDENTNAME` are all distinct.

- **Punctuation**: Characters like `@`, `$`, and `!` are **not allowed** in identifiers.

### Examples:
```python
student_age = 18  # Valid identifier
Student_Age = 21   # Another valid identifier (case-sensitive distinction)
# 1stRank = 5  # Invalid identifier (cannot start with a digit)
अंक = 10  # Valid Unicode identifier
رقم = 15  # Another valid Unicode identifier
sum_result = अंक + رقم
print(sum_result)  # Unicode identifiers are allowed in Python 3
```

## Naming Conventions

- **Class Names**: Typically start with an uppercase letter.
- **Other Identifiers**: Typically start with a lowercase letter.
- **Constants**: Conventionally written in all uppercase letters (e.g., `PI = 3.1416`).

### Example:
```python
class StudentProfile:  # Class name starts with an uppercase letter
    pass

def calculate_score():  # Function name starts with a lowercase letter
    pass

MAX_LIMIT = 100  # Constant identifier using uppercase letters
```

### Private Identifiers

- Starting an identifier with a single leading underscore `_` indicates that the identifier is intended to be **private**.
- Starting with two leading underscores `__` indicates a **strongly private** identifier.
- If an identifier starts and ends with double underscores `__name__`, it is a **language-defined special name**.

### Example:
```python
_internal_value = 50  # Indicates a private variable
__secure_data = "Secret"  # Indicates a strongly private variable
__str__ = "Special method in Python"  # Special language-defined name
```

## Special Use of Underscore in Interactive Sessions

- In the interactive Python interpreter, the identifier `_` (a single underscore) is special.
- It is automatically bound to the result of the last evaluated expression.

### Example:
```python
>>> 10 + 5
15
>>> _ * 2
30  # _ refers to the last result, which was 15
```

---

This section provided an in-depth overview of **identifiers** in Python, including the rules for creating them, best practices, and naming conventions. Proper use of identifiers ensures that your Python code remains structured, readable, and maintainable.

