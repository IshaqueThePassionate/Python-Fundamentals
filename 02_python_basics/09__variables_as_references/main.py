# Code Examples for Variables and References in Python

# --- References in Python ---

print("=== References in Python ===")
a = 50                      # 'a' initially refers to an integer object
print("a initially:", a)
a = [1, 2, 3]               # 'a' now refers to a list object
print("a now references a list:", a)


# --- Variables, Binding, and Rebinding ---

print("\n=== Variables, Binding, and Rebinding ===")
b = 30                      # Binding: 'b' refers to the integer 30
print("Original value of b:", b)
b = b + 5                   # Rebinding: 'b' now refers to a new integer value 35
print("Rebound value of b:", b)


# --- Unbinding Variables ---

print("\n=== Unbinding Variables ===")
c = {"x": 1, "y": 2}        # 'c' refers to a dictionary object
d = c                       # 'd' is another reference to the same dictionary
print("Before unbinding, d:", d)
del c                       # Unbinding: 'c' is removed, but the dictionary persists via 'd'
print("After unbinding c, d still holds the dictionary:", d)



# --- Global and Local Variables ---

print("\n=== Global and Local Variables ===")
global_message = "I am a global variable"  # Global variable

def demonstrate_scope():
    local_message = "I am a local variable"  # Local variable
    print("Inside function, local_message:", local_message)
    print("Inside function, global_message:", global_message)

demonstrate_scope()
print("Outside function, global_message:", global_message)
