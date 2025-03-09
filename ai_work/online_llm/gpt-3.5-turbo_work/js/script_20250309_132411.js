```js
// Function to generate a random automation tool
function generateAutomationTool() {
    const tools = [
        "Automated testing tool",
        "CI/CD pipeline setup tool",
        "Automated deployment tool",
        "Task scheduler for automating repetitive tasks",
        "Automated data backup tool",
        "Automation script generator",
        "Automated report generator",
        "Automated monitoring and alerting tool"
    ];

    const randomIndex = Math.floor(Math.random() * tools.length);
    return tools[randomIndex];
}

// Generate and display a random automation tool
const randomAutomationTool = generateAutomationTool();
console.log("Random Automation Tool: " + randomAutomationTool);
```

**Output:**
```
Random Automation Tool: Automated testing tool
```
In this script, a function `generateAutomationTool` is defined to generate a random useful automation tool from a predefined list. The function selects a random index from the list of tools and returns the corresponding tool. Finally, the script outputs the randomly generated automation tool.