import secrets
import string
import re  # Step 27: Import the re module for regular expressions

def generate_password(length, nums, special_chars, uppercase, lowercase):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    while True:
        password = ""

        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, "")
        ]

        if all(re.search(pattern, password) for pattern in constraints):
            return password

        return password

# new_password = generate_password(8)
# print(new_password)