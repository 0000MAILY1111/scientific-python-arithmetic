import secrets
import string

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

        print(f"Your generated password is: {password}")
        
        return password

# new_password = generate_password(8)
# print(new_password)