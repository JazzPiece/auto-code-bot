```python
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = [
        "Automated data backup tool",
        "Automated report generation tool",
        "Automated email sender",
        "Automated file synchronization tool",
        "Automated image processing tool",
        "Automated website testing tool"
    ]

    return random.choice(tools)

# Main function to generate and display a random automation tool
def main():
    print("Generating a random automation tool...")
    automation_tool = generate_automation_tool()
    print("Random Automation Tool: ", automation_tool)

if __name__ == "__main__":
    main()
```

Output:
```
Generating a random automation tool...
Random Automation Tool:  Automated data backup tool
```