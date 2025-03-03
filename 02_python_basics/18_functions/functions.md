# Defining a Function in Python

## What is a Function?

A function in Python is a block of organized, reusable code that is used to perform a single action. You define a function once and then call it whenever you need it. Let's break down how to define and use a simple function!

## Creating Your First Function

Here’s an example of a simple function called `greet_user()` that prints a greeting:

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
```

### Understanding the Structure:

1. **Keyword `def`**: We use `def` to inform Python that we are defining a new function.
2. **Function Name**: The function is named `greet_user()`. You can choose any meaningful name for your function.
3. **Parentheses `()`**: Even if the function doesn’t need any information, parentheses are always required.
4. **Colon `:`**: The function definition ends with a colon. This tells Python that the function body will follow.
5. **Indented Lines**: Any indented lines after `def greet_user():` form the **body** of the function. In this case, the function has one job: to print a message.

## What is a Docstring?

The line:

```python
"""Display a simple greeting."""
```

is called a **docstring** (documentation string). It's a short comment that describes what the function does. When Python generates documentation for your code, it uses this docstring to explain what the function is meant to do.

Pro Tip: Always write docstrings in triple quotes (`"""`), especially if your function performs multiple tasks. It makes your code easier to understand!

## Calling the Function

After defining a function, you can **call** it by writing its name followed by parentheses, like this:

```python
greet_user()
```

When you call `greet_user()`, Python executes the code inside the function, printing:

```
Hello!
```

### How It Works:
- The function `greet_user()` is called, and Python looks inside the function to find what it needs to do.
- It finds the `print("Hello!")` line, so it prints "Hello!" to the console.

---

# Passing Information to a Function in Python

## Customizing Your Functions with Arguments

In Python, you can make functions more flexible by passing information to them. This allows your function to process different data and produce dynamic results. Let’s modify our `greet_user()` function to greet people by their name.

## Modifying `greet_user()` to Accept a Name

Here’s how you can tweak the function to greet users by their names:

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
```

### What’s Different?
1. **`username` parameter**: We added `username` inside the parentheses. This means the function now expects some information (in this case, a name) whenever it’s called.
2. **Using `username`**: Inside the function, we use `username.title()` to capitalize the first letter of the name and display it in the greeting.

## Calling the Function with an Argument

To use this new version of `greet_user()`, you need to pass a name when calling the function:

```python
greet_user('ali')
```

### Output:
```
Hello, Ali!
```

## How Does It Work?
- When you call `greet_user('ali')`, you are passing the string `'ali'` to the function.
- The function then assigns `'ali'` to the **parameter** `username`.
- Inside the function, `username.title()` capitalizes the first letter and displays the message: "Hello, Ali!"

You can call `greet_user()` with different names to get personalized greetings each time:

```python
greet_user('ayesha')  # Outputs: Hello, Ayesha!
greet_user('hassan')  # Outputs: Hello, Hassan!
greet_user('ali')     # Outputs: Hello, Ali!
```

Every time you pass a different name, the function will display the corresponding greeting!

---

# Understanding Arguments and Parameters in Python

## What are Arguments and Parameters?

When working with functions in Python, we often deal with **parameters** and **arguments**. Let’s clarify the difference:

- **Parameter**: A variable in a function definition that acts as a placeholder for the information the function needs to do its job.
- **Argument**: The actual value you pass to the function when calling it.

Let’s revisit the function `greet_user()`:

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
```

Here:
- `username` is a **parameter**—it’s a variable inside the function that will hold the value passed to it.
- `'Ali'` is an **argument** when we call the function like this: `greet_user('Ali')`.

When Python runs `greet_user('Ali')`, it passes `'Ali'` as an argument to the parameter `username`. The function then prints:

```
Hello, Ali!
```

---

## Understanding Positional Arguments

When calling a function with multiple parameters, the **order of arguments matters**. These are called **positional arguments** because their order defines which parameter gets which value.

Let’s look at an example:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

Here, the function expects two **positional arguments**: `animal_type` and `pet_name`. When you call the function, you must provide these arguments in the correct order:

```python
describe_pet('parrot', 'moti')
```

In this case:
- `'parrot'` is passed to the `animal_type` parameter.
- `'moti'` is passed to the `pet_name` parameter.

The function outputs:

```
I have a parrot.
My parrot's name is Moti.
```

You can use different animals and names, like this:

```python
describe_pet('cat', 'shehzadi')
```

This will output:

```
I have a cat.
My cat's name is Shehzadi.
```

And another example:

```python
describe_pet('rabbit', 'gulabo')
```

The output will be:

```
I have a rabbit.
My rabbit's name is Gulabo.
```

---

## Try It Yourself

### 1. Message Function
Write a function called `display_message()` that prints one sentence about what you are learning:

```python
def display_message():
    """Print a message about learning."""
    print("I'm learning about functions in Python!")
    
# Call the function
display_message()
```

### 2. Favorite Book
Write a function called `favorite_book()` that accepts one **parameter**, `title`, and prints a message about your favorite book:

```python
def favorite_book(title):
    """Display a message about your favorite book."""
    print(f"One of my favorite books is {title}.")
    
# Call the function
favorite_book('Aag Ka Dariya')
```

---

# Calling a Function Multiple Times in Python

## Reusing Functions with Different Inputs

One of the great advantages of functions in Python is that you can call them as many times as you need. This allows you to reuse the same code for different inputs without rewriting it each time. Let’s explore this with the example of describing different pets.

## Describing Multiple Pets

Here’s a function called `describe_pet()` that we can use to describe different pets:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

Now, you can call this function multiple times with different animals and names. Each time, the function will work with the new inputs!

```python
describe_pet('hamster', 'shabbo')
describe_pet('dog', 'sheru')
```

### Output:

```
I have a hamster.
My hamster's name is Shabbo.

I have a dog.
My dog's name is Sheru.
```

#### How It Works

- The first call to `describe_pet('hamster', 'shabbo')` describes a hamster named Shabbo.
- The second call to `describe_pet('dog', 'sheru')` describes a dog named Sheru.

In both cases, Python matches the arguments with the parameters (`animal_type` and `pet_name`) and runs the same code with different values.

## Efficient Code Reuse

Imagine if the code inside `describe_pet()` had 10 lines. You’d still only need to call the function once for each new pet, rather than rewriting all the code. For example:

```python
describe_pet('rabbit', 'gulabo')
describe_pet('cat', 'shehzadi')
```

This will output:

```
I have a rabbit.
My rabbit's name is Gulabo.

I have a cat.
My cat's name is Shehzadi.
```

By calling the function with different arguments, you can describe any number of pets with just a single line each time.

---

# Order Matters in Positional Arguments

## What Are Positional Arguments?

In Python, when you call a function with positional arguments, the order of the arguments matters. Python assigns each argument to the corresponding parameter based on its position in the function call.

Let’s explore what happens if we mix up the order of positional arguments:

## Example: Mixing Up Argument Order

Here’s a function `describe_pet()` that expects two positional arguments: `animal_type` and `pet_name`:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

If we mix up the order of the arguments, like this:

```python
describe_pet('ali', 'cat')
```

### Output:

```
I have a ali.
My ali's name is Cat.
```

In this case, `'ali'` was assigned to `animal_type` and `'cat'` was assigned to `pet_name`, which leads to an unexpected output. This is because order matters when you use positional arguments.

### Fixing the Issue with Keyword Arguments

To avoid mistakes caused by the order of positional arguments, we can use **keyword arguments**. With keyword arguments, you explicitly tell Python which argument should go with which parameter by using a name-value pair.

Here’s how you can rewrite the function call using keyword arguments:

```python
describe_pet(animal_type='cat', pet_name='sheru')
```

### Output:

```
I have a cat.
My cat's name is Sheru.
```

Now, the output is correct because Python knows exactly which argument corresponds to each parameter, regardless of their order.

Keyword arguments can be in any order. Both of these calls will give the same result:

```python
describe_pet(animal_type='cat', pet_name='sheru')
describe_pet(pet_name='sheru', animal_type='cat')
```

Both will output:

```
I have a cat.
My cat's name is Sheru.
```

---

# Using Default Values in Python Functions

## What Are Default Values?

In Python, you can assign default values to function parameters. This means if no argument is provided for a parameter when calling the function, Python will use the default value you’ve specified. Default values can make your function calls simpler and more flexible!

## Example: Describing Pets with a Default Value

Here’s an updated version of the `describe_pet()` function. If most of the time you describe dogs, you can set the default value of `animal_type` to `'dog'`:

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

Now, when calling `describe_pet()` to describe a dog, you can omit the `animal_type` argument, like this:

```python
describe_pet(pet_name='sheru')
```

### Output:

```
I have a dog.
My dog's name is Sheru.
```

Since no argument was provided for `animal_type`, Python used the default value `'dog'`.

#### Calling the Function for Other Animals

If you want to describe an animal other than a dog, you can explicitly pass the `animal_type` argument. For example, to describe a hamster named Shabbo:

```python
describe_pet(pet_name='shabbo', animal_type='hamster')
```

### Output:

```
I have a hamster.
My hamster's name is Shabbo.
```

#### Order of Parameters with Default Values

When using default values, parameters with defaults must come after parameters without defaults in the function definition. This ensures Python can correctly match positional arguments.

For example, the parameter `pet_name` comes first, followed by `animal_type='dog'`:

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
```

#### Simplified Function Calls

With default values, you can make function calls even simpler:

```python
describe_pet('sheru')
```

This outputs:

```
I have a dog.
My dog's name is Sheru.
```

Here, `'sheru'` is matched to `pet_name`, and since `animal_type` isn’t specified, Python uses the default `'dog'`.

---

# Understanding Equivalent Function Calls in Python

## What Are Equivalent Function Calls?

In Python, you can call a function in multiple ways using positional arguments, keyword arguments, and default values. These different approaches can result in the same output, allowing you to choose whichever style is most comfortable for you.

## Example: Describing Pets with Different Function Call Styles

Let’s revisit the `describe_pet()` function. It has one required parameter, `pet_name`, and a default value for `animal_type`:

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

#### Describing a Dog Named Sheru

You can call the function to describe a dog named Sheru in several ways:

```python
# Using a positional argument
describe_pet('sheru')

# Using a keyword argument
describe_pet(pet_name='sheru')
```

Both function calls will output the same result:

```
I have a dog.
My dog's name is Sheru.
```

#### Describing a Hamster Named Shabbo

If the animal isn’t a dog, you can pass the `animal_type` argument explicitly. This can be done in multiple ways:

```python
# Using positional arguments
describe_pet('shabbo', 'hamster')

# Using keyword arguments
describe_pet(pet_name='shabbo', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='shabbo')
```

All of these calls will result in the same output:

```
I have a hamster.
My hamster's name is Shabbo.
```

#### Which Style to Use?

There are several ways to call the function, but they all give the same result. It doesn’t matter which style you use, as long as it produces the desired output. The style you choose is up to you, based on what you find easiest to read and understand.

#### Key Points:
- **Positional arguments** match arguments by the order in which they appear.
- **Keyword arguments** match arguments by the parameter names.
- **Default values** allow you to omit certain arguments when calling the function.

---

# Preventing Argument Errors in Python Functions

## What Are Argument Errors?

When working with functions, you might encounter errors if you pass too few or too many arguments than the function expects. These are called **argument errors**. Python provides detailed error messages to help you fix these issues quickly.

## Example: Missing Arguments

Let’s look at what happens when you call the `describe_pet()` function without providing the required arguments:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet()  # This will cause an error
```

### Error Output:

```
TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
```

Python tells us that the function `describe_pet()` is missing 2 arguments and shows the names of the missing arguments.

## Providing the Correct Arguments

To fix this, you need to make sure you provide the required arguments:

```python
describe_pet('cat', 'mitti')  # This works
```

### Output:

```
I have a cat.
My cat's name is Mitti.
```

## Too Many Arguments

If you provide more arguments than the function expects, you’ll encounter a similar error. For example:

```python
describe_pet('cat', 'mitti', 'extra')  # Too many arguments
```

### Error Output:

```
TypeError: describe_pet() takes 2 positional arguments but 3 were given
```

Python will let you know that too many arguments were provided.

#### How to Avoid Argument Errors

1. **Match the Number of Arguments**: Make sure the number of arguments in the function call matches the number of parameters in the function definition.
2. **Use Descriptive Names**: Naming your parameters clearly will help you identify errors more easily when reading error messages.

---

# T-Shirt Function Example

Write a function called `make_shirt()` that accepts a **size** and a **message** to be printed on the shirt. Then, call the function with positional and keyword arguments.

```python
def make_shirt(size, message):
    """Summarize the shirt size and message."""
    print(f"The shirt is size {size} and will say: '{message}'.")

# Positional arguments
make_shirt('L', 'I love Python')

# Keyword arguments
make_shirt(size='M', message='Coding is fun!')
```

---

# Default Values for Large Shirts

Modify the `make_shirt()` function so that the default shirt size is large, and the default message is "I love Python":

```python
def make_shirt(size='L', message='I love Python'):
    """Summarize the shirt size and message."""
    print(f"The shirt is size {size} and will say: '{message}'.")

# Using default values
make_shirt()
make_shirt('M')

# Custom message
make_shirt(size='S', message='Ali loves coding!')
```

---

# Describing Cities

Write a function `describe_city()` that accepts the name of a city and the country it’s in, with the country having a default value:

```python
def describe_city(city, country='Pakistan'):
    """Print a description of a city."""
    print(f"{city.title()} is in {country}.")

# Call with default country
describe_city('lahore')
describe_city('karachi')

# Call with a different country
describe_city('faisalabad', 'Pakistan')
```

---

# Return Values in Python Functions

## What Are Return Values?

A function doesn’t always need to display its output directly. Instead, it can process data and then return a value or set of values back to the part of your program that called the function. This is called a **return value**.

The `return` statement sends a value from inside a function back to the line that called the function. This allows you to move much of the complex logic into functions, keeping the main body of your program clean and simple.

## Returning a Simple Value

Let’s explore a function that takes a first name and last name and returns a neatly formatted full name:

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
```

### How It Works:
1. The function takes `first_name` and `last_name` as parameters.
2. It combines them into `full_name` and formats it in title case.
3. The `return` statement sends the formatted `full_name` back to the line that called the function.

## Calling a Function That Returns a Value

When you call a function that returns a value, you should assign that value to a variable so you can use it later. Let’s call the function and store the result in the variable `musician`:

```python
musician = get_formatted_name('ali', 'khan')
print(musician)
```

### Output:

```
Ali Khan
```

Here, the function returns the neatly formatted name "Ali Khan" and assigns it to the variable `musician`, which is then printed.

### Why Use Return Values?

While it may seem like extra work to use a function for something as simple as printing a name, this approach becomes much more useful in large programs. Imagine you have many first and last names stored separately. Instead of manually combining them, you can call `get_formatted_name()` whenever you need a full name, keeping your code organized and reusable.

For example, if you have a large list of names, you could call the function like this:

```python
names = [('ali', 'khan'), ('ayesha', 'bibi'), ('sana', 'malik')]

for first, last in names:
    full_name = get_formatted_name(first, last)
    print(full_name)
```

This would output:

```
Ali Khan
Ayesha Bibi
Sana Malik
```

---

# Making an Argument Optional in Python

## Why Make an Argument Optional?

Sometimes, you might want to allow an argument to be optional when calling a function. This provides flexibility to the function users—they can provide extra information only if needed. You can achieve this by using default values for function parameters.

## Example: Optional Middle Name

Let’s expand our `get_formatted_name()` function to handle middle names. First, here’s a version that requires a first name, middle name, and last name:

```python
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
```

This function expects all three parts of the name to be provided:

```python
musician = get_formatted_name('ali', 'hassan', 'khan')
print(musician)
```

### Output:

```
Ali Hassan Khan
```

But what if someone doesn’t have a middle name? The function would break if you only passed a first and last name.

## Making the Middle Name Optional

To handle cases where the middle name isn’t provided, we can set a default value of an empty string for the `middle_name` parameter. This way, the middle name is optional:

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
```

### How It Works Now:
1. The `middle_name` parameter has a default value of an empty string `''`.
2. The function checks if a middle name was provided using `if middle_name:`.
   - If a middle name is provided, it combines the first, middle, and last names.
   - If no middle name is provided, it only combines the first and last names.

## Calling the Function With or Without a Middle Name

You can now call the function with just a first and last name:

```python
musician = get_formatted_name('ali', 'khan')
print(musician)
```

### Output:

```
Ali Khan
```

Or, if a middle name is provided:

```python
musician = get_formatted_name('ali', 'khan', 'hassan')
print(musician)
```

### Output:

```
Ali Hassan Khan
```

This function now works for people with just a first and last name as well as for those who have a middle name. The middle name will only be included if provided.

---

# Returning a Dictionary in Python Functions

## Why Return a Dictionary?

In Python, a function can return more complex data structures like dictionaries and lists. This allows you to store and work with multiple pieces of information in a more organized way. For example, instead of returning just one value, you can return a dictionary that holds multiple pieces of related data.

## Example: Building a Dictionary for a Person

Let’s look at a function that takes a first name and last name, and returns a dictionary that stores these values:

```python
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
```

### How It Works:
1. The function takes `first_name` and `last_name` as inputs.
2. It stores these values in a dictionary, where the keys are `'first'` and `'last'`.
3. The dictionary is then returned to the calling line.

Let’s call this function:

```python
person_info = build_person('ali', 'khan')
print(person_info)
```

### Output:

```
{'first': 'Ali', 'last': 'Khan'}
```

This function takes simple text values and stores them in a meaningful dictionary.

## Adding Optional Information

You can easily extend this function to store additional information about a person, such as their age. By making the `age` parameter optional, the function becomes more flexible:

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
```

### How It Works:
- The new optional parameter `age` is added with a default value of `None`.
- If an age is provided when calling the function, it is added to the dictionary. If no age is provided, the dictionary will only include the first and last name.

Let’s call this extended version:

```python
person_info = build_person('ali', 'khan', age=28)
print(person_info)
```

### Output:

```
{'first': 'Ali', 'last': 'Khan', 'age': 28}
```

Now, the dictionary contains the person’s age along with their first and last name.

---

# Using a Function with a while Loop in Python

## Why Use Functions with a while Loop?

You can combine functions with a `while` loop to repeatedly perform actions based on user input. This is a common pattern in Python, where functions can be called within loops to handle repetitive tasks like gathering input, processing it, and displaying results.

## Example: Greeting Users with a while Loop

Let’s use the `get_formatted_name()` function to greet users more formally, repeatedly asking for their first and last names:

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name.lower() == 'q':
        break

    l_name = input("Last name: ")
    if l_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

### How It Works:
1. The `get_formatted_name()` function takes the first and last name and returns a neatly formatted full name.
2. The `while True` loop runs continuously, asking the user for their first and last name.
3. If the user enters `'q'` (in any case), the loop breaks.
4. The function processes the input and prints a greeting.

---

# City Names

Write a function called `city_country()` that takes in the name of a city and its country, and returns a formatted string like "Lahore, Pakistan".

```python
def city_country(city, country):
    """Return a city and country, neatly formatted."""
    return f"{city.title()}, {country.title()}"

# Calling the function with city-country pairs
print(city_country('lahore', 'pakistan'))
print(city_country('karachi', 'pakistan'))
print(city_country('islamabad', 'pakistan'))
```

---

# Album Dictionary

Write a function called `make_album()` that builds a dictionary describing a music album. It should take in the artist's name and album title, returning a dictionary. Use `None` to add an optional parameter for the number of songs.

```python
def make_album(artist, title, songs=None):
    """Return a dictionary of album information."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# Example album dictionaries
