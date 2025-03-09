```java
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class AutomationToolGenerator {

    private static List<String> availableTools = new ArrayList<>();

    // Function to initialize available tools
    public static void initializeAvailableTools() {
        availableTools.add("Selenium");
        availableTools.add("Appium");
        availableTools.add("Jenkins");
        availableTools.add("Postman");
        availableTools.add("Robot Framework");
        availableTools.add("Cypress");
    }

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        Random random = new Random();
        int index = random.nextInt(availableTools.size());
        return availableTools.get(index);
    }

    // Function to check if a specific tool is available
    public static boolean isToolAvailable(String tool) {
        return availableTools.contains(tool);
    }

    // Function to display all available tools
    public static void displayAllTools() {
        System.out.println("Available Automation Tools:");
        for (String tool : availableTools) {
            System.out.println(tool);
        }
    }

    // Function to get the total number of available tools
    public static int getTotalNumberOfTools() {
        return availableTools.size();
    }

    public static void main(String[] args) {
        // Initialize available tools
        initializeAvailableTools();

        System.out.println("Generating Random Automation Tool:");
        String automationTool = generateAutomationTool();
        System.out.println("Random Automation Tool: " + automationTool);

        // Checking if Selenium is available
        String toolToCheck = "Selenium";
        if (isToolAvailable(toolToCheck)) {
            System.out.println(toolToCheck + " is available.");
        } else {
            System.out.println(toolToCheck + " is not available.");
        }

        // Displaying all available tools
        displayAllTools();

        // Getting the total number of available tools
        System.out.println("Total number of available tools: " + getTotalNumberOfTools());
    }
}
```