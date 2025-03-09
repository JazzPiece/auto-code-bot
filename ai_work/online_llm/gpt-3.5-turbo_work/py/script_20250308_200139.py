```python
import random

# Function to generate random automation tools for different tasks
def generate_automation_tool():
    tools = [
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
    
    # Choose a random automation tool from the list
    random_tool = random.choice(tools)
    
    return random_tool

# Main function to run the script
def main():
    print("Generating random automation tools:")
    for i in range(5):
        automation_tool = generate_automation_tool()
        print(f"{i+1}. {automation_tool}")
        
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
```