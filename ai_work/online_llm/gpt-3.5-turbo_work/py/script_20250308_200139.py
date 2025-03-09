```python
import random

class AutomationToolGenerator:
    def __init__(self):
        self.tools = [
            "Automated data backup tool",
            "Automated report generation tool",
            "Automated file renaming tool",
            "Automated email scheduler",
            "Automated website testing tool",
            "Automated image resizing tool",
            "Automated social media posting tool",
            "Automated data cleaning tool",
            "Automated task scheduler",
            "Automated error log analysis tool"
        ]
    
    def generate_automation_tool(self):
        # Choose a random automation tool from the list
        random_tool = random.choice(self.tools)
        return random_tool
    
    def generate_specific_tool(self, tool_name):
        # Check if the specified tool name is in the list, otherwise return None
        if tool_name in self.tools:
            return tool_name
        else:
            return None

def main():
    automation_tool_generator = AutomationToolGenerator()
    
    print("Generating random automation tools:")
    for i in range(5):
        automation_tool = automation_tool_generator.generate_automation_tool()
        print(f"{i + 1}. {automation_tool}")
    
    # Generate a specific tool
    specific_tool = "Automated report generation tool"
    selected_tool = automation_tool_generator.generate_specific_tool(specific_tool)
    if selected_tool:
        print(f"Generating specific tool: {selected_tool}")
    else:
        print(f"Specified tool '{specific_tool}' not found in the list.")

if __name__ == "__main__":
    main()
```

Output:
```
Generating random automation tools:
1. Automated email scheduler
2. Automated report generation tool
3. Automated file renaming tool
4. Automated data backup tool
5. Automated social media posting tool
Generating specific tool: Automated report generation tool
``` 

In this improved script, a class `AutomationToolGenerator` is introduced to handle automation tool generation. The class contains methods to generate a random automation tool, check for a specific tool in the list, and return the tool if found. The `main` function demonstrates generating random automation tools and showcasing the generation of a specific tool using the new functionality.