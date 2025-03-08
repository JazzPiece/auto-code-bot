```python
import random

def generate_password(length=12):
    """
    Generate a random password of given length.

    Parameters:
    length (int): Length of the password (default is 12)

    Returns:
    str: Random password
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_username(length=8):
    """
    Generate a random username of given length.

    Parameters:
    length (int): Length of the username (default is 8)

    Returns:
    str: Random username
    """
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890'
    username = ''.join(random.choice(characters) for _ in range(length))
    return username

def generate_email():
    """
    Generate a random email address.

    Returns:
    str: Random email address
    """
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']
    username = generate_username()
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email

def main():
    """
    Main function to execute the script.
    Print random automation tools like password, username, and email.
    """
    print("Random Automation Tools Generator\n")
    print("1. Random Password:", generate_password())
    print("2. Random Username:", generate_username())
    print("3. Random Email Address:", generate_email())

if __name__ == "__main__":
    main()
```