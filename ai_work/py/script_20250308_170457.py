```python
import random

# Function to generate a random useful automation tool
def generate_random_tool():
    """
    This function generates a random useful automation tool.

    Returns:
    tool (str): A string representing the randomly generated tool.
    """
    tools = ["Automated screenshot taker", "File organizer", "Automated email sender", "Code snippet generator",
             "Automated data backup tool", "Website monitoring tool", "Text substitution tool"]

    tool = random.choice(tools)
    return tool

# Function to provide a description of the generated tool
def describe_tool(tool):
    """
    This function provides a brief description of the generated tool.

    Parameters:
    tool (str): The name of the generated tool.
    """
    descriptions = {
        "Automated screenshot taker": "Tool that captures screenshots automatically at specified intervals.",
        "File organizer": "Tool that organizes files and folders based on user-defined rules.",
        "Automated email sender": "Tool that sends pre-written emails automatically to specified recipients.",
        "Code snippet generator": "Tool that generates code snippets for common programming tasks.",
        "Automated data backup tool": "Tool that automatically backs up important data to a secure location.",
        "Website monitoring tool": "Tool that monitors websites for uptime and performance.",
        "Text substitution tool": "Tool that replaces specified text patterns in files or documents."
    }

    if tool in descriptions:
        print("Description of", tool + ":", descriptions[tool])
    else:
        print("No description available for", tool)

# Main function to generate and describe a random tool
def main():
    """
    This is the main function that generates and displays a random useful automation tool along with its description.
    """
    tool = generate_random_tool()
    print("Randomly generated useful automation tool:", tool)
    describe_tool(tool)

if __name__ == "__main__":
    main()
```

**Output:**
```
Randomly generated useful automation tool: Automated screenshot taker
Description of Automated screenshot taker: Tool that captures screenshots automatically at specified intervals.
``` 

In the improved script, a new function `describe_tool` has been added to provide descriptions of the generated tools. This enhances the script by providing additional information about the usefulness of the randomly generated automation tool.