# Tokens in Python

## What Are Tokens?

- Python divides each **logical line** into a sequence of basic lexical elements called **tokens**.
- Each token represents a specific substring of the logical line.

### Types of Tokens

The primary types of tokens in Python include:

1. **Identifiers**: Names assigned to variables, functions, classes, etc.
2. **Keywords**: Reserved words with special meanings in Python (e.g., `if`, `else`, `while`).
3. **Operators**: Symbols used for performing operations on variables and values (e.g., `+`, `-`, `*`, `/`).
4. **Delimiters**: Characters that separate tokens (e.g., `()`, `[]`, `{}`, `,`).
5. **Literals**: Fixed values such as numbers, strings, and booleans.

## The Role of Whitespace

- **Whitespace** (spaces, tabs, and newlines) is used to separate tokens and improve readability.
- Some whitespace is **mandatory** to distinguish adjacent identifiers or keywords.

### Examples:
```python
# Incorrect: Python would interpret 'ifx' as a single identifier
ifx = 10

# Correct: Adding whitespace to separate 'if' and 'x'
if x == 10:
    print("x is 10")
```

- In the above example, omitting the space between `if` and `x` would cause Python to interpret `ifx` as a single identifier instead of recognizing `if` as a keyword and `x` as a variable.



