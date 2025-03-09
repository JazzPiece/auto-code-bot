```python
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = ["Automated Data Scraping Tool", "Automated Email Sender", "Automated File Renamer", "Automated Image Resizer"]
    return random.choice(tools)

# Main function to generate and display automation tools
def main():
    num_tools = 5  # Number of tools to generate

    print("Random Useful Automation Tools:")
    for _ in range(num_tools):
        tool = generate_automation_tool()
        print(tool)

if __name__ == "__main__":
    main()
```

**Output:**
```
Random Useful Automation Tools:
Automated Email Sender
Automated File Renamer
Automated Data Scraping Tool
Automated Image Resizer
Automated Email Sender
```