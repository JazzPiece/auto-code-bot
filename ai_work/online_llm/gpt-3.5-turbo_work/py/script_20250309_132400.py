```python
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = [
        "Automated File Renamer",
        "Automated Data Backup Tool",
        "Automated Email Scheduler",
        "Automated Password Manager",
        "Automated Image Resizer",
        "Automated Website Monitor",
        "Automated Code Formatter",
        "Automated Task Scheduler"
    ]
    return random.choice(tools)

# Main function to generate and display a random automation tool
def main():
    print("Generating Random Automation Tool:")
    automation_tool = generate_automation_tool()
    print(automation_tool)

if __name__ == "__main__":
    main()
```

**Script Output:**
```
Generating Random Automation Tool:
Automated Image Resizer
```