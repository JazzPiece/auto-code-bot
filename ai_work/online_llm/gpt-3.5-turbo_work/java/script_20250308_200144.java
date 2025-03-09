```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "JIRA", "Git", "Docker"};
        Random random = new Random();
        int index = random.nextInt(tools.length);
        return tools[index];
    }

    // Function to check if a specific tool is included in the generated tools
    public static boolean isToolIncluded(String toolName) {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "JIRA", "Git", "Docker"};
        for (String tool : tools) {
            if (tool.equalsIgnoreCase(toolName)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Generating random useful automation tools:");

        for (int i = 0; i < 5; i++) {
            String tool = generateAutomationTool();
            System.out.println((i + 1) + ". " + tool);
        }

        String specificTool = "Selenium";
        System.out.println("\nChecking if " + specificTool + " is included in the generated tools:");
        if (isToolIncluded(specificTool)) {
            System.out.println(specificTool + " is included.");
        } else {
            System.out.println(specificTool + " is not included.");
        }
    }
}
```