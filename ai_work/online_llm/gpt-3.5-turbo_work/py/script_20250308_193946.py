```python
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = [
        "AutoClicker",
        "Screenshot Generator",
        "Data Scraper",
        "Text-to-Speech Converter",
        "File Renamer",
        "Backup Scheduler",
        "Password Generator",
        "Code Formatter",
        "Email Sender",
        "File Organizer"
    ]
    
    # Select a random tool from the list
    random_tool = random.choice(tools)
    
    return random_tool

# Main function to run the script
def main():
    print("Welcome to the Random Automation Tool Generator!")
    
    # Generate 5 random automation tools
    for i in range(5):
        tool = generate_automation_tool()
        print(f"Automation Tool {i+1}: {tool}")
    
if __name__ == "__main__":
    main()
```

Output:
```
Welcome to the Random Automation Tool Generator!
Automation Tool 1: Backup Scheduler
Automation Tool 2: Data Scraper
Automation Tool 3: Code Formatter
Automation Tool 4: Password Generator
Automation Tool 5: File Renamer
```