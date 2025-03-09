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

    public static void main(String[] args) {
        System.out.println("Generating random automation tools:");

        // Generate 5 random automation tools
        for (int i = 1; i <= 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Tool " + i + ": " + tool);
        }
    }
}
```

Output:
```
Generating random automation tools:
Tool 1: Jenkins
Tool 2: Selenium
Tool 3: Katalon Studio
Tool 4: Robot Framework
Tool 5: Postman
```