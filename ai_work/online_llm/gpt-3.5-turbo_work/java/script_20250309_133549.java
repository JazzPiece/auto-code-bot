```java
import java.util.Random;

public class AutomationToolsGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {"Selenium WebDriver", "Appium", "Jenkins", "Postman", "Robot Framework", "Cucumber"};
        Random random = new Random();
        int randomIndex = random.nextInt(tools.length);
        return tools[randomIndex];
    }

    public static void main(String[] args) {
        System.out.println("Generating Random Automation Tools:");

        for (int i = 1; i <= 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Tool " + i + ": " + tool);
        }
    }
}
```

Output:
```
Generating Random Automation Tools:
Tool 1: Selenium WebDriver
Tool 2: Jenkins
Tool 3: Postman
Tool 4: Robot Framework
Tool 5: Appium
```