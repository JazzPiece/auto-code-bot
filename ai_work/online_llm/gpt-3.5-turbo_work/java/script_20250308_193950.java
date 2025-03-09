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

    public static void main(String[] args) {
        // Generating 5 random automation tools
        for (int i = 1; i <= 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Automation Tool " + i + ": " + tool);
        }
    }
}
```

Output:
```
Automation Tool 1: Jenkins
Automation Tool 2: Postman
Automation Tool 3: Selenium WebDriver
Automation Tool 4: JIRA
Automation Tool 5: Appium
```