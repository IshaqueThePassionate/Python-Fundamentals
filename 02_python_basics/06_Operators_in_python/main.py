# Arithmetic Operators
a = 10
b = 3

print(a + b)  # Addition: 10 + 3 = 13
print(a - b)  # Subtraction: 10 - 3 = 7
print(a * b)  # Multiplication: 10 * 3 = 30
print(a / b)  # Division: 10 / 3 = 3.3333...
print(a % b)  # Modulus: Remainder of 10 / 3 = 1
print(a ** b) # Exponentiation: 10^3 = 1000
print(a // b) # Floor division: 10 // 3 = 3 (removes decimal)

# Comparison Operators
x = 5
y = 3

print(x < y)   # Less than: False
print(x <= y)  # Less than or equal to: False
print(x > y)   # Greater than: True
print(x >= y)  # Greater than or equal to: True
print(x == y)  # Equal to: False
print(x != y)  # Not equal to: True

# Logical Operators
p = True
q = False

print(p and q)  # AND: False (both must be True)
print(p or q)   # OR: True (at least one True)
print(not p)    # NOT: False (reverses True)

# Bitwise Operators
m = 5  # 101 in binary
n = 3  # 011 in binary

print(m & n)  # Bitwise AND: 101 & 011 = 001 (1)
print(m | n)  # Bitwise OR: 101 | 011 = 111 (7)
print(m ^ n)  # Bitwise XOR: 101 ^ 011 = 110 (6)
print(~m)     # Bitwise NOT: ~101 = -6 (inverts bits)
print(m << 1) # Left shift: 101 << 1 = 1010 (10)
print(m >> 1) # Right shift: 101 >> 1 = 10 (2)

# Assignment Operators
num = 10
num += 5  # Equivalent to num = num + 5
print(num)  # Output: 15

num *= 2  # Equivalent to num = num * 2
print(num)  # Output: 30

# Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)  # True (same object)
print(list1 is list3)  # False (different objects)
print(list1 is not list3)  # True

# Membership Operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  # True (exists in the list)
print("grape" not in fruits)  # True (does not exist)

# Using @ Operator (Matrix Multiplication)
import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = matrix1 @ matrix2  # Matrix multiplication
print(result)  # Output: [[19 22]
              #          [43 50]]
