```ts
/**
 * TypeScript class to generate random automation tools
 */
class AutomationToolsGenerator {

    // Declare array of available automation tools
    private automationTools: string[] = [
        "Selenium",
        "Puppeteer",
        "Cypress",
        "TestComplete",
        "Tricentis Tosca",
        "Postman",
        "JMeter",
        "Robot Framework",
        "Cucumber",
        "Mabl"
    ];

    /**
     * Function to generate a random automation tool
     * @returns {string} A random automation tool
     */
    public getRandomAutomationTool(): string {
        // Generate a random index within the range of available tools
        let randomIndex = Math.floor(Math.random() * this.automationTools.length);
        // Return the tool at the random index
        return this.automationTools[randomIndex];
    }

    /**
     * Function to generate multiple random automation tools
     * @param {number} count The number of tools to generate
     * @returns {string[]} An array of random automation tools
     */
    public getRandomAutomationTools(count: number): string[] {
        let tools: string[] = [];
        for (let i = 0; i < count; i++) {
            tools.push(this.getRandomAutomationTool());
        }
        return tools;
    }
}

// Instantiate the class
let generator = new AutomationToolsGenerator();

// Generate a single random automation tool
let tool = generator.getRandomAutomationTool();
console.log(`Randomly selected automation tool: ${tool}`);

// Generate multiple random automation tools
let tools = generator.getRandomAutomationTools(5);
console.log("Randomly selected automation tools: ", tools);
```

The above script creates an 'AutomationToolsGenerator' class in TypeScript, which consists of two methods:

1. getRandomAutomationTool(): This method randomly returns one automation tool from the 'automationTools' array.
2. getRandomAutomationTools(count: number): It takes 'count' as an argument and returns that many number of random automation tools from the 'automationTools' array.

At the end, we instantiate the class and use it to generate random automation tools and print them to the console.