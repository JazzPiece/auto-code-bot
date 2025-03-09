```python
# Import required libraries
import random

# Define a list of automation tools
automation_tools = ['Selenium', 'Puppet', 'Chef', 'Ansible', 'SaltStack', 'Jenkins', 'Docker', 'Kubernetes', 'Nagios', 'Splunk']

def generate_random_tool(tools):
    """
    This function returns a random tool from a given list of tools.
    
    Args:
    tools: List of automation tools
    
    Returns:
    Randomly selected tool
    """
    return random.choice(tools)

def generate_multiple_random_tools(tools, num):
    """
    This function returns a list of unique random tools from a given list.
    
    Args:
    tools: List of automation tools
    num: Number of random tools to be returned
    
    Returns:
    A list of randomly selected, unique tools
    """
    return random.sample(tools, num)

def main():
    """
    Main function, generates a random automation tool
    """
    print("Randomly selected automation tool is: ", generate_random_tool(automation_tools))
    print("Randomly selected multiple distinct automation tools are: ", ', '.join(generate_multiple_random_tools(automation_tools, 3)))

if __name__ == "__main__":
    main()
```

In this improved script, a new function `generate_multiple_random_tools` is added that allows generating multiple unique random tools from the list. The number of unique tools to be generated can be passed as an argument. The main function now also prints these randomly selected distinct tools.