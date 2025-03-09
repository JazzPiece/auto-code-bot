```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "Robot Framework", "Katalon Studio"};
        Random rand = new Random();
        int index = rand.nextInt(tools.length);
        return tools[index];
    }

    // Function to check if a specific tool is available
    public static boolean isToolAvailable(String toolName) {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "Robot Framework", "Katalon Studio"};
        for (String tool : tools) {
            if (tool.equalsIgnoreCase(toolName)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Generating random automation tools:");

        // Generate 5 random automation tools
        for (int i = 1; i <= 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Tool " + i + ": " + tool);
        }

        // Check if a specific tool is available
        String toolToCheck = "Selenium";
        if(isToolAvailable(toolToCheck)) {
            System.out.println(toolToCheck + " is available.");
        } else {
            System.out.println(toolToCheck + " is not available.");
        }
    }
}
``` 

Improved script:
- Added a new function `isToolAvailable(String toolName)` that checks if a specific tool is available in the list of tools.
- In the main method, after generating random automation tools, it checks if "Selenium" tool is available using the new function `isToolAvailable()`.