```js
// Class for AutomationTools with additional functionalities

class AutomationTools {
    constructor() {
        this.automationTools = [
            'Selenium WebDriver',
            'Appium',
            'Postman',
            'Jenkins',
            'Robot Framework',
            'Cypress',
            'TestNG',
            'Protractor',
            'Katalon Studio',
            'SoapUI'
        ];
    }

    // Function to generate a random automation tool
    generateAutomationTool() {
        const randomIndex = Math.floor(Math.random() * this.automationTools.length);
        return this.automationTools[randomIndex];
    }

    // Function to display the randomly generated automation tool
    displayRandomAutomationTool() {
        console.log('Random Automation Tool: ' + this.generateAutomationTool());
    }

    // Function to add a new automation tool to the list
    addAutomationTool(tool) {
        this.automationTools.push(tool);
    }

    // Function to display all automation tools in the list
    displayAllAutomationTools() {
        console.log('All Automation Tools:');
        this.automationTools.forEach(tool => {
            console.log(tool);
        });
    }
}

// Create an instance of AutomationTools class
const tools = new AutomationTools();

// Generate and display a random automation tool
tools.displayRandomAutomationTool();

// Add a new tool and display all tools
tools.addAutomationTool('Nightwatch');
tools.displayAllAutomationTools();
```

Output:
```
Random Automation Tool: Jenkins
All Automation Tools:
Selenium WebDriver
Appium
Postman
Jenkins
Robot Framework
Cypress
TestNG
Protractor
Katalon Studio
SoapUI
Nightwatch
```