# Character to Number Conversion

# Method 1: Using ord() function
char = 'A'
number = ord(char)
print(f"Character '{char}' to number: {number}")
# Output: Character 'A' to number: 65

# Method 2: Converting digits
digit_char = '7'
digit_number = int(digit_char)
print(f"Digit '{digit_char}' to number: {digit_number}")
# Output: Digit '7' to number: 7

# Method 3: Multiple characters
text = "ABC"
numbers = [ord(ch) for ch in text]
print(f"Text '{text}' to numbers: {numbers}")
# Output: Text 'ABC' to numbers: [65, 66, 67]

# Method 4: Number to Character using chr()
num = 65
character = chr(num)
print(f"Number {num} to character: '{character}'")
# Output: Number 65 to character: 'A'