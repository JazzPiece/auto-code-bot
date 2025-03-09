```javascript
// Function to generate a random automation tool
function generateAutomationTool() {
    const tools = [
        "Automated testing tool",
        "Task scheduling tool",
        "Data scraping tool",
        "Automated deployment tool",
        "Monitoring tool",
        "Code generation tool",
        "Notification tool"
    ];

    // Generate a random index to select a tool from the array
    const randomIndex = Math.floor(Math.random() * tools.length);

    return tools[randomIndex];
}

// Function to check if a specific tool is included in the array
function checkIfToolExists(toolName) {
    const tools = [
        "Automated testing tool",
        "Task scheduling tool",
        "Data scraping tool",
        "Automated deployment tool",
        "Monitoring tool",
        "Code generation tool",
        "Notification tool"
    ];

    return tools.includes(toolName);
}

// Generate a random automation tool
const randomTool = generateAutomationTool();

// Output the randomly generated automation tool
console.log("Random Automation Tool: " + randomTool);

// Check if a specific tool exists in the array
const specificTool = "Monitoring tool";
const toolExists = checkIfToolExists(specificTool);

if (toolExists) {
    console.log(`${specificTool} is included in the list of automation tools.`);
} else {
    console.log(`${specificTool} is not included in the list of automation tools.`);
}
```

**Output:**
Random Automation Tool: Automated testing tool
Monitoring tool is included in the list of automation tools.
``` 

In the improved script, I have added a new function called `checkIfToolExists` that checks if a specific tool is included in the array of automation tools. This function utilizes the `includes()` method to determine if the tool exists.

I've also included an example in the script to demonstrate how the `checkIfToolExists` function can be used to check if a specific tool ("Monitoring tool" in this case) exists in the list of automation tools.