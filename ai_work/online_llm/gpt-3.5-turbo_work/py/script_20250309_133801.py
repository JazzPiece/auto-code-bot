```python
import random

# Function to generate a random password
def generate_password():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    password = ''.join(random.choices(characters, k=12))
    return password

# Function to generate a random email address
def generate_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
    domain = random.choice(domains)
    email = f'{username}@{domain}'
    return email

# Function to generate a random phone number
def generate_phone_number():
    phone_number = '+1-555-' + ''.join(random.choices('0123456789', k=8))
    return phone_number

# Main function to generate random automation tools
def generate_automation_tools():
    password = generate_password()
    email = generate_email()
    phone_number = generate_phone_number()

    automation_tool = {
        "password": password,
        "email": email,
        "phone_number": phone_number
    }

    return automation_tool

# Generate automation tools
automation_tools = generate_automation_tools()

# Output
print("Random Automation Tools Generated:")
print(f"Password: {automation_tools['password']}")
print(f"Email: {automation_tools['email']}")
print(f"Phone Number: {automation_tools['phone_number']}")

```

**Output:**
```
Random Automation Tools Generated:
Password: bQ7Y#8!DxJW6
Email: zrpyfzhu@outlook.com
Phone Number: +1-555-42678433
```