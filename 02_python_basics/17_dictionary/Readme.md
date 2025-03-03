# Python Dictionaries

A **dictionary** in Python is a collection of **key-value pairs**. Each key is associated with a value, and you can use a key to access its corresponding value. Dictionaries are defined using curly braces `{}` or with the `set()` function.

## What is a Dictionary?

A dictionary is a collection of items where each item has a key and a value. Keys must be unique and of an immutable type (such as strings, numbers, or tuples), while values can be of any type. Think of a dictionary like a real-life dictionary where a word (key) maps to its meaning (value).

### Key Points:
- A dictionary is defined using curly braces `{}`.
- **Keys** must be unique and can be of any immutable type (e.g., strings, numbers, or tuples).
- **Values** can be of any type, including other dictionaries.

## Working with Dictionaries

### Adding New Key-Value Pairs

Dictionaries are dynamic, allowing you to add key-value pairs at any time.

```python
student_0 = {'name': 'Ali', 'age': 18}
student_0['city'] = 'Lahore'
student_0['university'] = 'LUMS'
print(student_0)
```

**Explanation:**  
We add new key-value pairs `'city': 'Lahore'` and `'university': 'LUMS'` to the `student_0` dictionary.

### Modifying Values in a Dictionary

To change a value, simply assign a new value to an existing key.

```python
student_0 = {'name': 'Sana', 'age': 20}
print(f"Student's name is {student_0['name']}.")
student_0['name'] = 'Sadia'
print(f"Student's name is now {student_0['name']}.")
```

**Explanation:**  
The value for the key `'name'` is updated from `'Sana'` to `'Sadia'`.

### Removing Key-Value Pairs

Remove a key-value pair using the `del` statement.

```python
student_0 = {'name': 'Ahmed', 'age': 19, 'city': 'Karachi'}
del student_0['age']
print(student_0)
```

**Explanation:**  
The key `'age'` and its associated value are removed from the dictionary.

### Using `get()` to Access Values

The `get()` method safely accesses a value; it returns a default value if the key is not present.

```python
student_0 = {'name': 'Hassan', 'grade': 'A'}
print(student_0.get('grade', 'Grade not available'))
print(student_0.get('age', 'Age not provided'))
```

**Explanation:**  
`get()` retrieves the value for `'grade'`. Since `'age'` is missing, it returns the default message.

## Looping Through a Dictionary

### Looping Through Key-Value Pairs

```python
student_info = {'name': 'Faisal', 'age': 21, 'city': 'Islamabad'}
for key, value in student_info.items():
    print(f"{key}: {value}")
```

**Explanation:**  
The loop iterates through each key-value pair, printing the details of the student.

### Looping Through Keys

```python
languages = {'Ali': 'Python', 'Sana': 'Java', 'Ahmed': 'C++'}
for person in languages.keys():
    print(person.title())
```

**Explanation:**  
Iterates over all the keys in the `languages` dictionary and prints them in title case.

### Looping Through Values

```python
print("Programming languages used:")
for language in languages.values():
    print(language)
```

**Explanation:**  
Loops through all values and prints the programming languages.

### Looping Through Sorted Keys

```python
for person in sorted(languages.keys()):
    print(f"{person.title()}, thank you for your input.")
```

**Explanation:**  
The keys are sorted alphabetically before iteration, ensuring a consistent order.

## Dictionary Unpacking

Dictionary unpacking allows you to pass key-value pairs as arguments in functions or to merge dictionaries.

### Function Call with Unpacked Dictionary

```python
def display_student(name, city):
    print(f"{name} lives in {city}.")

student = {'name': 'Zara', 'city': 'Multan'}
display_student(**student)
```

**Explanation:**  
The `**` operator unpacks the `student` dictionary into keyword arguments.

### Merging Dictionaries Using `**`

```python
dict1 = {'name': 'Sadia', 'age': 22}
dict2 = {'city': 'Faisalabad', 'university': 'NUST'}
merged = {**dict1, **dict2}
print(merged)
```

**Explanation:**  
Dictionary unpacking merges `dict1` and `dict2` into a single dictionary.

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries.

### Creating a Dictionary from a List

```python
cities = ["Lahore", "Karachi", "Islamabad"]
populations = [11_000_000, 14_000_000, 1_000_000]
city_population = {city: pop for city, pop in zip(cities, populations)}
print(city_population)
```

**Explanation:**  
The comprehension pairs each city with its corresponding population, creating a dictionary.

### Filtering with Dictionary Comprehensions

```python
grades = {'Ali': 85, 'Sana': 92, 'Ahmed': 78, 'Hassan': 95}
high_scores = {student: score for student, score in grades.items() if score >= 90}
print(high_scores)
```

**Explanation:**  
Only students with scores 90 or above are included in `high_scores`.

### Inverting a Dictionary

```python
student_ids = {'Ali': 101, 'Sana': 102, 'Ahmed': 103}
id_students = {v: k for k, v in student_ids.items()}
print(id_students)
```

**Explanation:**  
The comprehension swaps keys and values, which can be useful for reverse lookups.

---

