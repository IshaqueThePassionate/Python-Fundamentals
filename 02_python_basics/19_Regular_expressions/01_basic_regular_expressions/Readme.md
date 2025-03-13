# Basic Regular Expressions

## Problem 1.1
### Matching Literal Text with Regular Expressions
We want to create a **regular expression** that matches the following sentence **exactly**:

**Sentence to Match:**
```
The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
```

This exercise helps us understand which characters in regular expressions have special meanings and which ones match themselves without any special rules. Let's break it down in a fun way!

### Solution

To match this sentence exactly, we need a **regular expression** like this:

```regex
The\s+punctuation\s+characters\s+in\s+the\s+ASCII\s+table\s+are:\s+↵
!"#\$%&'\(\)\*\+,-\./:;<=>\?@\[\\]\^_`\{\|}~
```

**Explanation:**

- **Special Characters Escaped**: Some characters have special roles in regular expressions. To match them **literally** (as they appear), we need to put a backslash `\` before them. For example:
  - `*` becomes `\*`
  - `?` becomes `\?`
  - `.` becomes `\.`

- **Normal Characters Match Themselves**: Characters like letters (A-Z, a-z), numbers (0-9), and some punctuation marks (like `,` or `:`) match themselves directly without any extra rules.

#### Example:

If we want to search for the string `$()*+.?[\^{|`, we use the regex:

```regex
\$\(\)\*\+\.\?\[\\\^\{\|
```

Each metacharacter has a backslash `\` before it to indicate that we want the **literal** character, not its special function.

### Tips for Beginners

- **Don’t Over-Escape!**: Avoid adding too many backslashes (`\`). Over-escaping can make your regex harder to read and understand. Only escape characters that need it!

- **Block Escape**: Some regex "flavors" support a feature called **block escape** using `\Q...\E`. Everything between `\Q` and `\E` is treated as **literal**, meaning you don’t have to escape any special characters.
  - Example:
    ```regex
    \Q!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\E
    ```
  - This is much easier to read than escaping each character individually!

### Case-Insensitive Matching

Regular expressions are **case-sensitive** by default. This means `regex` will match `regex`, but **not** `Regex`, `REGEX`, or `ReGeX`. If you want to match all of them, you can turn on **case insensitivity** using `(?i)`:

```regex
(?i)regex
```

- `(?i)` makes everything **after** it case-insensitive.
- `(?-i)` can turn case sensitivity back **on**.

Example:

```regex
sensitive(?i)caseless(?-i)sensitive
```

This will match `sensitiveCASELESSsensitive` but **not** `SENSITIVEcaselessSENSITIVE`. Think of `(?i)` and `(?-i)` as switches to turn case sensitivity on or off.

To match the exact pattern using the provided regular expression, you can use Python's `re` module. Here's the code to achieve this:

```python
import re

# The sentence to match
text_to_match = """The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~."""

# Regular expression to match the exact text
pattern = r"The\s+punctuation\s+characters\s+in\s+the\s+ASCII\s+table\s+are:\s+↵!"r"#\$%&'\(\)\*\+,-\./:;<=>\?@\[\\]\^_`\{\|}~"

# Performing the match
if re.fullmatch(pattern, text_to_match):
    print("The text matches the pattern exactly!")
else:
    print("The text does not match the pattern.")
```

### Explanation:
1. **`import re`**: Imports Python's regular expression library.
2. **`pattern`**: The regular expression pattern provided.
3. **`re.fullmatch()`**: Checks if the entire string matches the regular expression pattern.

This code will let you know if the provided text matches the exact pattern!

---

## Problem 1.2
### Matching Nonprintable Characters with Regular Expressions

We want to create a **regular expression** to match a string containing these nonprintable ASCII control characters: 

1. **Bell** (`\a`)
2. **Escape** (`\x1B`)
3. **Form Feed** (`\f`)
4. **Line Feed** (`\n`)
5. **Carriage Return** (`\r`)
6. **Horizontal Tab** (`\t`)
7. **Vertical Tab** (`\v`)

These characters have specific uses in programming and text processing. Each has a hexadecimal ASCII code that is used to represent it.

### Solution

#### Option 1: Common Escape Sequences and Hexadecimal Codes
```regex
\a\x1B\f\n\r\t\v
```
This uses the escape sequences and hexadecimal codes for each character:
- `\a` for Bell
- `\x1B` for Escape
- `\f` for Form Feed
- `\n` for Line Feed
- `\r` for Carriage Return
- `\t` for Horizontal Tab
- `\v` for Vertical Tab

#### Option 2: All Hexadecimal Codes
```regex
\x07\x1B\x0C\x0A\x0D\x09\x0B
```
This option uses the hexadecimal ASCII codes to represent each character:
- `\x07` for Bell
- `\x1B` for Escape
- `\x0C` for Form Feed
- `\x0A` for Line Feed
- `\x0D` for Carriage Return
- `\x09` for Horizontal Tab
- `\x0B` for Vertical Tab

### Python Code to Match Nonprintable Characters

```python
import re
# String to match
nonprintable_string = "\a\x1B\f\n\r\t\v"
# Regular expression pattern to match the nonprintable characters
pattern = r"\a\x1B\f\n\r\t\v"
# Matching the pattern
if re.fullmatch(pattern, nonprintable_string):
    print("The text matches the pattern exactly!")
else:
    print("The text does not match the pattern.")
```

### Explanation

1. **Use `\x1B` for Escape**: Python's `re` module does not support `\e`, so we use the hexadecimal `\x1B`.
2. **Other Characters**: Escape sequences like `\a`, `\f`, `\n`, `\r`, `\t`, and `\v` are directly supported.
3. **`re.fullmatch()`**: Ensures the entire string matches the provided pattern.

### Usage of Each Nonprintable Character

1. **Bell (`\a`)**: Triggers an alert sound in terminals or consoles.
2. **Escape (`\x1B`)**: Starts an escape sequence for formatting text in terminals.
3. **Form Feed (`\f`)**: Moves the cursor to the next page or clears the screen.
4. **Line Feed (`\n`)**: Represents a newline in UNIX-based systems.
5. **Carriage Return (`\r`)**: Moves the cursor to the beginning of the current line.
6. **Horizontal Tab (`\t`)**: Adds horizontal spacing.
7. **Vertical Tab (`\v`)**: Moves the cursor vertically to the next tab stop.

---

## Problem 1.3

### Match One of Many Characters 

We need to create **regular expressions** (regex) that solve the following problems:

1. **Match all common misspellings of the word "calendar."**  
   Allow either "a" or "e" in each vowel position. This helps us catch different variations of spelling without worrying about exact correctness.
   
2. **Match a single hexadecimal character.**  
   This is a character that is part of the set 0-9 or A-F (case-insensitive).
   
3. **Match a single character that is not a hexadecimal character.**  
   This is any character that is not in the set 0-9 or A-F.

These problems introduce us to a powerful regex feature called **character classes**.

### Solution

#### 1. Matching Common Misspellings of "Calendar"

```python
import re

# Regex to match common misspellings of 'calendar'
calendar_regex = r'c[ae]l[ae]nd[ae]r'

# Example usage
text = "calender, calandar, celendar, celandar"
matches = re.findall(calendar_regex, text)
print(matches)  # Output: ['calender', 'calandar', 'celendar', 'celandar']
```

**Explanation:**

- **Pattern Breakdown**:
  - `c[ae]l[ae]nd[ae]r`:
    - `c` matches the letter "c."
    - `[ae]` matches either "a" or "e."
    - `l` matches the letter "l."
    - `[ae]` again matches either "a" or "e."
    - `nd` matches the sequence "nd."
    - `[ae]` matches either "a" or "e."
    - `r` matches the letter "r."
- **Result**: This regex will match all variations of the word "calendar" where each vowel can be either "a" or "e."

#### 2. Matching a Single Hexadecimal Character

```python
# Regex to match a single hexadecimal character
hex_char_regex = r'[a-fA-F0-9]'

# Example usage
text = "1, A, g, 3F, Z"
matches = re.findall(hex_char_regex, text)
print(matches)  # Output: ['1', 'A', '3', 'F']
```

**Explanation:**

- **Pattern Breakdown**:
  - `[a-fA-F0-9]`:
    - Matches any lowercase letter from "a" to "f."
    - Matches any uppercase letter from "A" to "F."
    - Matches any digit from "0" to "9."
- **Result**: This regex will match any valid hexadecimal character.

#### 3. Matching a Single Non-Hexadecimal Character

```python
# Regex to match a single non-hexadecimal character
non_hex_char_regex = r'[^a-fA-F0-9]'

# Example usage
text = "1, A, g, 3F, Z, !"
matches = re.findall(non_hex_char_regex, text)
print(matches)  # Output: [',', ' ', ',', ' ', 'g', ',', ' ', ',', ' ', 'Z', ',', ' ', '!']
```

**Explanation:**

- **Pattern Breakdown**:
  - `[^a-fA-F0-9]`:
    - `^` placed at the beginning negates the character class.
    - Matches any character that is **not** a hexadecimal character.
- **Result**: This regex will match any character that is not a hexadecimal character.

### Explanation

A **character class** is a group of characters you put inside square brackets `[]`. It matches **one single character** from the list inside the brackets.

#### Key Points on Character Classes

- **Metacharacters** in character classes:
  - `\`, `^`, `-`, `]` (special handling is required)
- **Shorthand Classes**:
  - `\d`: Matches any digit (`[0-9]`).
  - `\D`: Matches any non-digit (`[^0-9]`).
  - `\w`: Matches any word character (`[a-zA-Z0-9_]`).
  - `\W`: Matches any non-word character (`[^a-zA-Z0-9_]`).
  - `\s`: Matches any whitespace character.
  - `\S`: Matches any non-whitespace character.

#### Case Insensitivity with Character Classes

You can make a regex **case-insensitive** using the `(?i)` flag:

```python
# Case insensitive match for hexadecimal characters
case_insensitive_hex_regex = r'(?i)[a-f0-9]'

# Example usage
text = "A, b, C, d, 3, F"
matches = re.findall(case_insensitive_hex_regex, text)
print(matches)  # Output: ['A', 'b', 'C', 'd', '3', 'F']
```

- **Explanation**: `(?i)` makes the regex case-insensitive.

---

## Problem 1.4

### Match Any Character

We need to create **regular expressions** (regex) that solve the following problems:

1. **Match any single character except a line break.**  
   This will match any character except for newline characters (like `\n`).

2. **Match any single character including line breaks.**  
   This will match all characters, even newline characters.

### Solution

#### 1. Match Any Character Except Line Breaks

To match **any single character** except for line breaks, we use the dot `.` metacharacter in regex.

```python
import re

regex_any_char_except_linebreaks = r'.'

text = "Hello! How are \nyou?"
matches = re.findall(regex_any_char_except_linebreaks, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
```

**Explanation:**

- **Pattern Breakdown**:
  - `.`: The dot metacharacter matches **any single character** except for line break characters (`\n`, `\r`).
- **Result**: The regex matches every character in the string except line breaks.

#### 2. Match Any Character Including Line Breaks

To match **any character including line breaks**, we have two options:

1. **Enable Dot to Match Line Breaks**: Some programming languages have a special option to allow the dot to match line breaks.
2. **Use a Character Class Combination**: A character class like `[\s\S]` matches both whitespace (`\s`) and non-whitespace (`\S`) characters, effectively matching any character.

```python
# Regex to match any character, including line breaks
regex_any_char_including_linebreaks = r'[\s\S]'

# Example usage
text = "Hello!\nHow are you?"
matches = re.findall(regex_any_char_including_linebreaks, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', '\n', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
```

**Explanation:**

- **Pattern Breakdown**:
  - `[\s\S]`: Combines `\s` (whitespace) and `\S` (non-whitespace) to match **any character**, including line breaks.
- **Result**: The regex matches every character, including line breaks.

#### Alternative Method with Mode Modifier

```python
# Regex with mode modifier to match any character, including line breaks
regex_with_mode_modifier = r'(?s).'

# Example usage
text = "Hello!\nHow are you?"
matches = re.findall(regex_with_mode_modifier, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', '\n', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
```

- **Explanation**: `(?s)` enables "dot matches line breaks" mode and then `.` matches any character.

---

## Problem 1.5

### Match Something at the Start and/or the End of a Line

We need to create **regular expressions** (regex) to solve the following problems:

1. **Match the word "alpha" only at the start of the entire text.**  
2. **Match the word "omega" only at the end of the entire text.**  
3. **Match the word "begin" only at the start of a line.**  
4. **Match the word "end" only at the end of a line.**

These solutions introduce the concept of **anchors** in regex.

### Solution

#### 1. Match the Word "alpha" Only at the Start of the Text

```python
import re

# Regex to match "alpha" at the start of the text
regex_start_alpha = r'^\balpha\b'

# Example usage
text1 = "alpha is at the beginning. Not in between."
text2 = "Is alpha at the beginning. Not in between."
matche1 = re.findall(regex_start_alpha, text1)
matche2 = re.findall(regex_start_alpha, text2)
print(matche1)  # Output: ['alpha']
print(matche2)  # Output: No match
```

**Explanation:**

- **Pattern Breakdown**:
  - `^`: Matches the **start** of the text.
  - `\balpha\b`: Matches the word "alpha" as a **whole word**.
- **Result**: The regex matches "alpha" only if it appears at the start of the text.

Alternatively, you can use `\A`:

```python
regex_start_alpha = r'\Aalpha'
```

#### 2. Match the Word "omega" Only at the End of the Text

```python
# Regex to match "omega" at the end of the text
regex_end_omega = r'\bomega\b$'

# Example usage
text1 = "Not in between, but omega is at the end."
text2 = "Not in between, but  is at the end omega"
matche1 = re.findall(regex_end_omega, text1)
matche2 = re.findall(regex_end_omega, text2)
print(matche1)  # Output: No match
print(matche2)  # Output: ['omega']
```

**Explanation:**

- **Pattern Breakdown**:
  - `\bomega\b`: Matches the word "omega" as a **whole word**.
  - `$`: Matches the **end** of the text.
- **Result**: The regex matches "omega" only if it appears at the end of the text.

Alternatively, you can use `\Z`:

```python
regex_end_omega = r'omega\Z'
```

#### 3. Match the Word "begin" Only at the Start of a Line

```python
# Regex to match "begin" at the start of a line
regex_line_start_begin = r'^begin'

# Example usage
text1 = "Not in between.\nbegin is at the start of a line."
text2 = "Not in between.\n begin is at the start of a line."
matche1 = re.findall(regex_line_start_begin, text1, re.MULTILINE)
matche2 = re.findall(regex_line_start_begin, text2, re.MULTILINE)
print(matche1)  # Output: ['begin']
print(matche2)  # Output: No match
```

**Explanation:**

- **Pattern Breakdown**:
  - `^`: Matches the **start** of each line in **multiline mode**.
  - `begin`: Matches the word "begin".
- **Result**: The regex matches "begin" only if it appears at the start of a line.

#### 4. Match the Word "end" Only at the End of a Line

```python
# Regex to match "end" at the end of a line
regex_line_end_end = r'end$'

# Example usage
text1 = "Not in between.\nBut this line ends with end"
text2 = "Not in between.\nBut this line ends end with"
matche1 = re.findall(regex_line_end_end, text1, re.MULTILINE)
matche2 = re.findall(regex_line_end_end, text2, re.MULTILINE)
print(matche1)  # Output: ['end']
print(matche2)  # Output: No match
```

**Explanation:**

- **Pattern Breakdown**:
  - `end`: Matches the word "end".
  - `$`: Matches the **end** of each line in **multiline mode**.
- **Result**: The regex matches "end" only if it appears at the end of a line.

### Explanation

**Anchors** are special regex tokens that match positions in the text rather than actual characters:

- `^`: Matches the **start** of the text or line.
- `$`: Matches the **end** of the text or line.
- `\A`: Matches the **start** of the entire text.
- `\Z`: Matches the **end** of the entire text, just before a trailing newline.

---

## Problem 1.6

### Match Whole Words 

We need to create **regular expressions** (regex) that solve the following problems:

1. **Match the word "cat" only if it appears as a whole word** in a sentence like "My cat is brown," but **not** in words like "category" or "bobcat."
2. **Match the word "cat" only if it is part of another word**, such as in "staccato," but **not** as a standalone word like in "My cat is brown."

### Solution

#### 1. Match the Word "cat" Only as a Whole Word

```python
import re

# Regex to match "cat" as a whole word
regex_whole_word_cat = r'\bcat\b'

# Example usage
text = "My cat is brown. A category is different from a cat."
matches = re.findall(regex_whole_word_cat, text)
print(matches)  # Output: ['cat', 'cat']
```

**Explanation:**

- **Pattern Breakdown**:
  - `\b`: Matches a **word boundary**.
  - `cat`: Matches the literal string "cat".
  - `\b`: Matches another **word boundary**.
- **Result**: This regex will match "cat" only if it appears as a separate word.

#### 2. Match the Word "cat" Only If It Is Part of Another Word

```python
# Regex to match "cat" only if it is part of another word
regex_non_whole_word_cat = r'\Bcat\B'

# Example usage
text = "My cat is brown. staccato is a word, and so is bobcat."
matches = re.findall(regex_non_whole_word_cat, text)
print(matches)  # Output: ['cat', 'cat']
```

**Explanation:**

- **Pattern Breakdown**:
  - `\B`: Matches a **non-word boundary**.
  - `cat`: Matches the literal string "cat".
  - `\B`: Matches another **non-word boundary**.
- **Result**: This regex will match "cat" only when it is part of another word.

### Explanation

- **`\b` (Word Boundary)**: Matches the position where a word character is next to a non-word character.
- **`\B` (Non-Word Boundary)**: Matches the position not at a word boundary.

---

## Problem 1.7

### Unicode Code Points, Categories, Blocks, and Scripts

We need to use **regular expressions** (regex) to solve the following problems related to Unicode:

1. **Find the trademark sign (™) by specifying its Unicode code point** rather than copying and pasting it.
2. **Match any character that belongs to the "Currency Symbol" Unicode category**.
3. **Match any character in the "Greek Extended" Unicode block**.
4. **Match any character that is part of the "Greek" script according to Unicode**.
5. **Match a grapheme (a base character with all its combining marks)**.

### Explanation of `\p{}` in Regex

The `\p{}` notation in regular expressions is used to match **Unicode properties**. It allows matching characters based on their Unicode properties (letters, numbers, symbols, scripts, blocks, etc.).

#### Installing the `regex` Module

Python's built-in `re` module does not support the `\p{}` syntax. To use Unicode properties like `\p{Sc}` (currency symbol), install the `regex` module:

```bash
pip install regex
```

### Solution Table

| **Category**                         | **Description**                                                    | **Regex Pattern**              | **Python Example**                                      |
|--------------------------------------|--------------------------------------------------------------------|--------------------------------|---------------------------------------------------------|
| **Unicode Code Point**               | Matches a specific Unicode character by its code point.            | `\u2122`                      | `r'\u2122'` for ™ (trademark)                            |
| **Currency Symbol Category**         | Matches any currency symbol like $, €, ¥, etc.                     | `\p{Sc}`                      | `r'\p{Sc}'` (requires `regex` module)                   |
| **Greek Extended Block**             | Matches any character in the Greek Extended Unicode block.         | `[\u1F00-\u1FFF]`             | `r'[\u1F00-\u1FFF]'`                                    |
| **Greek Script**                     | Matches any character in the Greek script.                         | `[\u0370-\u03FF]`             | `r'[\u0370-\u03FF]'`                                    |
| **Grapheme (Base + Combining Marks)** | Matches a grapheme (base character and its combining marks).         | `(\P{M}\p{M}*)`               | `r'(\P{M}\p{M}*)'`                                     |

### Detailed Examples

#### 1. Find the Trademark Sign (™) by Unicode Code Point

```python
import re

# Regex to find the trademark sign (™)
regex_trademark = r'\u2122'

text = "This is a trademark symbol ™ and here is another one: ™."
matches = re.findall(regex_trademark, text)
print(matches)  # Output: ['™', '™']
```

#### 2. Match Any Character in the "Currency Symbol" Unicode Category

```python
import regex as re  # Use 'regex' module instead of 're'

# Regex to match any currency symbol
regex_currency = r'\p{Sc}'

text = "The price is $100 or €85 or ¥1000."
matches = re.findall(regex_currency, text)
print(matches)  # Output: ['$', '€', '¥']
```

#### 3. Match Any Character in the "Greek Extended" Unicode Block

```python
import re

# Regex to match any character in the "Greek Extended" block
regex_greek_extended = r'[\u1F00-\u1FFF]'

text = "Greek letters: ἀ ἁ ἂ ἃ."
matches = re.findall(regex_greek_extended, text)
print(matches)  # Output: ['ἀ', 'ἁ', 'ἂ', 'ἃ']
```

#### 4. Match Any Character in the "Greek" Script

```python
import re

# Regex to match any character in the "Greek" script
regex_greek_script = r'[\u0370-\u03FF]'

text = "Greek letters: Α, Β, Γ, Δ, ε, ζ."
matches = re.findall(regex_greek_script, text)
print(matches)  # Output: ['Α', 'Β', 'Γ', 'Δ', 'ε', 'ζ']
```

#### 5. Match a Grapheme (Base Character with All Its Combining Marks)

```python
import regex as re  # Use 'regex' module

# Regex to match a grapheme (base character + combining marks)
regex_grapheme = r'(\P{M}\p{M}*)'

text = "à is a grapheme."
matches = re.findall(regex_grapheme, text)
print(matches)  # Output: ['à', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'r', 'a', 'p', 'h', 'e', 'm', 'e', '.']
```

---

## Problem 2.8
### Match One of Several Alternatives

We need to create a **regular expression** (regex) that matches one of several alternatives. Specifically, we want a regex that matches any of the names "Muhammad," "Hashim," or "Ali" in the following text:

```
Muhammad, Hashim, and Ali went to Muhammad's house.
```

The regex should be applied repeatedly to find each name in the text until no more matches are found.

### Solution

To match any of the names "Muhammad," "Hashim," or "Ali," we can use the **pipe symbol** (`|`) to create an **alternation** in regex:

```python
import re

# Regex to match "Muhammad", "Hashim", or "Ali"
regex_names = r'Muhammad|Hashim|Ali'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
```

**Explanation:**

- **Pattern Breakdown**:
  - `Muhammad|Hashim|Ali`: This regex uses the pipe symbol (`|`) to specify an **alternation**. It matches **either** "Muhammad," **or** "Hashim," **or** "Ali."
- **Result**: The regex finds all occurrences of the names in the text.

### Example with Word Boundaries

If you want to ensure that only **whole words** are matched, you can use **word boundaries** (`\b`):

```python
import re

# Regex to match whole words "Muhammad", "Hashim", or "Ali"
regex_names_whole = r'\bMuhammad\b|\bHashim\b|\bAli\b'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names_whole, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
```

**Explanation:**

- **Pattern Breakdown**:
  - `\bMuhammad\b|\bHashim\b|\bAli\b`: Uses word boundaries to ensure only whole words are matched.
- **Result**: The regex prevents partial matches.

---

## Problem 2.9

### Group and Capture Parts of the Match

We need to create **regular expressions** (regex) that solve the following problems:

1. Improve the regex for matching "Muhammad," "Hashim," or "Ali" by ensuring that the match is a **whole word** using a single pair of word boundaries around a grouped alternation.
2. Create a regex to match any date in the format `yyyy-mm-dd` and separately capture the **year**, **month**, and **day** for easy processing.

### Solution

#### 1. Matching Whole Words with Grouping

```python
import re

# Regex to match whole words "Muhammad", "Hashim", or "Ali" using grouping
regex_names = r'\b(Muhammad|Hashim|Ali)\b'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
```

**Explanation:**

- **Pattern Breakdown**:
  - `\b`: Word boundary at the beginning.
  - `(Muhammad|Hashim|Ali)`: Group that matches any of the three names.
  - `\b`: Word boundary at the end.
- **Result**: Matches whole word occurrences.

#### 2. Capturing Groups for Dates in `yyyy-mm-dd` Format

```python
import re

# Regex to match and capture date parts in yyyy-mm-dd format
regex_date = r'\b(\d{4})-(\d{2})-(\d{2})\b'

# Example text with a date
text = "The event is scheduled for 2024-09-12."

# Find all matches with captured groups
matches = re.findall(regex_date, text)
print(matches)  # Output: [('2024', '09', '12')]

# Extracting year, month, and day from the first match
if matches:
    year, month, day = matches[0]
    print(f"Year: {year}, Month: {month}, Day: {day}")
```

**Explanation:**

- **Pattern Breakdown**:
  - `(\d{4})`: Captures the **year**.
  - `(\d{2})`: Captures the **month**.
  - `(\d{2})`: Captures the **day**.
- **Result**: Captures year, month, and day separately.

#### Complete Example

```python
import re

# Example 1: Matching Whole Words "Muhammad", "Hashim", or "Ali"
regex_names = r'\b(Muhammad|Hashim|Ali)\b'
text_names = "Muhammad, Hashim, and Ali went to Muhammad's house."

matches_names = re.findall(regex_names, text_names)
print("Matching Names:", matches_names)

# Example 2: Matching and Capturing Dates in yyyy-mm-dd Format
regex_date = r'\b(\d{4})-(\d{2})-(\d{2})\b'
text_date = "The event is scheduled for 2024-09-12."

matches_date = re.findall(regex_date, text_date)
print("Matching Dates:", matches_date)

if matches_date:
    year, month, day = matches_date[0]
    print(f"Year: {year}, Month: {month}, Day: {day}")
```

#### Non-Capturing Groups Example

```python
# Non-capturing group for matching "Muhammad", "Hashim", or "Ali"
regex_names_non_capture = r'\b(?:Muhammad|Hashim|Ali)\b'
regex_date_without_capture = r'\b(?:\d{4})-(?:\d{2})-(?:\d{2})\b'

text = "The event is scheduled for 2024-09-12."

matches = re.findall(regex_date, text)
print(matches)  # Output: [('2024', '09', '12')]
matches = re.findall(regex_date_without_capture, text)
print(matches)  # Output: ['2024-09-12']
```

---

## Problem 2.0

### Match Previously Matched Text Again

We want to create a regular expression that matches **"magical" dates** in the format `yyyy-mm-dd`. A date is considered **magical** if the last two digits of the year, the month, and the day are all the same. For example, `2008-08-08` is a magical date.

### Solution

```python
import re

# Regex to match "magical" dates in yyyy-mm-dd format
regex_magical_date = r'\b\d\d(\d\d)-\1-\1\b'

# Example text containing dates
text_dates = "Here are some dates: 2008-08-08, 1999-12-12, 2024-09-12, and 2011-11-11."

# Find all magical dates
matches_magical_dates = re.findall(regex_magical_date, text_dates)
print("Magical Dates:", matches_magical_dates)
```

**Explanation:**

- **Pattern Breakdown**:
  - `\d\d`: Matches the first two digits of the year.
  - `(\d\d)`: Captures the last two digits.
  - `-\1-\1`: Uses backreferences to ensure the month and day match the captured two digits.
- **Result**: Only dates where the last two digits of the year, month, and day match will be considered magical.

---

## Problem 2.1

### Capture and Name Parts of the Match

1. **Match any date** in the `yyyy-mm-dd` format and capture the year, month, and day with **descriptive names**.
2. **Match "magical" dates** in the `yyyy-mm-dd` format and capture the magical number as `"magic"`.

#### Named Capture for Dates

```python
import re

# Regex to match dates and capture year, month, and day
regex_named_date = r'\b(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\b'

text_dates = "Here are some dates: 2024-09-12, 1999-12-25, 2008-08-08."

matches_dates = re.finditer(regex_named_date, text_dates)
for match in matches_dates:
    print(f"Year: {match.group('year')}, Month: {match.group('month')}, Day: {match.group('day')}")
```

#### Named Capture for Magical Dates

```python
# Regex to match "magical" dates and capture the magical number
regex_magical_named = r'\b\d{2}(?P<magic>\d{2})-(?P=magic)-(?P=magic)\b'

text_magical_dates = "Some magical dates are: 2008-08-08, 2024-09-12, and 2011-11-11."

matches_magical = re.finditer(regex_magical_named, text_magical_dates)
for match in matches_magical:
    print(f"Magical Number: {match.group('magic')}")
```

**Explanation:**

1. **Named Capture for Dates**:
   - `(?P<year>\d{4})`: Captures the year.
   - `(?P<month>\d{2})`: Captures the month.
   - `(?P<day>\d{2})`: Captures the day.
2. **Named Capture for Magical Dates**:
   - `(?P<magic>\d{2})`: Captures the magical number.
   - `(?P=magic)`: Ensures that the month and day match the captured magical number.

---

## Problem 2.2

### Repeating Parts of a Regex a Certain Number of Times

Create regular expressions to match these types of numbers:

1. **Googol**: A number with exactly 100 digits.
2. **32-bit Hexadecimal Number**: A number with 1 to 8 hexadecimal digits.
3. **32-bit Hexadecimal Number with Optional 'h' Suffix**.
4. **Floating-Point Number**: A number that has a decimal point, with optional integer and exponent parts.

#### 1. Match a Googol (100-digit Number)

```python
import re

# Match a googol (100-digit number)
regex_googol = r'\b\d{100}\b'

text = "Number: 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890."
matches = re.findall(regex_googol, text)
print("Googol Matches:", matches)
```

#### 2. Match a 32-bit Hexadecimal Number

```python
# Match a 32-bit hexadecimal number
regex_hex = r'\b[a-f0-9]{1,8}\b'
text = "Hex numbers: 1a2b, deadbeef, 01234567."
matches = re.findall(regex_hex, text, re.IGNORECASE)
print("Hexadecimal Matches:", matches)
```

#### 3. Match a 32-bit Hexadecimal Number with Optional 'h' Suffix

```python
# Match a 32-bit hexadecimal number with optional 'h'
regex_hex_suffix = r'\b[a-f0-9]{1,8}h?\b'
text = "Hex numbers: 1a2bh, deadbeef, 01234567h."
matches = re.findall(regex_hex_suffix, text, re.IGNORECASE)
print("Hexadecimal Matches with 'h' suffix:", matches)
```

#### 4. Match a Floating-Point Number

```python
# Match a floating-point number
regex_float = r'\d*\.\d+(?:e\d+)?'
text = "Floating-point numbers: 0.5, 1.23e10, .75."
matches = re.findall(regex_float, text)
print("Floating-Point Matches:", matches)
```

**Explanation:**

- **Googol**: `\d{100}` matches exactly 100 digits.
- **Hexadecimal Number**: `[a-f0-9]{1,8}` matches between 1 and 8 hexadecimal digits.
- **Optional 'h' Suffix**: `h?` makes the 'h' optional.
- **Floating-Point Number**: Ensures a decimal point is present with optional exponent.

---

## Problem 2.3

### Choose Minimal or Maximal Repetition

Match a pair of `<p>` and `</p>` XHTML tags and the text between them. The text between the tags may contain other XHTML tags.

#### Correct Regex to Match Text Between `<p>` and `</p>` Tags

```python
import re

# Correct regex to match text between <p> and </p> tags
regex_lazy = r'<p>.*?</p>'

text = """
<p>
The very <em>first</em> task is to find the beginning of a paragraph.
</p>
<p>
Then you have to find the end of the paragraph
</p>
"""

# Find all matches for text between <p> and </p> tags
matches = re.findall(regex_lazy, text, re.DOTALL)
print("Matched Paragraphs:", matches)
```

**Explanation:**

- **`.*?`**: The lazy quantifier ensures matching stops at the first occurrence of `</p>`.

---

## Problem 2.4

### Eliminate Needless Backtracking 

Sometimes, regex patterns perform **unnecessary backtracking** which can slow down matching. Consider these two patterns:

1. **Greedy Quantifier:** `\b\d+\b`
2. **Lazy Quantifier:** `\b\d+?\b`

Both match integers and find the same results, but both can backtrack unnecessarily.

#### Python Code Example

```python
import re

text = "123abc 456"

# Greedy quantifier example
regex_greedy = r'\b\d+\b'
matches_greedy = re.findall(regex_greedy, text)
print("Greedy Matches:", matches_greedy)

# Lazy quantifier example
regex_lazy = r'\b\d+?\b'
matches_lazy = re.findall(regex_lazy, text)
print("Lazy Matches:", matches_lazy)
```

**Expected Output:**

```
Greedy Matches: ['123', '456']
Lazy Matches: ['123', '456']
```

**Explanation:**

Both patterns match the same integers, but they differ in how they attempt to match.

---

## Problem 2.5

### Prevent Runaway Repetition

When using repeating regex patterns (like `.*?`), the regex engine might take a long time to match if the pattern can't be fully matched, a situation known as **catastrophic backtracking**.

#### Example:

```regex
<.*?></html>
```

If the `</html>` tag is missing, `.*?` may keep expanding, trying every possible match.

#### Solution: Use Atomic Grouping

```regex
(?>.*?</body>)</html>
```

This atomic group `(?>.*?</body>)` prevents backtracking if `</html>` isn’t found.

#### Python Code Example

```python
import re

text = """
<html>
  <body>
    Some content here.
  </body>
  <div>
    More content without closing the HTML tag.
"""

regex_atomic = r'(?>.*?</body>)</html>'
matches_atomic = re.findall(regex_atomic, text, re.DOTALL)
print("Matches with Atomic Grouping:", matches_atomic)
```

**Expected Output:**

```
Matches with Atomic Grouping: []
```

**Explanation:**

- The atomic group locks in the match, preventing excessive backtracking.

---

## Problem 2.6

### Test for a Match Without Including It in the Overall Match

We want to find any word that appears between `<b>` and `</b>` tags without including the tags in the match. For example, in `"My <b>cat</b> is furry"`, the match should only be `"cat"`.

#### Regex Pattern Using Lookaround

```python
import re

text = "My <b>cat</b> is furry"
regex_pattern = r"(?<=<b>)\w+(?=</b>)"
matches = re.findall(regex_pattern, text)
print("Matches:", matches)
```

**Expected Output:**

```
Matches: ['cat']
```

**Explanation:**

- `(?<=<b>)`: Positive lookbehind ensures `<b>` precedes.
- `(?=</b>)`: Positive lookahead ensures `</b>` follows.

#### Alternative Using Capturing Group

```python
import re

text = "My <b>cat</b> is furry"
regex_pattern = r"<b>(\w+)(?=</b>)"
matches = re.findall(regex_pattern, text)
print("Matches without lookbehind:", matches)
```

**Expected Output:**

```
Matches without lookbehind: ['cat']
```

---

## Problem 2.7

### Match One of Two Alternatives Based on a Condition

Create a regex to match a **comma-delimited list** containing the words `one`, `two`, and `three`. Each word can appear any number of times and in any order, but **each must appear at least once**.

#### Regex Pattern with Conditionals

```regex
\b(?:(?:(one)|(two)|(three))(?:,|\b)){3,}(?(1)|(?!))(?(2)|(?!))(?(3)|(?!))
```

**Explanation:**

1. **`\b`**: Ensures whole words.
2. **`(?:(one)|(two)|(three))`**: Captures each word in separate groups.
3. **`(?:,|\b)`**: Matches a comma or a word boundary.
4. **`{3,}`**: Ensures at least three matches.
5. **Conditionals**: `(?(1)|(?!))` for group 1, etc., ensure each word appears at least once.

#### Python Code Example Using Conditionals

```python
import re

text = "one,two,three,one,two"
regex_pattern = r'\b(?:(?:(one)|(two)|(three))(?:,|\b)){3,}(?(1)|(?!))(?(2)|(?!))(?(3)|(?!))'
match = re.match(regex_pattern, text)

if match:
    print("Valid match: All three words are present at least once.")
else:
    print("Invalid match: Not all three words are present.")
```

**Expected Output:**

```
Valid match: All three words are present at least once.
```

#### Simpler Alternative (Without Conditionals)

```python
import re

text = "one,two,three,one,two"
regex_pattern_simple = r'\b(?:(one|two|three)(?:,|\b)){3,}'
matches = re.findall(regex_pattern_simple, text)

if set(matches) == {'one', 'two', 'three'}:
    print("Valid match: All three words are present at least once.")
else:
    print("Invalid match: Not all three words are present.")
```

**Expected Output:**

```
Valid match: All three words are present at least once.
```

---

## Problem 2.8

### Add Comments to a Regular Expression

We have a regex `\d{4}-\d{2}-\d{2}` that matches a date in `yyyy-mm-dd` format. We want to add comments to explain each part.

#### Using Free-Spacing Mode in Python

```python
import re

regex_pattern = r'''
    \d{4}  # Year (four digits)
    -      # Separator (hyphen)
    \d{2}  # Month (two digits)
    -      # Separator (hyphen)
    \d{2}  # Day (two digits)
'''

text = "The date is 2024-08-19."
matches = re.findall(regex_pattern, text, re.VERBOSE)
print("Matches:", matches)
```

**Expected Output:**

```
Matches: ['2024-08-19']
```

#### Using Inline Comments

```python
import re

regex_pattern = r'(?#Year)\d{4}-(?#Separator)\d{2}-(?#Day)\d{2}'
text = "The date is 2024-08-19."
matches = re.findall(regex_pattern, text)
print("Matches with inline comments:", matches)
```

**Expected Output:**

```
Matches with inline comments: ['2024-08-19']
```

---

## Problem 2.9

### Insert Literal Text into the Replacement Text

Perform a search-and-replace where any regex match is replaced **literally** with the text `$%\*$1\1`.

#### Correct Replacement Text for Python

```python
replacement_text = r"$%\*$1\\1"
```

#### Python Code Example

```python
import re

text = "This is a test: 123-456."
regex_pattern = r"\d{3}"
replacement_text = r"$%\*$1\\1"

result = re.sub(regex_pattern, replacement_text, text)
print("Result after replacement:", result)
```

**Expected Output:**

```
Result after replacement: This is a test: $%*$1\1123-$%*$1\1456.
```

---

## Problem 3.0

### Insert the Whole Regex Match into Replacement Text

Insert the entire match back into the replacement text, for example, wrapping the match in an `<a>` tag.

#### Python Replacement Example

```python
import re

text = "Visit example.com for more info."
regex_pattern = r"\b\w+\b"
replacement_text = r'<a href="\g<0>">\g<0></a>'

result = re.sub(regex_pattern, replacement_text, text)
print("Result after replacement:", result)
```

**Expected Output:**

```
Result after replacement: <a href="Visit">Visit</a> <a href="example">example</a>.<a href="com">com</a> <a href="for">for</a> <a href="more">more</a> <a href="info">info</a>.
```

---

## Problem 3.1

### Insert Part of the Regex Match into the Replacement Text

Match any contiguous sequence of 10 digits and convert it into the format `(123) 456-7890`.

#### Regular Expression and Replacement Text for Python

```python
import re

text = "My number is 1234567890, please call me!"
regex_pattern = r"\b(\d{3})(\d{3})(\d{4})\b"
replacement_text = r"(\1) \2-\3"

formatted_text = re.sub(regex_pattern, replacement_text, text)
print("Formatted text:", formatted_text)
```

**Expected Output:**

```
Formatted text: My number is (123) 456-7890, please call me!
```

#### Using Named Capturing Groups

```python
import re

text = "My number is 1234567890, please call me!"
regex_pattern = r"\b(?P<area>\d{3})(?P<exchange>\d{3})(?P<number>\d{4})\b"
replacement_text = r"(\g<area>) \g<exchange>-\g<number>"

formatted_text = re.sub(regex_pattern, replacement_text, text)
print("Formatted text with named groups:", formatted_text)
```

**Expected Output:**

```
Formatted text with named groups: My number is (123) 456-7890, please call me!
```

---

## Problem 3.2

### Insert Match Context into the Replacement Text

Replace a regex match with the text **before** the match, followed by the **whole subject text**, and then the text **after** the match. For example, if "Match" is found in "BeforeMatchAfter," the result should be "BeforeBeforeBeforeMatchAfterAfterAfter."

#### Python Code Example

```python
import re

text = "BeforeMatchAfter"
regex_pattern = r"(.*?)(Match)(.*)"

def replacement_function(match):
    left_context = match.group(1)
    matched_text = match.group(2)
    right_context = match.group(3)
    return f"{left_context}{left_context}{matched_text}{right_context}{right_context}"

result = re.sub(regex_pattern, replacement_function, text)
print("Result after replacement:", result)
```

**Expected Output:**

```
Result after replacement: BeforeBeforeBeforeMatchAfterAfterAfter
```
