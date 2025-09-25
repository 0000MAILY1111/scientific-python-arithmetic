import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password_list = []
    
    for char in range(length):
        password_list.append(random.choice(letters))
    
    random.shuffle(password_list)

    password = ''.join(password_list)

    print(f"Your generated password is: {password}")