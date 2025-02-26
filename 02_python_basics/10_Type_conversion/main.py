
# Type Conversion Examples in Python

# --- Implicit Type Conversion ---

print("=== Implicit Type Conversion ===")
a = 5          # integer
b = 2.5        # float
result = a + b # 'a' is implicitly converted to float
print("Result of adding an integer and a float:", result, type(result))


# --- Explicit Type Conversion ---

print("\n=== Explicit Type Conversion ===")

# Converting a string to an integer
num_str = "123"
num_int = int(num_str)
print("Converted string to integer:", num_int, type(num_int))


# Converting a float to an integer (truncation occurs)

flt = 9.99
int_flt = int(flt)
print("Converted float to integer:", int_flt, type(int_flt))



# Converting an integer to a float

int_val = 10
flt_val = float(int_val)
print("Converted integer to float:", flt_val, type(flt_val))



# Converting a number to a string

num = 456
str_num = str(num)
print("Converted number to string:", str_num, type(str_num))



# Converting a list to a tuple

my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print("Converted list to tuple:", my_tuple, type(my_tuple))



# --- Input Conversion Examples ---
print("\n=== Input Conversion Examples ===")

# Example: Converting user input to an integer

user_input = input("Enter an integer: ")
converted_int = int(user_input)
print("User input converted to integer:", converted_int, type(converted_int))


# Example: Converting user input to a float

user_input = input("Enter a floating-point number: ")
converted_float = float(user_input)
print("User input converted to float:", converted_float, type(converted_float))
