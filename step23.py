import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Step 15: Declare password variable with empty string
    password = ""

    # Step 18: Modified to use underscore since the iteration variable is not used
    for _ in range(length):
        password += secrets.choice(all_characters)

    # Display the final password
    print(f"Your generated password is: {password}")
    
    # Step 19: Return the password variable
    return password

# new_password = generate_password(8)
# print(new_password)