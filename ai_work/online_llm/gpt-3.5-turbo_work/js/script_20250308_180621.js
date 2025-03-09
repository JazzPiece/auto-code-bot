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

// Generate a random automation tool
const randomAutomationTool = generateAutomationTool();

// Output the random automation tool
console.log("Random Automation Tool Generated: " + randomAutomationTool);
```

**Sample Output:**
```
Random Automation Tool Generated: Batch Image Resizer
```