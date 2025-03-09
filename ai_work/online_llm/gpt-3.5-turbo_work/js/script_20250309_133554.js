// Function to generate a random automation tool
function generateAutomationTool() {
    const tools = [
        "Automated testing tool",
        "File organization tool",
        "Code deployment tool",
        "Data scraping tool",
        "Automated report generation tool",
        "Code formatting tool"
    ];

    const randomIndex = Math.floor(Math.random() * tools.length);
    return tools[randomIndex];
}

// Generate a random automation tool
const automationTool = generateAutomationTool();

// Output the randomly generated automation tool
console.log(`Random Automation Tool: ${automationTool}`);

// Sample Output:
// Random Automation Tool: Automated testing tool