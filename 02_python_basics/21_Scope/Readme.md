# **Scope**

## **Explanation**:
In Python, **scope** refers to the part of the program where a **variable** can be **accessed** or **modified**. Understanding scope is essential when writing code, especially when working with **functions**, because it affects how variables are created, accessed, and maintained.

## **Key Concepts of Scope**:
1. **Local Scope**:
   - Variables **defined within a function**.
   - Only **accessible** within that function.
2. **Nonlocal Scope**:
   - Variables **defined in an enclosing function**.
   - **Accessible** in **nested functions** but **not** in the **outermost scope**.
3. **Global Scope**:
   - Variables **defined outside of all functions**.
   - **Accessible** from **anywhere** within the file.

## **Understanding Lexical Scoping**:
- **Lexical scoping** (or **static scoping**) means that the **location** of a variable’s assignment in the **source code** determines its **scope**.
- For example, a variable defined **inside a function** is **local** to that function, even if that function is called from another part of the program.

## **Examples of Different Scopes**

### **1. Local Scope: Variables Inside a Function**
Variables defined within a function are **local** to that function.

```python
def greet():
    name = "Muhammad Hashim"  # Local variable
    print(f"Hello, {name}!")

greet()  # Output: Hello, Muhammad Hashim
print(name)  # Error: name is not defined
```

**Explanation**:
- **`name`** is a **local variable** defined inside the `greet()` function.
- It is only accessible within the `greet()` function. Trying to access it **outside** the function will result in an **error** because **`name` does not exist** in the global scope.

### **2. Global Scope: Variables Defined Outside Functions**
Variables defined **outside** of all functions are **global** and can be accessed anywhere.

```python
name = "Muhammad Hashim"  # Global variable

def greet():
    print(f"Hello, {name}!")

greet()  # Output: Hello, Muhammad Hashim
print(name)  # Output: Muhammad Hashim
```

**Explanation**:
- The **`name`** variable is defined **outside** any function, so it is **global**.
- Both the `greet()` function and the **main program** can access it.

### **3. Local and Global Variables with the Same Name**
Even if a local and global variable have the **same name**, they are treated as **different variables**.

```python
name = "Muhammad Hashim"  # Global variable

def greet():
    name = "Hashim"  # Local variable
    print(f"Hello, {name}!")

greet()  # Output: Hello, Hashim
print(name)  # Output: Muhammad Hashim
```

**Explanation**:
- The **`name`** inside `greet()` is **local** to the function and **different** from the **global `name`**.
- When **`greet()`** is called, it prints **"Hashim"** (the local `name`). Outside of `greet()`, it prints **"Muhammad Hashim"** (the global `name`).

## **Understanding Nonlocal Scope with Nested Functions**

### **4. Nonlocal Variables: Variables in an Enclosing Function**
If you have **nested functions**, a variable defined in the **enclosing function** is **nonlocal** to the nested function.

```python
def outer():
    name = "Hashim"  # Nonlocal variable

    def inner():
        nonlocal name
        name = "Muhammad Hashim"
        print(f"Inside inner: {name}")

    inner()
    print(f"Inside outer: {name}")

outer()
```

**Output**:
```
Inside inner: Muhammad Hashim
Inside outer: Muhammad Hashim
```

**Explanation**:
- The `name` defined inside `outer()` is **nonlocal** because it is **enclosing** for `inner()`.
- By using **`nonlocal`**, the `inner()` function can **modify** the **`name`** variable from `outer()`. Without **`nonlocal`**, a new **local variable** would have been created inside `inner()`.

## **Important Rules**:
1. **Names assigned inside a `def`** (function) can **only be seen** by the code **within that `def`**. 
2. **Names assigned inside a `def`** do **not clash** with variables **outside** the `def`, even if the **same names** are used elsewhere. 
3. The **scope** of a variable is determined by **where** it is **assigned** in your code.

## **Example: Local, Nonlocal, and Global Variables in Action**

```python
X = "Global X"  # Global variable

def outer():
    X = "Outer X"  # Nonlocal variable

    def inner():
        nonlocal X  # Refers to the nonlocal X in `outer`
        X = "Inner X"  # Local to inner, modifies outer's X
        print(f"Inside inner: {X}")

    inner()
    print(f"Inside outer: {X}")

outer()
print(f"Outside all: {X}")
```

