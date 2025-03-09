```python
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = ["Automated screenshot taker", "File organizer by type", "Automated email sender", "Code deployment tool", "Automated data backup system"]
    return random.choice(tools)

# Function to provide a brief description of the generated automation tool
def tool_description(tool_name):
    descriptions = {
        "Automated screenshot taker": "Automatically captures screenshots at regular intervals.",
        "File organizer by type": "Organizes files into folders based on their types.",
        "Automated email sender": "Sends pre-written emails automatically.",
        "Code deployment tool": "Automates the deployment process of code to servers.",
        "Automated data backup system": "Automatically backs up data to secure storage."
    }
    return descriptions.get(tool_name, "No description available.")

# Main function to generate, print a random automation tool, and its description
def main():
    automation_tool = generate_automation_tool()
    print("Random Automation Tool Generated:")
    print(automation_tool)
    print("\nDescription:")
    print(tool_description(automation_tool))

if __name__ == "__main__":
    main()
```

**Output:**
```
Random Automation Tool Generated:
File organizer by type

Description:
Organizes files into folders based on their types.
``` 

In the improved script, I added a new function `tool_description` that provides a brief description of the generated automation tool. This enhances the functionality by giving more information about the randomly selected tool.