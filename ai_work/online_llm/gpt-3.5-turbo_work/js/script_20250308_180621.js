```js
// Function to generate a random automation tool
function generateAutomationTool() {
    // List of automation tools
    const tools = [
        "Automated Testing Framework",
        "Web Scraping Bot",
        "Automated Email Sender",
        "Batch Image Resizer",
        "Data Backup Automation Tool"
    ];

    // Generate a random index
    const randomIndex = Math.floor(Math.random() * tools.length);

    // Return the random automation tool
    return tools[randomIndex];
}

// Function to check if a tool is available in the list of automation tools
function checkToolAvailability(toolName) {
    // List of automation tools
    const tools = [
        "Automated Testing Framework",
        "Web Scraping Bot",
        "Automated Email Sender",
        "Batch Image Resizer",
        "Data Backup Automation Tool"
    ];

    // Check if the tool exists in the list
    if (tools.includes(toolName)) {
        return `The tool "${toolName}" is available in the list of automation tools.`;
    } else {
        return `The tool "${toolName}" is not available in the list of automation tools.`;
    }
}

// Generate a random automation tool
const randomAutomationTool = generateAutomationTool();

// Output the random automation tool
console.log("Random Automation Tool Generated: " + randomAutomationTool);

// Check if a specific tool is available in the list
const toolToCheck = "Web Scraping Bot";
console.log(checkToolAvailability(toolToCheck));
```

**Sample Output:**
```
Random Automation Tool Generated: Batch Image Resizer
The tool "Web Scraping Bot" is available in the list of automation tools.
``` 

In this improved script, a new function `checkToolAvailability` is added to check if a specific tool is available in the list of automation tools. The function provides a message indicating whether the tool is available in the list or not. A sample output is provided for demonstration.