**Output**:
```
Inside inner: Inner X
Inside outer: Inner X
Outside all: Global X
```

**Explanation**:
- **Global X** is defined at the **module level**.
- **`X = "Outer X"`** is **nonlocal** because it's inside the `outer()` function, and it **can be accessed** by `inner()` if **`nonlocal`** is used.
- **`inner()`** modifies **nonlocal X** because **`nonlocal`** allows it to change the variable defined in `outer()`.

## **Key Points to Remember**:

1. **Local Variables**:
   - Declared **inside a function**.
   - Accessible **only within that function**.

2. **Nonlocal Variables**:
   - Declared in an **enclosing function**.
   - Accessible **inside nested functions**, but not in the **global scope**.

3. **Global Variables**:
   - Declared **outside of all functions**.
   - Accessible **anywhere** in the program file.

4. **Lexical Scoping** ensures that **variable access** is determined by **where** the **variable** is **declared**, not **where** it is **used**.

---

## **The LEGB Rule**
Python follows the **LEGB rule** to resolve variable names:
1. **Local (L)**: Variables defined **inside the current function**.
2. **Enclosing (E)**: Variables in the **outer function** (if the current function is nested).
3. **Global (G)**: Variables defined at the **module level**.
4. **Built-in (B)**: Predefined Python functions and constants.

### **Example: LEGB Rule in Action**

```python
# Global Scope
name = "Muhammad Hashim"  # Global variable

def outer():
    name = "Hashim"  # Enclosing (Nonlocal) variable

    def inner():
        name = "Local Hashim"  # Local variable
        print(f"Inside inner: {name}")

    inner()
    print(f"Inside outer: {name}")

outer()
print(f"Global scope: {name}")
```

**Output**:
```
Inside inner: Local Hashim
Inside outer: Hashim
Global scope: Muhammad Hashim
```

**Explanation**:
1. **`inner()`** prints **"Local Hashim"** because **`name`** is a **local variable** inside `inner()`.
2. **`outer()`** prints **"Hashim"** because **`name`** refers to the **enclosing nonlocal variable** in `outer()`.
3. The **global scope** prints **"Muhammad Hashim"**, the **global variable**.

---

## **Understanding Built-in Scope and Redefining Names in Python**

In Python, several built-in functions, constants, and modules are available without import. These reside in the **built-in scope**.

### **What is Built-in Scope?**
The **built-in scope** consists of names that are predefined and always available, such as:
- Functions like `print()`, `len()`, `open()`
- Constants like `True`, `False`, `None`
- Exceptions like `ValueError`, `TypeError`

Python checks the **built-in scope** last when resolving a variable name, following the **LEGB rule**.

### **Viewing All Built-in Names**
To get a list of all built-in names in Python, use the **`dir()`** function on the `builtins` module:

```python
import builtins
print(dir(builtins))
```

### **Redefining Built-in Names: Be Careful!**
Redefining built-in names can lead to unexpected behavior. For example, if you create a variable named `open`, you **hide** the built-in `open()` function.

#### **Example: Redefining a Built-in Name**
```python
# Redefine the built-in open function
open = "This is not a function anymore!"  # Overrides the built-in open
print(open)  # Output: This is not a function anymore!

# Now, try to use open() to open a file:
try:
    open("example.txt", "r")
except TypeError as e:
    print(f"Error: {e}")
```

**Explanation**:
- **`open`** is redefined as a **string**, hiding the built-in `open()` function.
- Attempting to use **`open()`** afterward causes a **TypeError**.

### **Safely Accessing Built-ins After Overriding**
If you accidentally override a built-in name, access the original function using the **`builtins`** module:

```python
import builtins

# Safely using built-ins after overriding
open = "Overridden Open"  # Overrides the built-in open
print(open)  # Prints the string

# Access the original built-in open
with builtins.open("example.txt", "w") as file:
    file.write("This is safe!")
```

### **Best Practices to Avoid Overriding Built-ins**
1. Choose unique variable names that do not clash with built-ins.
2. Avoid using built-in names like `list`, `str`, `sum` for your variables.
3. Restore built-in functionality if overridden using `del`:

