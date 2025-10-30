print("\n=== CONDITIONAL STATEMENTS ===")

# Simple if statement
print("1. Simple if statement:")
number = 15
if number > 10:
    print(f"{number} is greater than 10")

# if-else statement
print("\n2. if-else statement:")
age = 16
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# if-elif-else statement
print("\n3. if-elif-else statement:")
score = 85

if score >= 90:
    grade = 'A'
    print("Excellent!")
elif score >= 80:
    grade = 'B'
    print("Good job!")
elif score >= 70:
    grade = 'C'
    print("Fair")
elif score >= 60:
    grade = 'D'
    print("Needs improvement")
else:
    grade = 'F'
    print("Failed")

print(f"Score: {score}, Grade: {grade}")

# Nested if statements
print("\n4. Nested if statements:")
temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Perfect weather for a picnic!")
    else:
        print("Warm but cloudy")
else:
    print("It's quite cold")

# Multiple conditions
print("\n5. Multiple conditions:")
number = 15
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5")
elif number % 3 == 0:
    print(f"{number} is divisible by 3")
elif number % 5 == 0:
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 3 or 5")