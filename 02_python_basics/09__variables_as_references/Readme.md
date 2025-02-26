# Variables and Other References in Python

This section explains how Python uses variables and references to access and manipulate data values within programs.

In this section, we examine how Python programs access and manipulate data through **references**. Understanding how variables and references work is essential for effective Python programming.

## References in Python

A reference in Python is a label or name that points to a specific object in memory, enabling dynamic and flexible data management.

- A **reference** is essentially a label that points to a value (object) in Python.
- **References** can appear as variables, attributes, or items.
- In Python, a reference itself does not have an intrinsic type; the type is determined by the object to which it currently points.
- Over the course of a program’s execution, a single reference may be associated with objects of different types.

### Example:
```python
value = 42       # 'value' is a reference to an integer object
value = "hello"  # 'value' now references a string object
```

## Variables in Python

Variables in Python are names that refer to objects. They are created by assignment and can be rebound to different objects as needed.

- In Python, variables are simply **references** to objects. Unlike some other programming languages, there are no explicit variable declarations.
- A variable comes into existence when it is **bound** to an object.
- Variables can be **rebound** to new objects, and they can also be **unbound**, meaning they no longer refer to any object.

### Binding and Rebinding

- **Binding:** The process of associating a variable with an object.
- **Rebinding:** Assigning a new object to a variable that already has a binding.

### Example:
```python
num = 10    # Binding: 'num' refers to the integer 10
num = 20    # Rebinding: 'num' now refers to the integer 20
```

Unbinding is the process of removing the association between a variable and an object, typically using the `del` statement.

### Example:
```python
item = 10   # 'item' refers to the integer 10
del item    # 'item' is now unbound; the name no longer exists
```

When a reference is unbound, the object it pointed to may be reclaimed by Python's garbage collector if no other references exist.

### Example:
```python
list_obj = [1, 2, 3]  # 'list_obj' refers to a list object
alias = list_obj      # 'alias' also refers to the same list object
del list_obj          # 'list_obj' is unbound, but the list remains because 'alias' still references it
```

## Naming Variables

Variable names in Python must follow the rules for identifiers and cannot be reserved keywords. Variables are categorized by their scope:

- **Global Variables:** Accessible throughout the entire module; they are attributes of the module.
- **Local Variables:** Accessible only within the function in which they are defined.

### Example:
```python
message = "Global Message"  # Global variable

def show_message():
    note = "Local Note"     # Local variable
    print("Inside function:", note)
    print("Inside function accessing global variable:", message)

show_message()          # Displays both local and global messages
print("Outside function:", message)
```