```python
list = [1, 2, 3]  # Overrides built-in list function
print(list)  # Output: [1, 2, 3]
del list  # Remove override
print(list("123"))  # Built-in list function works again
```

### **Example: Safely Overriding and Using Built-in Functions**
```python
import builtins

def process_data():
    len = "Overridden Length"  # Override the built-in len function
    print(len)  # Prints the string
    print(builtins.len([1, 2, 3, 4]))  # Safely use the original len function

process_data()
```

**Output**:
```
Overridden Length
4
```

---

## **Understanding Global Variables and Best Practices in Python**

When programming in Python, it’s crucial to manage how functions handle variables to avoid pitfalls. While global variables can be useful, overreliance on them may lead to bugs and difficult-to-maintain code.

### **What Are Global Variables?**
- **Global variables** are defined at the top level of a script or module, making them accessible throughout the entire file.
- They can be read or modified by any function within the same module, which may cause unintended side effects.

### **Example of a Global Variable**
```python
age = 25  # Global variable

def print_age():
    print(f"Muhammad Hashim is {age} years old.")  # Accessing global variable inside a function

print_age()  # Output: Muhammad Hashim is 25 years old.
```

**Explanation**: The variable `age` is global and accessible in `print_age()`.

### **The `global` Statement**
To modify a global variable inside a function, use the **`global`** statement.

#### **Example of Modifying a Global Variable**
```python
experience = 3  # Global variable representing years of experience

def update_experience():
    global experience  # Declare as global
    experience = 5  # Modify the global variable

print("Before:", experience)  # Output: 3
update_experience()
print("After:", experience)  # Output: 5
```

**Explanation**: The `global` statement allows `update_experience()` to modify the global `experience`.

### **Why Minimize Global Variables?**
Global variables can:
1. Be hard to debug due to unexpected changes.
2. Make code harder to reuse since functions depend on external data.
3. Lead to unintended overwrites.

### **Preferred Approach: Use Function Arguments & Return Values**
Instead of relying on globals, pass data as arguments and return results.

```python
def calculate_age(birth_year):
    current_year = 2024
    return current_year - birth_year

muhammad_age = calculate_age(1999)
print(f"Muhammad Hashim is {muhammad_age} years old.")  # Output: Muhammad Hashim is 25 years old.
```

**Explanation**: The function is self-contained and does not depend on external variables.

### **Combining Concepts: Managing State Without Globals**
Avoid global variables by passing data explicitly.

#### **Not Recommended**
```python
monthly_income = 5000
monthly_expenses = 3000

def calculate_monthly_savings():
    return monthly_income - monthly_expenses

def predict_yearly_savings():
    return calculate_monthly_savings() * 12

print(f"Predicted Yearly Savings: {predict_yearly_savings()}")  # Output: 24000
```

#### **Recommended**
```python
def calculate_monthly_savings(income, expenses):
    return income - expenses

def predict_yearly_savings(income, expenses):
    monthly_savings = calculate_monthly_savings(income, expenses)
    return monthly_savings * 12

income = 5000
expenses = 3000
yearly_savings = predict_yearly_savings(income, expenses)

print(f"Predicted Yearly Savings: {yearly_savings}")  # Output: 24000
```

**Explanation**: Passing arguments makes functions independent and predictable.

---

## **The Concept of Nested Functions and Enclosing Scope**

A **nested function** is defined inside another function, creating an **enclosing scope**. Variables from the outer function can be accessed by the inner function.

### **Example: Nested Function Accessing Enclosing Scope**
```python
def greet():
    message = "Hello, Muhammad Hashim!"  # Enclosing scope

    def print_message():
        print(message)  # Accessing 'message' from enclosing scope

    print_message()

greet()  # Output: Hello, Muhammad Hashim!
```

**Explanation**: The inner function can access `message` because it is in the enclosing scope.

## **The `global` Keyword: Access and Modify Global Variables**

The **`global`** keyword allows you to modify a global variable from within a function.

### **Incorrect Example: Without `global`**
```python
counter = 0

def increment():
    counter += 1  # Error: 'counter' is treated as local
increment()  # Raises UnboundLocalError
```

