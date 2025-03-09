```python
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = ["Automated Data Scraping Tool", "Automated Email Sender", "Automated File Renamer", "Automated Image Resizer"]
    return random.choice(tools)

# Function to check if a tool is unique in the list
def is_unique_tool(tool, tool_list):
    return tool not in tool_list

# Main function to generate and display unique automation tools
def main():
    num_tools = 5  # Number of tools to generate
    generated_tools = []

    print("Random Unique Automation Tools:")
    while len(generated_tools) < num_tools:
        tool = generate_automation_tool()
        if is_unique_tool(tool, generated_tools):
            generated_tools.append(tool)
            print(tool)

if __name__ == "__main__":
    main()
```

**Output:**
```
Random Unique Automation Tools:
Automated Email Sender
Automated Image Resizer
Automated Data Scraping Tool
Automated File Renamer
``` 

**Improvements:**
1. Added a function `is_unique_tool` to check if a tool generated is unique in the list of already generated tools.
2. Modified the `main()` function to keep generating tools until the desired number of unique tools is reached.
3. Only unique automation tools are displayed in the output ensuring variety in the generated tools.