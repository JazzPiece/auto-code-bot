```javascript
/**
 * Function to generate a random automation tool
 * @returns {string} Random automation tool
 */
function generateRandomAutomationTool() {
    const automationTools = [
        "Selenium WebDriver",
        "Appium",
        "Katalon Studio",
        "Cypress",
        "Postman",
        "Jenkins",
        "Robot Framework",
        "TestProject",
        "SoapUI",
        "XCUITest"
    ];

    // Generate a random index to select a random automation tool
    const randomIndex = Math.floor(Math.random() * automationTools.length);

    return automationTools[randomIndex];
}

/**
 * Function to check if a given automation tool is included in the list
 * @param {string} tool - Automation tool to check
 * @returns {boolean} true if the tool is included, false otherwise
 */
function checkIfToolIncluded(tool) {
    const automationTools = [
        "Selenium WebDriver",
        "Appium",
        "Katalon Studio",
        "Cypress",
        "Postman",
        "Jenkins",
        "Robot Framework",
        "TestProject",
        "SoapUI",
        "XCUITest"
    ];

    return automationTools.includes(tool);
}

/**
 * Function to get all automation tools in the list
 * @returns {Array} List of automation tools
 */
function getAllAutomationTools() {
    return [
        "Selenium WebDriver",
        "Appium",
        "Katalon Studio",
        "Cypress",
        "Postman",
        "Jenkins",
        "Robot Framework",
        "TestProject",
        "SoapUI",
        "XCUITest"
    ];
}

// Generate a random automation tool
const randomAutomationTool = generateRandomAutomationTool();

// Output the randomly generated automation tool
console.log("Random Automation Tool: " + randomAutomationTool);

// Check if a specific tool is included in the list
const toolToCheck = "Selenium WebDriver";
const isToolIncluded = checkIfToolIncluded(toolToCheck);

// Output the result of checking if the tool is included
console.log(`Is ${toolToCheck} included in the list? ${isToolIncluded}`);

// Get all automation tools in the list
const allTools = getAllAutomationTools();

// Output all automation tools
console.log("All Automation Tools:");
allTools.forEach(tool => console.log(tool));
```