import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters to meet general security rules.")

    # Characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password meets the general rules
    password = [
        random.choice(string.ascii_uppercase),  # at least one uppercase letter
        random.choice(string.ascii_lowercase),  # at least one lowercase letter
        random.choice(string.digits),           # at least one digit
        random.choice(string.punctuation)       # at least one special character
    ]

    # Fill the rest of the password length with random characters
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the password list to avoid predictable sequences
    random.shuffle(password)

    return ''.join(password)

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate and display the password
try:
    password = generate_password(length)
    print("Generated password:", password)
except ValueError as ve:
    print(ve)
