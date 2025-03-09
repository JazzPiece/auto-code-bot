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

// Generate a random automation tool
const randomTool = generateAutomationTool();

// Output the randomly generated automation tool
console.log("Random Automation Tool: " + randomTool);
```

**Output:**
Random Automation Tool: Automated testing tool
```

This script defines a function `generateAutomationTool` that generates a random automation tool from a predefined array of tools. It then generates a random index and selects a tool based on that index. Finally, it outputs the randomly generated automation tool.