import secrets
import string

def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate password characters
    password_list = []
    
    for char in range(length):
        password_list.append(secrets.choice(all_characters))
    
    # Convert list to string
    password = ''.join(password_list)

    # Display the final password
    print(f"Your generated password is: {password}")
    
    # Step 15: Declare password variable with empty string at the bottom
    password = ""