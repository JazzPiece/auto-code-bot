```python
# Import necessary libraries
import random

# Function to generate a random automation tool
def generate_automation_tool():
    tools = ["Automated data backup tool",
             "Automated email sender",
             "Automated report generator",
             "Scheduled task runner",
             "Automated file organizer"]
    
    # Choose a random tool from the list
    random_tool = random.choice(tools)
    
    return random_tool

# Main function to generate and display a random automation tool
def main():
    print("Generating random automation tool...")
    automation_tool = generate_automation_tool()
    print("Random Automation Tool: {}".format(automation_tool))

# Run the main function
if __name__ == "__main__":
    main()
```

**Output:**
```
Generating random automation tool...
Random Automation Tool: Automated report generator
```