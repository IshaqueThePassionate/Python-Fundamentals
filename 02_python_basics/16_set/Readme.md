# Python Set Data Structure

A **set** is an unordered collection of unique and immutable elements in Python. It is defined by placing elements within curly braces `{}` or by using the built-in `set()` function.

## Key Characteristics of a Set:
- **Unordered:** The elements do not have a defined order.
- **Unique:** No duplicate elements are allowed.
- **Mutable:** You can add or remove elements from a set.

## Where Do We Use Sets in Python?

Sets are used in Python for tasks that require handling unique items and performing operations such as:
- Removing duplicates from a collection.
- Checking membership quickly.
- Executing mathematical operations like union, intersection, difference, and symmetric difference.

## Why Use Sets?

1. **Uniqueness:** Automatically eliminates duplicate entries.
2. **Efficient Membership Testing:** Provides an average-time complexity of O(1) for membership tests.
3. **Mathematical Operations:** Ideal for operations like union, intersection, and difference.

## Set Initialization Examples

### Creating a Set Using Curly Braces

```python
names_set = {"Ali", "Sana", "Ahmed", "Zara"}
print(names_set)  # Output: {'Ali', 'Ahmed', 'Sana', 'Zara'} (order may vary)
```

### Creating a Set Using the `set()` Constructor

```python
names_list = ["Ali", "Sana", "Ahmed", "Ahmed", "Zara", "Zara"]
names_set = set(names_list)
print(names_set)  # Output: {'Ali', 'Ahmed', 'Sana', 'Zara'} (duplicates removed)
```

### Creating an Empty Set

```python
empty_set = set()
print(empty_set)  # Output: set()
```

## Common Set Methods

Below is a detailed list of set methods with examples adapted to include Pakistani names.

### 1. `add()`
- **Purpose:** Adds an element to the set.
- **Example:**
  ```python
  students = {"Ali", "Sana", "Ahmed"}
  students.add("Hina")
  print(students)  # Output: {'Ali', 'Sana', 'Ahmed', 'Hina'}
  ```
- **Explanation:**  
  The `add()` method inserts "Hina" into the set. If the element already exists, it does nothing.

---

### 2. `clear()`
- **Purpose:** Removes all elements from the set.
- **Example:**
  ```python
  cities = {"Lahore", "Karachi", "Islamabad"}
  cities.clear()
  print(cities)  # Output: set()
  ```
- **Explanation:**  
  The `clear()` method empties the set, leaving it with no elements.

---

### 3. `copy()`
- **Purpose:** Returns a shallow copy of the set.
- **Example:**
  ```python
  original_names = {"Faisal", "Khadija", "Zainab"}
  copied_names = original_names.copy()
  copied_names.add("Omar")
  print(original_names)  # Output: {'Faisal', 'Khadija', 'Zainab'}
  print(copied_names)    # Output: {'Faisal', 'Khadija', 'Zainab', 'Omar'}
  ```
- **Explanation:**  
  A shallow copy creates a new set with the same elements. Modifications to the copy do not affect the original.

---

### 4. `difference()`
- **Purpose:** Returns a new set containing elements in the first set that are not in the second.
- **Example:**
  ```python
  team_A = {"Ali", "Sana", "Ahmed", "Hina"}
  team_B = {"Ahmed", "Hina", "Sadia"}
  diff = team_A.difference(team_B)
  print(diff)  # Output: {'Ali', 'Sana'}
  ```
- **Explanation:**  
  The `difference()` method identifies elements unique to `team_A` that are not present in `team_B`.

---

### 5. `difference_update()`
- **Purpose:** Removes elements from the set that are also in another set.
- **Example:**
  ```python
  primary_team = {"Ali", "Sana", "Ahmed", "Hina"}
  secondary_team = {"Ahmed", "Hina", "Sadia"}
  primary_team.difference_update(secondary_team)
  print(primary_team)  # Output: {'Ali', 'Sana'}
  ```
- **Explanation:**  
  `difference_update()` modifies `primary_team` by removing elements that are found in `secondary_team`.

---

### 6. `discard()`
- **Purpose:** Removes a specified element without raising an error if it is not found.
- **Example:**
  ```python
  colors = {"red", "green", "blue"}
  colors.discard("green")
  colors.discard("yellow")  # No error even though "yellow" is not in the set
  print(colors)  # Output: {'red', 'blue'}
  ```
- **Explanation:**  
  The `discard()` method removes the specified element safely.

---

### 7. `intersection()`
- **Purpose:** Returns a new set containing only the common elements between sets.
- **Example:**
  ```python
  group1 = {"Ali", "Sana", "Ahmed"}
  group2 = {"Ahmed", "Sadia", "Hassan"}
  common_members = group1.intersection(group2)
  print(common_members)  # Output: {'Ahmed'}
  ```
