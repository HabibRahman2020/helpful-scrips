import secrets
import string

def gen_password(length=16, include_uppercase=True, include_lowercase=True, include_numbers=True, include_special=True):

    Generate a random password of the specified length with customizable character sets.

    Parameters:
    - length (int): Length of the password (default: 16)
    - include_uppercase (bool): Include uppercase letters (default: True)
    - include_lowercase (bool): Include lowercase letters (default: True)
    - include_numbers (bool): Include numbers (default: True)
    - include_special (bool): Include special characters (default: True)

    Returns:
    - password (str): Generated password
       
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer")
    
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

password = secrets.token_urlsafe(16)
print("This is your new password:", password)
