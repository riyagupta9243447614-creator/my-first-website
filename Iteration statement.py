print("\n=== ITERATION STATEMENTS ===")

# While loop
print("1. While Loop:")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While loop with break
print("\n2. While Loop with break:")
num = 1
while True:
    print(f"Number: {num}")
    num += 1
    if num > 3:
        print("Breaking the loop")
        break

# For loop with range
print("\n3. For Loop with range:")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"i = {i}")

# For loop with list
print("\n4. For Loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with string
print("\n5. For Loop with string:")
word = "Python"
for char in word:
    print(f"Character: {char}")

# Break statement
print("\n6. Break statement:")
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break
    print(f"i = {i}")

# Continue statement
print("\n7. Continue statement:")
for i in range(6):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# Pass statement
print("\n8. Pass statement:")
for i in range(3):
    if i == 1:
        pass  # Do nothing, placeholder
    else:
        print(f"i = {i}")

# Nested loops
print("\n9. Nested loops:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Loop with else
print("\n10. Loop with else:")
for i in range(3):
    print(f"i = {i}")
else:
    print("Loop completed successfully!")

# Practical example: Number guessing game
print("\n11. Practical Example - Number Guessing:")
import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input("Guess a number between 1-10: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry! The number was {secret_number}")

print("\n=== ALL CONCEPTS COMPLETED ===")