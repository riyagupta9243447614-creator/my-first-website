# Boolean Values and Operators

# Boolean Values
true_value = True
false_value = False
print(f"True: {true_value}, False: {false_value}")

# Comparison Operators
a, b = 10, 5
print(f"a > b: {a > b}")    # Greater than
print(f"a < b: {a < b}")    # Less than  
print(f"a == b: {a == b}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print(f"a >= b: {a >= b}")  # Greater than or equal
print(f"a <= b: {a <= b}")  # Less than or equal

# Logical Operators
x, y = True, False
print(f"x and y: {x and y}")  # AND - Both must be True
print(f"x or y: {x or y}")    # OR - At least one True
print(f"not x: {not x}")      # NOT - Reverse the value

# Real-world examples
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

# Boolean with strings
name = "John"
is_john = name == "John"
print(f"Is name John: {is_john}")