### **Correct Usage with `global`**
```python
counter = 0  # Global variable

def increment():
    global counter  # Declare 'counter' as global
    counter += 1

increment()
print(counter)  # Output: 1
```

**Explanation**: Using `global` tells Python to use the global `counter`.

## **The `nonlocal` Keyword: Modify Variables in Enclosing Scopes (Python 3.x)**

The **`nonlocal`** keyword is used to modify variables in the nearest **enclosing scope**.

### **Example: Using `nonlocal`**
```python
def outer():
    age = 25  # Enclosing scope

    def inner():
        nonlocal age  # Declare 'age' as nonlocal
        age = 30  # Modify the enclosing 'age'
    
    inner()
    print(f"Muhammad Hashim's updated age: {age}")

outer()  # Output: Muhammad Hashim's updated age: 30
```

**Explanation**: `nonlocal` allows the inner function to modify `age` from `outer()`.

## **Factory Functions and Closures**

**Closures** are nested functions that "remember" values from their enclosing scopes even after the outer function has finished execution.

### **Example: Creating a Closure**
```python
def multiplier(factor):
    def multiply(number):
        return number * factor  # 'factor' is remembered from enclosing scope
    return multiply

double = multiplier(2)
print(double(5))  # Output: 10

triple = multiplier(3)
print(triple(5))  # Output: 15
```

**Explanation**: Each closure remembers its own `factor`, allowing flexible reuse.

## **Loop Variables and the Default Argument Trap**

When creating functions within a loop, use default arguments to capture the current value of the loop variable.

### **Incorrect Example: Loop Variables in Closures**
```python
def create_actions():
    actions = []
    for i in range(3):
        actions.append(lambda: print(i))  # Each lambda references the same 'i'
    return actions

actions = create_actions()
actions[0]()  # Output: 2
actions[1]()  # Output: 2
actions[2]()  # Output: 2
```

### **Correct Usage: Preserve Loop Variable with Default Arguments**
```python
def create_actions():
    actions = []
    for i in range(3):
        actions.append(lambda i=i: print(i))  # Capture 'i' at each iteration
    return actions

actions = create_actions()
actions[0]()  # Output: 0
actions[1]()  # Output: 1
actions[2]()  # Output: 2
```

**Explanation**: Using `i=i` in the lambda captures the current value of `i`.

---

## **The `nonlocal` Statement in Python 3.x**

The `nonlocal` keyword allows a nested function to modify variables in its enclosing function's scope.

### **Example: Using `nonlocal`**
```python
def outer():
    x = 10  # Enclosing scope

    def inner():
        nonlocal x  # Declare 'x' as nonlocal
        x += 1

    inner()
    print(x)  # Output: 11

outer()
```

**Explanation**: `nonlocal` lets the inner function both read and modify `x` from `outer()`.

### **Why Use `nonlocal`?**
It is especially useful for state retention within nested functions, such as implementing counters or trackers.

### **Example: Counter Using `nonlocal`**
```python
def create_counter(start=25):
    age = start  # Enclosing variable

    def increment():
        nonlocal age  # Declare 'age' as nonlocal
        age += 1
        print(f"Muhammad Hashim's age is now: {age}")

    return increment

counter = create_counter()  # Starting age at 25
counter()  # Output: Muhammad Hashim's age is now: 26
counter()  # Output: Muhammad Hashim's age is now: 27
```

**Explanation**: The nested `increment` function can modify `age` from `outer()`.

### **Comparison: `nonlocal` vs `global`**

| **Feature**    | **`nonlocal`**                                     | **`global`**                                   |
|----------------|----------------------------------------------------|------------------------------------------------|
| Scope          | Enclosing function                                | Module-level (global)                         |
| Can Modify?    | Yes (only in enclosing functions)                 | Yes (affects global variables)                |
| Must Exist?    | Yes (must be pre-defined in the enclosing scope)  | No (can be created dynamically)               |
| Usage Context  | For nested functions                               | For values shared across modules              |

### **Incorrect Example: `nonlocal` Must Reference an Existing Variable**
```python
def outer_function():
    def inner_function():
        nonlocal value  # Error: 'value' does not exist in the enclosing scope
        value = 10

    inner_function()

outer_function()  # Raises SyntaxError
```

