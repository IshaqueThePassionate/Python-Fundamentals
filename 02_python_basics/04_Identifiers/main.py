# Valid Identifiers

student_name = "John Doe"  # Variable with lowercase and underscore
StudentName = "Alice"  # Variable with PascalCase
studentAge = 20  # CamelCase variable
_studentID = 1001  # Private variable with a leading underscore
PI = 3.14159  # Constant variable (conventionally in uppercase)



# Invalid Identifiers

# 1student = "Invalid"  # Cannot start with a digit
# student-name = "Invalid"  # Cannot contain hyphens
# student@id = 101  # Cannot contain special characters



# Using Unicode Identifiers (Python 3+)

नाम = "राम"  # Hindi Unicode variable
رقم = 500  # Arabic Unicode variable
結果 = 98  # Chinese Unicode variable

print(नाम, رقم, 結果)



# Private and Strongly Private Identifiers

class User:
    def __init__(self, username):
        self._internal_value = 42  # Private variable (single underscore)
        self.__secure_data = "Hidden"  # Strongly private variable (double underscores)

user1 = User("admin")
# print(user1.__secure_data)  # This will raise an AttributeError due to name mangling



# Special Use of Underscore in Interactive Mode

# >>> 100 + 25
# 125
# >>> _ * 2
# 250  # The underscore holds the last evaluated expression
