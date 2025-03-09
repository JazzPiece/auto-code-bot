// Function to generate a random automation tool
function generateAutomationTool() {
    const tools = [
        "Automated test script generator",
        "Automated screenshot capture tool",
        "Automated data migration tool",
        "Automated report generation tool",
        "Automated backup and restore tool"
    ];

    // Generate a random index to select a tool from the array
    const randomIndex = Math.floor(Math.random() * tools.length);

    return tools[randomIndex];
}

// Main function to run the script
function main() {
    const randomTool = generateAutomationTool();

    console.log("Random Automation Tool Generated:");
    console.log(randomTool);
}

// Execute the main function
main();