**Explanation**: `nonlocal` does not create new variables; it must reference an existing variable in the enclosing scope.

### **Alternative State Retention Methods**

Before `nonlocal`, state was managed using classes, globals, or function attributes.

### **Example: Using Function Attributes**
```python
def create_stateful():
    def inner():
        inner.counter += 1
        print(f"Counter: {inner.counter}")

    inner.counter = 0  # Initialize attribute
    return inner

counter_function = create_stateful()
counter_function()  # Output: Counter: 1
counter_function()  # Output: Counter: 2
```

**Explanation**: The function attribute `inner.counter` is used for state retention without `nonlocal`.

---

# **Understanding Global Variables and Best Practices in Python**

Global variables are defined at the top level of a module and are accessible throughout the file. However, overuse of globals can lead to bugs and maintenance challenges.

## **What Are Global Variables?**
- Defined at the module level.
- Accessible throughout the file.
- Can be read or modified by any function, leading to potential side effects.

### **Example of a Global Variable**
```python
age = 25  # Global variable

def print_age():
    print(f"Muhammad Hashim is {age} years old.")

print_age()  # Output: Muhammad Hashim is 25 years old.
```

**Explanation**: The variable `age` is global and accessible within the function.

## **Global Variables Across Multiple Files**
Global variables can be accessed from other modules, though this can lead to complex cross-file dependencies.

### **Example: Accessing Globals from Another File**
- **File 1: `muhammad.py`**
    ```python
    city = "Lahore"  # Global variable in muhammad.py
    ```

- **File 2: `details.py`**
    ```python
    import muhammad

    print(f"Muhammad Hashim lives in {muhammad.city}.")
    muhammad.city = "Islamabad"
    ```

**Explanation**: `details.py` accesses and modifies the global variable `city` from `muhammad.py`.

## **Better Practice: Use Accessor Functions**
Instead of modifying globals directly, use functions to access and update global state.

### **Example with Accessor Functions**
- **File 1: `muhammad.py`**
    ```python
    skill_level = "Intermediate"

    def set_skill_level(level):
        global skill_level
        skill_level = level

    def get_skill_level():
        return skill_level
    ```

- **File 2: `details.py`**
    ```python
    import muhammad

    print(f"Muhammad Hashim's skill level: {muhammad.get_skill_level()}.")
    muhammad.set_skill_level("Expert")
    print(f"Updated skill level: {muhammad.get_skill_level()}.")
    ```

**Explanation**: Using accessor functions makes modifications explicit and controlled.

## **Global Variables in Multithreading**
When multiple threads access and modify the same global variable, use thread synchronization (e.g., `threading.Lock`) to prevent race conditions.

## **Alternative Approach: Using `sys.modules`**
You can access and modify global variables as module attributes.

### **Example: Using `sys.modules`**
- **File: `hashim.py`**
    ```python
    import sys

    projects_completed = 15

    def increment_projects():
        sys.modules[__name__].projects_completed += 1
    ```

**Explanation**: `sys.modules` provides access to the module itself for explicit global variable modification.

## **Advanced Example: Managing Global Configuration**
```python
# File: config.py
settings = {
    "name": "Muhammad Hashim",
    "profession": "Software Engineer",
    "projects": 10
}

def update_settings(key, value):
    global settings
    if key in settings:
        settings[key] = value
    else:
        raise KeyError("Key does not exist in settings")

# File: app.py
from config import settings, update_settings

print("Before Update:", settings)
update_settings("projects", 12)
print("After Update:", settings)
```

**Output**:
```
Before Update: {'name': 'Muhammad Hashim', 'profession': 'Software Engineer', 'projects': 10}
After Update: {'name': 'Muhammad Hashim', 'profession': 'Software Engineer', 'projects': 12}
```

**Explanation**: Managing settings through functions provides clear and controlled updates.

---

## **The Concept of Nested Functions and Enclosing Scope**

Nested functions create an **enclosing scope**. Variables in the outer function can be accessed by the inner function.

### **Example: Nested Function Accessing Enclosing Scope**
```python
def greet():
    message = "Hello, Muhammad Hashim!"  # Enclosing scope

    def print_message():
        print(message)  # Accessing 'message' from enclosing scope

    print_message()

greet()  # Output: Hello, Muhammad Hashim!
```

