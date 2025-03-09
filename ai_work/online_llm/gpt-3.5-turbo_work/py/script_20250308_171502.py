```python
import random

class AutomationToolGenerator:
    def __init__(self):
        self.tools = [
            "Automated backup tool",
            "Automated testing tool",
            "Automated deployment tool",
            "Automated data validation tool",
            "Automated report generation tool",
            "Automated monitoring tool"  # New tool added
        ]

    def generate_automation_tool(self):
        return random.choice(self.tools)

    def generate_multiple_tools(self, num_tools):
        generated_tools = []
        for i in range(num_tools):
            tool = self.generate_automation_tool()
            generated_tools.append(tool)
        return generated_tools

    def filter_tools_by_keyword(self, keyword):
        filtered_tools = [tool for tool in self.tools if keyword.lower() in tool.lower()]
        return filtered_tools

# Function to check if a tool is a backup tool
def check_backup(tool):
    return "backup" in tool.lower()

def main():
    num_tools = 7  # Increased number of tools to generate
    keyword = "deployment"  # Keyword to filter tools by

    print("Generating {} random automation tools:".format(num_tools))
    
    tool_generator = AutomationToolGenerator()
    generated_tools = tool_generator.generate_multiple_tools(num_tools)
    
    for i, tool in enumerate(generated_tools):
        print("Tool {}: {}".format(i+1, tool))

    filtered_tools = tool_generator.filter_tools_by_keyword(keyword)
    print("\nTools containing the keyword '{}':".format(keyword))
    for i, tool in enumerate(filtered_tools):
        print("Tool {}: {}".format(i+1, tool))

if __name__ == "__main__":
    main()
    
    tool_to_check = "Automated backup tool"
    if check_backup(tool_to_check):
        print(f"\n{tool_to_check} is a backup tool.")
    else:
        print(f"\n{tool_to_check} is not a backup tool.")
```