import secrets
import string

def generate_password(length=16, include_uppercase=True, include_lowercase=True,
                      include_numbers=True, include_special_chars=True):
    # Define character sets based on user requirements
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    # Generate a secure random password using secrets.choice
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

# Generate a new password with default settings
new_password = generate_password()

# Print the new password
print("This is your new password: " + new_password)
