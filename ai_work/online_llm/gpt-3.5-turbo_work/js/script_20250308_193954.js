/**
 * Function to generate a random automation tool
 */
function generateRandomTool() {
    const tools = [
        "Automated Test Framework",
        "Data Scraping Tool",
        "Batch File Renamer",
        "Automated Deployment Script",
        "Log File Analyzer"
    ];

    // Generate a random index to select a tool from the array
    const randomIndex = Math.floor(Math.random() * tools.length);

    return tools[randomIndex];
}

// Generate a random automation tool
const randomTool = generateRandomTool();

console.log("Random Automation Tool Generated: " + randomTool);