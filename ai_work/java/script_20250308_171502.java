```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "Robot Framework", "Cypress"};

        Random random = new Random();
        int index = random.nextInt(tools.length);

        return tools[index];
    }

    // Function to check if a specific tool is available
    public static boolean isToolAvailable(String tool) {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "Robot Framework", "Cypress"};

        for(String availableTool : tools) {
            if(availableTool.equalsIgnoreCase(tool)) {
                return true;
            }
        }

        return false;
    }

    // Function to display all available tools
    public static void displayAllTools() {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "Robot Framework", "Cypress"};
        
        System.out.println("Available Automation Tools:");
        for(String tool : tools) {
            System.out.println(tool);
        }
    }

    public static void main(String[] args) {
        System.out.println("Generating Random Automation Tool:");
        String automationTool = generateAutomationTool();
        System.out.println("Random Automation Tool: " + automationTool);

        // Checking if Selenium is available
        String toolToCheck = "Selenium";
        if(isToolAvailable(toolToCheck)) {
            System.out.println(toolToCheck + " is available.");
        } else {
            System.out.println(toolToCheck + " is not available.");
        }

        // Displaying all available tools
        displayAllTools();
    }
}
```