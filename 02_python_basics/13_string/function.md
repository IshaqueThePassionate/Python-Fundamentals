```python
def to_uppercase(input_string):
    uppercase_string = ""  # Initialize an empty string to store the result
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase by subtracting 32 from its ASCII value
            uppercase_char = chr(ord(char) - 32)
            # Append the converted character to the result string
            uppercase_string += uppercase_char
        else:
            # If the character is not a lowercase letter, add it as is
            uppercase_string += char
    
    return uppercase_string  # Return the final uppercase string

# Example usage
example_str = "hello world!"
result = to_uppercase(example_str)
print(result)  # Output: HELLO WORLD!
```

### Explanation:

1. **Initialize an Empty String:**
   - An empty string `uppercase_string` is created to store the final result.

2. **Iterate Through Each Character:**
   - The function iterates through each character in `input_string` using a `for` loop.

3. **Check if Character is Lowercase:**
   - It checks if the character is a lowercase letter by comparing its ASCII value.

4. **Convert Lowercase to Uppercase:**
   - If the character is lowercase, it is converted to its uppercase equivalent by subtracting 32 from its ASCII value.

5. **Append to Result String:**
   - The converted uppercase character is appended to `uppercase_string`.

6. **Handle Non-Lowercase Characters:**
   - If the character is not lowercase, it is directly appended to `uppercase_string`.

7. **Return the Uppercase String:**
   - Finally, the function returns the `uppercase_string` containing all the uppercase characters.