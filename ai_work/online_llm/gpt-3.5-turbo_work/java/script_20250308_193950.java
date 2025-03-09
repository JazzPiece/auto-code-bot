```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {"Selenium WebDriver", "Jenkins", "Appium", "Postman", "JIRA"};
        Random random = new Random();
        int index = random.nextInt(tools.length);
        return tools[index];
    }
    
    // Function to check if a specific tool is available
    public static boolean isToolAvailable(String tool) {
        String[] tools = {"Selenium WebDriver", "Jenkins", "Appium", "Postman", "JIRA"};
        for (String availableTool : tools) {
            if (availableTool.equalsIgnoreCase(tool)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        // Generating 5 random automation tools
        for (int i = 1; i <= 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Automation Tool " + i + ": " + tool);
        }
        
        // Checking if a specific tool is available
        String toolToCheck = "Selenium WebDriver";
        if(isToolAvailable(toolToCheck)) {
            System.out.println(toolToCheck + " is available.");
        } else {
            System.out.println(toolToCheck + " is not available.");
        }
    }
}
```