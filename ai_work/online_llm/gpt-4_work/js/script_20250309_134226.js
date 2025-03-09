```javascript
// This script generates different types of useful automation tools
// We use an array to store different types of automation tools
// Each time script runs, it generates a random tool from the array
// Added functionality: The script now also generates a brief description for the chosen tool

// Automation tools list with descriptions
const automationTools = [
    {tool: 'Script Runner', description: 'Automate and control the execution of your scripts.'},
    {tool: 'File Organizer', description: 'Keep your files neatly categorized and easy to find.'},
    {tool: 'Task Scheduler', description: 'Schedule tasks to run automatically at specified times.'},
    {tool: 'Auto Email Sender', description: 'Send emails without any manual intervention.'},
    {tool: 'Web Scraper', description: 'Extract data from websites in a format suitable for analysis.'},
    {tool: 'Data Extractor', description: 'Pull data from any source in a structured format.'},
    {tool: 'Social Media Poster', description: 'Automatically post updates on your social media platforms.'},
    {tool: 'Database Manager', description: 'Manage and control access to your database.'},
    {tool: 'Code Cleaner', description: 'Optimize your code by removing unnecessary elements.'},
    {tool: 'Bulk Image Downloader', description: 'Download multiple images from a source at once.'}
];

// Function to pick a random tool from the array
function generateRandomTool() {
    // Generate a random index
    let randomIndex = Math.floor(Math.random() * automationTools.length);
    return automationTools[randomIndex];
}

// Generate and log a random automation tool with description
let generatedTool = generateRandomTool();
console.log(`Your randomly generated automation tool for today is: ${generatedTool.tool}.`);
console.log(`Description: ${generatedTool.description}`);
```

Full Script Output:

The output of the script cannot be determined beforehand as it depends on the random selection of the automation tool and its associated description. However, it will be in the following format: 

`Your randomly generated automation tool for today is: [Automation Tool Name]`
`Description: [Tool Description]`

For example:

`Your randomly generated automation tool for today is: Web Scraper`
`Description: Extract data from websites in a format suitable for analysis.`