print(make_album('Atif Aslam', 'Jal Pari'))
print(make_album('Ali Zafar', 'Channo', songs=10))
print(make_album('Abida Parveen', 'Raqs-e-Bismil'))
```

---

# User Albums

Create a `while` loop that asks the user to enter an album’s artist and title, then calls `make_album()` to print the album dictionary. Include a quit option.

```python
while True:
    print("\nEnter the artist and album details:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    album_title = input("Album title: ")
    if album_title.lower() == 'q':
        break

    album = make_album(artist, album_title)
    print(f"\nAlbum Info: {album}")
```

---

# Passing a List to a Function in Python

## Why Pass a List?

In Python, it’s often useful to pass a list to a function, whether the list contains names, numbers, or more complex data like dictionaries. When you pass a list to a function, that function gets direct access to the contents of the list, allowing you to manipulate and work with the data more efficiently.

## Example: Greeting Users from a List

Let’s say you have a list of users and want to greet each one individually. You can pass this list of names to a function that will handle greeting them all:

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# List of usernames
usernames = ['ayesha', 'ali', 'sana']

# Calling the function and passing the list
greet_users(usernames)
```

### Output:

```
Hello, Ayesha!
Hello, Ali!
Hello, Sana!
```

Each user sees a personalized greeting based on their name in the list.

---

# Modifying a List in a Function in Python

## Why Modify a List Inside a Function?

When you pass a list to a function, the function has direct access to modify that list. Any changes made to the list within the function will be permanent, making this an efficient way to handle large amounts of data, especially when you need to update or reorganize lists.

## Example: 3D Printing Models

Imagine a company that 3D prints models from user-submitted designs. You have a list of unprinted designs and want to move them to a list of completed models once they’re printed.

Without using functions:

```python
# List of designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

### Output:

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

## Refactoring the Code with Functions

To make the program cleaner and more maintainable, let’s refactor it into two functions: one for printing the models and another for displaying the completed models.

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Display all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

# List of designs and an empty list for completed models.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the functions.
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

### Output:

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

#### Benefits of Refactoring with Functions

By breaking the program into two functions, the code becomes more organized, readable, and maintainable. Functions allow us to:
- Reuse code: You can call `print_models()` and `show_completed_models()` whenever you need to print and display designs.
- Improve readability: Descriptive function names make it easy to understand what each part of the program does.
- Maintain efficiency: If you need to change the printing process, you can modify it in one place.

---

# Preventing a Function from Modifying a List in Python

## Why Prevent a Function from Modifying a List?

Sometimes, you may want to prevent a function from modifying the original list you pass to it. This is especially useful when you want to keep a record of the original list. Instead of passing the original list to the function, you can pass a copy of the list. Any changes the function makes will only affect the copy, leaving the original list intact.

## Example: Copying a List to Prevent Changes

Let’s say you have a list of unprinted designs and want to move them to a list of completed models. To preserve the original list of unprinted designs, pass a copy of the list to the function:

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

# Original list of unprinted designs and an empty list for completed models.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Pass a copy of the unprinted_designs list to prevent modification of the original list.
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Print the original unprinted designs to show it's still intact.
print("\nOriginal list of unprinted designs:")
print(unprinted_designs)
```

### Output:

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case

Original list of unprinted designs:
['phone case', 'robot pendant', 'dodecahedron']
```

Any changes made inside the function affect only the copy, keeping the original list unchanged.

---

# Passing an Arbitrary Number of Arguments in Python

## What Are Arbitrary Arguments?

Sometimes, you won’t know ahead of time how many arguments a function needs to accept. In such cases, Python allows you to pass an arbitrary number of arguments using the asterisk `*`, which tells Python to pack all extra arguments into a tuple.

## Example: Making a Pizza with Multiple Toppings

Imagine a function that builds a pizza, where you can add any number of toppings. You can’t know ahead of time how many toppings a person will want. Here’s how you can handle that:

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

# Calling the function with one topping
make_pizza('pepperoni')

# Calling the function with multiple toppings
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

### Output:

```
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```

Python packs the arguments into a tuple, allowing the function to handle any number of toppings.

## Enhancing the Function with a Loop

Instead of just printing the tuple, let’s summarize the pizza order by listing all the toppings:

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Making pizzas with different toppings
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

### Output:

```
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

---

# Mixing Positional and Arbitrary Arguments in Python

## Why Mix Positional and Arbitrary Arguments?

In Python, you can combine positional arguments with arbitrary arguments in a function. When doing this, the positional arguments must come first, followed by the arbitrary arguments. This allows Python to correctly assign values to the parameters in your function.

## Example: Making a Pizza with a Size and Multiple Toppings

Let’s say we want to make pizzas where we specify both the size and any number of toppings. The size will be a positional argument, and the toppings will be collected using an arbitrary argument.

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Making pizzas with a size and various toppings
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

### Output:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

---

# Using Arbitrary Keyword Arguments in Python

## What Are Arbitrary Keyword Arguments?

Sometimes, you’ll want a function to accept an arbitrary number of key-value pairs, but you won’t know ahead of time what kind of information will be passed. In these cases, you can write functions that accept an arbitrary number of keyword arguments using `**`. Python collects these keyword arguments into a dictionary.

## Example: Building a User Profile

Let’s create a function called `build_profile()` that takes a first and last name, and also accepts any number of additional keyword arguments. These extra pieces of information will be stored in a dictionary:

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Building a profile with arbitrary keyword arguments
user_profile = build_profile('ali', 'khan', location='Karachi', field='Software Engineering', hobby='cricket')
print(user_profile)
```

### Output:

```
{'location': 'Karachi', 'field': 'Software Engineering', 'hobby': 'cricket', 'first_name': 'Ali', 'last_name': 'Khan'}
```

## Example: Storing Car Information

Write a function that stores information about a car. The function will always require the manufacturer and model, but it can accept other optional features like color or sunroof.

```python
def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Example call with arbitrary keyword arguments
car = make_car('toyota', 'corolla', color='white', sunroof=True)
print(car)
```

### Output:

```
{'color': 'white', 'sunroof': True, 'manufacturer': 'toyota', 'model': 'corolla'}
```

---

# Try It Yourself!

### 1. Sandwiches
Write a function that accepts a list of items a person wants on a sandwich and prints a summary of the sandwich being ordered.

```python
def make_sandwich(*items):
    """Summarize the sandwich with requested items."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese')
make_sandwich('chicken', 'avocado', 'bacon', 'mayo')
```

### 2. User Profile
Create a profile for yourself using `build_profile()` with your first and last name, and three other key-value pairs describing you.

```python
user_profile = build_profile('sana', 'malik', location='Lahore', profession='Data Scientist', hobby='reading')
print(user_profile)
```

### 3. Cars
Write a function that stores information about a car and accepts an arbitrary number of keyword arguments.

```python
car = make_car('honda', 'civic', color='silver', autopilot=True)
print(car)
```

---

This revised text now has no emojis and uses Pakistani names in the examples.