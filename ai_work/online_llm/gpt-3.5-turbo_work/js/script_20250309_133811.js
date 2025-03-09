```javascript
// Function to generate a random automation tool
function generateAutomationTool() {
    const tools = [
        "Automated regression testing tool",
        "Automated deployment script generator",
        "Automated data migration tool",
        "Automated performance testing script",
        "Automated API testing framework",
        "Automated UI testing tool",
        "Automated error log analyzer",
        "Automated security testing tool"
    ];

    // Generate a random index to select a tool from the array
    const randomIndex = Math.floor(Math.random() * tools.length);

    return tools[randomIndex];
}

// Main function to generate and display a random automation tool
function main() {
    const automationTool = generateAutomationTool();

    console.log("Random Automation Tool Generated:");
    console.log(automationTool);
}

// Call the main function to generate and display a random automation tool
main();
```

**Output:**
```
Random Automation Tool Generated:
Automated regression testing tool
```
```