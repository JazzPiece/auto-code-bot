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

# Function to check if a tool is essential or not
def check_tool_essential(tool):
    essential_tools = ["Backup Scheduler", "Password Generator", "Code Formatter", "Email Sender"]
    
    if tool in essential_tools:
        return "Essential Tool"
    else:
        return "Optional Tool"

# Main function to run the script
def main():
    print("Welcome to the Random Automation Tool Generator!")
    
    # Generate 5 random automation tools
    for i in range(5):
        tool = generate_automation_tool()
        tool_category = check_tool_essential(tool)
        print(f"Automation Tool {i+1}: {tool} - {tool_category}")
    
if __name__ == "__main__":
    main()
```

Output:
```
Welcome to the Random Automation Tool Generator!
Automation Tool 1: Backup Scheduler - Essential Tool
Automation Tool 2: Data Scraper - Optional Tool
Automation Tool 3: Code Formatter - Essential Tool
Automation Tool 4: Password Generator - Essential Tool
Automation Tool 5: File Renamer - Optional Tool
``` 

In this improved script, a new function `check_tool_essential` is added to determine if a generated tool is essential or optional. The function categorizes tools based on a predefined list of essential tools. The category of each tool is displayed alongside the name when generating the random automation tools. This extra feature provides more information about the generated tools, helping users identify essential tools easily.