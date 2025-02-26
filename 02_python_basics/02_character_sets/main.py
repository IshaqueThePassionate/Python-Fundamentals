# Python 3: Using UTF-8 encoding
# UTF-8 allows the use of any Unicode character
# ASCII characters (0-127) are encoded as single bytes

# Example of a valid Python 3 source file with Unicode characters
print("Hello, World!")  # Standard ASCII characters
print("こんにちは, 世界!")  # Japanese characters (UTF-8 encoded)

# Specifying a Different Encoding
# The following comment should be placed at the top of the file
# coding: utf-8

# Using Non-ASCII Characters in Python 2
# In Python 2, non-ASCII characters can be used in comments and string literals
# Ensure the appropriate encoding is declared at the top

# Example with ISO-8859-1 encoding
# coding: iso-8859-1
print("Hola, señor!")  # Spanish text with a special character

# Best Practices for Encoding
# Always use UTF-8 encoding for Python files to ensure compatibility across different systems
# UTF-8 supports a vast range of characters from different languages
# Configure the editor to replace tabs with four spaces for consistency

# Correct indentation using four spaces
def greet(name):
    print(f"Hello, {name}!")  # Properly formatted function with UTF-8 compatibility
