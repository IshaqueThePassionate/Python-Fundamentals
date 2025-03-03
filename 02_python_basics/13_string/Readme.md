# Using Python to Manipulate Strings

Python provides powerful ways to manipulate strings, allowing you to perform a variety of operations. This document explains how strings work in Python—including their creation, indexing, methods, formatting, escape sequences, and raw strings—with detailed code examples and explanations for each section.

---

## Creating Strings in Python

Strings can be created using single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`). Triple quotes are especially useful for creating multiline strings or docstrings.

### Example:
```python
# Using single quotes
str1 = 'Hello Python'
print(str1)  # Output: Hello Python

# Using double quotes
str2 = "Hello Python"
print(str2)  # Output: Hello Python

# Using triple quotes for multiline strings
str3 = '''Triple quotes are generally used for
multiline strings or docstrings.'''
print(str3)
```

**Explanation:**  
- The first two examples show that both single and double quotes can be used to create strings that print identically.  
- The triple-quoted string spans multiple lines, which is useful for long texts or documentation.

---

## Strings Indexing and Splitting

Python strings are sequences, and each character in the string can be accessed by its index. Indexing starts at `0` for the first character, and negative indices allow access from the end.

### Example:
```python
text = "HELLO"

# Positive indexing
print(text[0])  # Output: H
print(text[1])  # Output: E

# Negative indexing
print(text[-1])  # Output: O
print(text[-2])  # Output: L
```

**Explanation:**  
- `text[0]` accesses the first character 'H'.  
- `text[-1]` accesses the last character 'O'.  
This demonstrates how both positive and negative indexing work for accessing string characters.

---

## String Methods

Python provides many built-in methods for manipulating strings. These methods return new strings and do not modify the original string.

### Example:
```python
s = "hello world"

# Capitalize: Convert the first character to uppercase.
print(s.capitalize())  # Output: Hello world

# Uppercase: Convert the entire string to uppercase.
print(s.upper())  # Output: HELLO WORLD

# Find: Locate the substring "world".
print(s.find("world"))  # Output: 6

# Replace: Substitute "world" with "Python".
print(s.replace("world", "Python"))  # Output: hello Python
```

**Explanation:**  
- `capitalize()` changes only the first letter of the string.  
- `upper()` transforms all characters to uppercase.  
- `find()` returns the starting index of the substring "world" (which is 6).  
- `replace()` creates a new string where "world" is replaced with "Python".

---

## String Indexing and Slicing

You can access individual characters or subsets of a string using indexing and slicing.

### Example:
```python
word = 'Didcoding'

# Accessing individual characters
print(word[0])  # Output: D
print(word[5])  # Output: d

# Slicing: Get a substring from index 0 to 2 (excluding index 2).
print(word[0:2])  # Output: Di

# Slicing: Get a substring from index 2 to 5 (excluding index 5).
print(word[2:5])  # Output: dco

# Slicing with step: Reverse the string.
print(word[::-1])  # Output: gnidcoDiD
```

**Explanation:**  
- `word[0:2]` extracts the first two characters of the string.  
- `word[2:5]` extracts a section from the string.  
- The slice `[::-1]` reverses the string by stepping backwards.

---

## String Operators

Python supports several operators for string manipulation, including concatenation, repetition, and membership testing.

### Example:
```python
str1 = "Hello"
str2 = " World"

# Concatenation: Combine strings using +
print(str1 + str2)  # Output: Hello World

# Repetition: Repeat string using *
print(str1 * 3)  # Output: HelloHelloHello

# Membership: Check if a substring exists within a string.
print('H' in str1)  # Output: True
```

**Explanation:**  
- The `+` operator concatenates two strings together.  
- The `*` operator repeats a string a specified number of times.  
- The `in` operator tests whether a character or substring is present in a string.

---

## String Formatting

Python offers several methods to format strings. Two common techniques are using the `format()` method and the `%` operator.

### Using the `format()` Method:
```python
name1 = "Hamza"
name2 = "Hashim"

# Using positional arguments.
print("{} and {} are best friends.".format(name1, name2))
# Output: Hamza and Hashim are best friends.

# Using keyword arguments.
print("{a} and {b} are best friends.".format(a="Hamza", b="Hashim"))
# Output: Hamza and Hashim are best friends.
```

**Explanation:**  
- The `format()` method replaces placeholders `{}` with the provided values.  
- Positional arguments fill the placeholders in order; keyword arguments let you explicitly assign values.

### Using the `%` Operator:
```python
integer = 10
floating = 1.29
string = "Hamza"

print("Integer: %d, Float: %f, String: %s" % (integer, floating, string))
# Output: Integer: 10, Float: 1.290000, String: Hamza
```

**Explanation:**  
- The `%` operator formats the string by inserting values into the format specifiers `%d`, `%f`, and `%s`.

---

## Escape Sequences in Strings

Escape sequences allow you to include special characters in strings by using a backslash (`\`) followed by a character.

### Common Escape Sequence Examples:

1. **Newline (`\n`)**
   ```python
   print("Hello\nWorld")
   # Output:
   # Hello
   # World
   ```
   **Explanation:**  
   Moves the text after `\n` to a new line.

2. **Tab (`\t`)**
   ```python
   print("Hello\tWorld")
   # Output: Hello   World
   ```
   **Explanation:**  
   Inserts a horizontal tab space between words.

3. **Backslash (`\\`)**
   ```python
   print("This is a backslash: \\")
   # Output: This is a backslash: \
   ```
   **Explanation:**  
   Displays a single backslash by escaping it with another backslash.

4. **Single Quote (`\'`)**
   ```python
   print('It\'s a sunny day!')
   # Output: It's a sunny day!
   ```
   **Explanation:**  
   Allows a single quote to be included in a string defined with single quotes.

5. **Double Quote (`\"`)**
   ```python
   print("She said, \"Hello!\"")
   # Output: She said, "Hello!"
   ```
   **Explanation:**  
   Allows double quotes within a double-quoted string.

6. **Carriage Return (`\r`)**
   ```python
   print("Hello\rWorld")
   # Output: World
   ```
   **Explanation:**  
   Moves the cursor to the beginning of the line, so subsequent text overwrites it.

7. **Backspace (`\b`)**
   ```python
   print("Hello\bWorld")
   # Output: HellWorld
   ```
   **Explanation:**  
   Deletes the character immediately before it.

8. **Unicode and Hexadecimal Escapes**
   ```python
   print("\u03A9")        # Output: Ω (Greek Omega)
   print("\U0001F600")     # Output: 😀 (Smiling Face Emoji)
   print("\x48\x65\x6c\x6c\x6f")  # Output: Hello
   ```
   **Explanation:**  
   Inserts Unicode characters using their hexadecimal values.

---

## Raw Strings

Raw strings treat backslashes as literal characters and are defined by placing an `r` or `R` before the string. This is especially useful for regular expressions and file paths.

### Example:
```python
print(r"C:\Users\Hashim\Python")
# Output: C:\Users\Hashim\Python
```

**Explanation:**  
- The `r` prefix tells Python not to interpret backslashes as escape characters, so the string prints exactly as written.

---