- **Explanation:**  
  `intersection()` extracts elements that appear in both groups.

---

### 8. `intersection_update()`
- **Purpose:** Updates the set to contain only elements found in both sets.
- **Example:**
  ```python
  club_members = {"Ali", "Sana", "Ahmed", "Hina"}
  new_members = {"Ahmed", "Hina", "Usman"}
  club_members.intersection_update(new_members)
  print(club_members)  # Output: {'Ahmed', 'Hina'}
  ```
- **Explanation:**  
  `intersection_update()` modifies `club_members` to keep only the members present in `new_members`.

---

### 9. `isdisjoint()`
- **Purpose:** Returns `True` if two sets have no elements in common.
- **Example:**
  ```python
  set_X = {"Kamran", "Shazia"}
  set_Y = {"Rashid", "Ayesha"}
  print(set_X.isdisjoint(set_Y))  # Output: True
  ```
- **Explanation:**  
  `isdisjoint()` verifies that the two sets have no overlapping elements.

---

### 10. `issubset()`
- **Purpose:** Returns `True` if every element of one set is present in another.
- **Example:**
  ```python
  junior_team = {"Ali", "Sana"}
  senior_team = {"Ali", "Sana", "Ahmed", "Hina"}
  print(junior_team.issubset(senior_team))  # Output: True
  ```
- **Explanation:**  
  The `issubset()` method confirms that all members of `junior_team` are included in `senior_team`.

---

### 11. `issuperset()`
- **Purpose:** Returns `True` if a set contains all elements of another set.
- **Example:**
  ```python
  full_team = {"Ali", "Sana", "Ahmed", "Hina", "Usman"}
  part_team = {"Ali", "Usman"}
  print(full_team.issuperset(part_team))  # Output: True
  ```
- **Explanation:**  
  `issuperset()` checks if `full_team` includes every member of `part_team`.

---

### 12. `pop()`
- **Purpose:** Removes and returns an arbitrary element from the set.
- **Example:**
  ```python
  applicants = {"Zara", "Sadia", "Faisal"}
  removed_applicant = applicants.pop()
  print("Removed:", removed_applicant)
  print("Remaining:", applicants)
  ```
- **Explanation:**  
  The `pop()` method removes a random element since sets are unordered.

---

### 13. `remove()`
- **Purpose:** Removes a specified element from the set and raises a `KeyError` if the element is not found.
- **Example:**
  ```python
  registration = {"Hassan", "Sana", "Ali"}
  registration.remove("Sana")
  print(registration)  # Output: {"Hassan", "Ali"}
  # registration.remove("Zainab")  # Would raise KeyError if uncommented.
  ```
- **Explanation:**  
  `remove()` is used when you are certain the element exists; otherwise, `discard()` is safer.

---

### 14. `symmetric_difference()`
- **Purpose:** Returns a new set with elements in either set, but not in both.
- **Example:**
  ```python
  set_A = {"Ali", "Ahmed", "Sana"}
  set_B = {"Sana", "Hina", "Usman"}
  sym_diff = set_A.symmetric_difference(set_B)
  print(sym_diff)  # Output: {'Ali', 'Ahmed', 'Hina', 'Usman'}
  ```
- **Explanation:**  
  `symmetric_difference()` returns the elements that are unique to each set.

---

### 15. `symmetric_difference_update()`
- **Purpose:** Updates the set with the symmetric difference of itself and another.
- **Example:**
  ```python
  team_one = {"Ali", "Sana", "Ahmed"}
  team_two = {"Ahmed", "Hina", "Usman"}
  team_one.symmetric_difference_update(team_two)
  print(team_one)  # Output: {'Ali', 'Sana', 'Hina', 'Usman'}
  ```
- **Explanation:**  
  This method updates `team_one` to contain only the elements not common with `team_two`.

---

### 16. `union()`
- **Purpose:** Returns a new set containing all elements from both sets.
- **Example:**
  ```python
  group_A = {"Ali", "Ahmed"}
  group_B = {"Ahmed", "Sana"}
  combined_group = group_A.union(group_B)
  print(combined_group)  # Output: {'Ali', 'Ahmed', 'Sana'}
  ```
- **Explanation:**  
  `union()` combines both sets while removing duplicates.

---

### 17. `update()`
- **Purpose:** Adds all elements from another iterable (e.g., list, set) to the set.
- **Example:**
  ```python
  enrolled = {"Zara", "Ali"}
  new_enrollments = ["Ahmed", "Sana", "Ali"]
  enrolled.update(new_enrollments)
  print(enrolled)  # Output: {'Zara', 'Ali', 'Ahmed', 'Sana'}
  ```
- **Explanation:**  
  `update()` incorporates all new elements into the set, ignoring duplicates.