**Explanation**: The inner function accesses `message` from the enclosing scope.

## **The `global` Keyword: Access and Modify Global Variables**

The **`global`** keyword allows modification of a global variable within a function.

### **Incorrect Example: Without `global`**
```python
counter = 0

def increment():
    counter += 1  # Error: 'counter' is treated as local
increment()  # Raises UnboundLocalError
```

### **Correct Usage with `global`**
```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # Output: 1
```

**Explanation**: `global` makes Python use the module-level `counter`.

## **The `nonlocal` Keyword: Modify Variables in Enclosing Scopes**

`nonlocal` allows a nested function to modify a variable from its enclosing scope.

### **Example: Using `nonlocal`**
```python
def outer():
    age = 25

    def inner():
        nonlocal age
        age = 30
    
    inner()
    print(f"Muhammad Hashim's updated age: {age}")

outer()  # Output: Muhammad Hashim's updated age: 30
```

**Explanation**: `nonlocal` allows the inner function to modify `age` in `outer()`.

## **Factory Functions and Closures**

Closures "remember" variables from their enclosing scopes.

### **Example: Creating a Closure**
```python
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
print(double(5))  # Output: 10

triple = multiplier(3)
print(triple(5))  # Output: 15
```

**Explanation**: Each closure remembers its own `factor`.

## **Loop Variables and the Default Argument Trap**

Use default arguments to capture the current value of loop variables in closures.

### **Incorrect Example: Loop Variables in Closures**
```python
def create_actions():
    actions = []
    for i in range(3):
        actions.append(lambda: print(i))
    return actions

actions = create_actions()
actions[0]()  # Output: 2
actions[1]()  # Output: 2
actions[2]()  # Output: 2
```

### **Correct Usage: Preserve Loop Variable with Default Arguments**
```python
def create_actions():
    actions = []
    for i in range(3):
        actions.append(lambda i=i: print(i))
    return actions

actions = create_actions()
actions[0]()  # Output: 0
actions[1]()  # Output: 1
actions[2]()  # Output: 2
```

**Explanation**: Default arguments capture the current value of `i`.

---

## **The `nonlocal` Statement in Python 3.x**

The `nonlocal` keyword lets a nested function modify a variable from its enclosing function.

### **Example: Using `nonlocal`**
```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1

    inner()
    print(x)  # Output: 11

outer()
```

**Explanation**: The inner function modifies `x` from `outer()`.

### **Example: Counter Using `nonlocal`**
```python
def create_counter(start=25):
    age = start

    def increment():
        nonlocal age
        age += 1
        print(f"Muhammad Hashim's age is now: {age}")

    return increment

counter = create_counter()  # Starting age at 25
counter()  # Output: Muhammad Hashim's age is now: 26
counter()  # Output: Muhammad Hashim's age is now: 27
```

**Explanation**: Each call to `counter()` increments the nonlocal variable `age`.

### **Comparison: `nonlocal` vs `global`**

| **Feature**    | **`nonlocal`**                      | **`global`**                  |
|----------------|-------------------------------------|-------------------------------|
| Scope          | Enclosing function                  | Module-level (global)         |
| Can Modify?    | Yes, in enclosing functions         | Yes, affects global variables |
| Must Exist?    | Yes, must be pre-defined in enclosing scope | No, can be created dynamically  |
| Usage Context  | For nested functions                | For values shared across modules |

### **Incorrect Example: `nonlocal` Must Reference an Existing Variable**
```python
def outer_function():
    def inner_function():
        nonlocal value  # Error: 'value' does not exist in the enclosing scope
        value = 10

    inner_function()

outer_function()  # Raises SyntaxError
```

**Explanation**: `nonlocal` cannot create a new variable.

### **Alternative: Using Function Attributes**
```python
def create_stateful():
    def inner():
        inner.counter += 1
        print(f"Counter: {inner.counter}")

    inner.counter = 0
    return inner

counter_function = create_stateful()
counter_function()  # Output: Counter: 1
counter_function()  # Output: Counter: 2
```

**Explanation**: Function attributes can also manage state.

