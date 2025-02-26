# Character Sets in Python

## Unicode and ASCII in Python

### Python 3

- **Python 3** source files can use **any Unicode character**, encoded as **UTF-8**.
  - **UTF-8** is a variable-width character encoding that represents every character in the Unicode character set.
  - **ASCII characters** (with codes between 0 and 127) are encoded in UTF-8 as single bytes, ensuring that an ASCII text file is valid as a Python 3 source file.

### Python 2

- **Python 2** source files typically consist of characters from the **ASCII set**.
  - ASCII characters have codes ranging between 0 and 127.

## Specifying a Different Encoding

- In both Python 2 and 3, you can specify a different encoding for a source file.
- Python uses this specified encoding to interpret the file correctly.

### Example:
```python
# coding: utf-8
```

- This comment should be placed at the very beginning of the Python source file (immediately after the "shebang line" if present).
- The `coding:` directive is also referred to as an **encoding declaration**.

## Using Non-ASCII Characters

- In **Python 2**, non-ASCII characters can only be used in **comments** and **string literals**.
- The **coding directive** allows you to use these characters by specifying the appropriate encoding.

### Example:
```python
# coding: iso-8859-1
# This is a comment with a non-ASCII character: ñ
print("Hola, señor!")
```

## Best Practices for Encoding

- It is recommended to use **UTF-8** for all text files, including Python source files.
  - **UTF-8** ensures compatibility with a wide variety of characters from different languages.

### Example:
```python
# coding: utf-8
print("こんにちは, 世界!")  # Prints "Hello, World!" in Japanese
```

---
This section covered how Python handles character sets and encodings. By understanding and applying the correct encoding, you can write Python code that is robust, flexible, and compatible across different systems.

