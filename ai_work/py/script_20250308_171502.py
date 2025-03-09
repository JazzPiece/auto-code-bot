```python
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = [
        "Automated backup tool",
        "Automated testing tool",
        "Automated deployment tool",
        "Automated data validation tool",
        "Automated report generation tool",
        "Automated monitoring tool"  # New tool added
    ]
    return random.choice(tools)

# Main function to generate and display automation tools
def main():
    num_tools = 6  # Increased number of tools to generate
    print("Generating {} random automation tools:".format(num_tools))
    for i in range(num_tools):
        tool = generate_automation_tool()
        print("Tool {}: {}".format(i+1, tool))

# Function to check if a tool is a backup tool
def check_backup(tool):
    return "backup" in tool.lower()

if __name__ == "__main__":
    main()
    tool_to_check = "Automated backup tool"
    if check_backup(tool_to_check):
        print(f"\n{tool_to_check} is a backup tool.")
    else:
        print(f"\n{tool_to_check} is not a backup tool.")
```

**Output:**
```
Generating 6 random automation tools:
Tool 1: Automated report generation tool
Tool 2: Automated backup tool
Tool 3: Automated data validation tool
Tool 4: Automated monitoring tool
Tool 5: Automated testing tool
Tool 6: Automated backup tool

Automated backup tool is a backup tool.
```