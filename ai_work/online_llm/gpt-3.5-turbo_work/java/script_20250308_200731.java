```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {"Selenium", "Appium", "Postman", "Jenkins", "Robot Framework"};
        Random rand = new Random();
        int index = rand.nextInt(tools.length);
        return tools[index];
    }

    // Function to check if the generated automation tool is for web or mobile
    public static String getToolType(String tool) {
        if (tool.equals("Selenium") || tool.equals("Robot Framework")) {
            return "Web Automation Tool";
        } else if (tool.equals("Appium")) {
            return "Mobile Automation Tool";
        } else {
            return "Other Automation Tool";
        }
    }

    public static void main(String[] args) {
        // Generate a random automation tool
        String automationTool = generateAutomationTool();
        
        // Output the generated automation tool
        System.out.println("Random Automation Tool Generated: " + automationTool);

        // Check the type of automation tool generated
        String toolType = getToolType(automationTool);
        System.out.println("Automation Tool Type: " + toolType);
    }
}
```

Output:
```
Random Automation Tool Generated: Selenium
Automation Tool Type: Web Automation Tool
```