```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {
            "Selenium WebDriver",
            "Appium",
            "Jenkins",
            "Postman",
            "Cucumber",
            "Robot Framework"
        };

        Random random = new Random();
        int index = random.nextInt(tools.length);

        return tools[index];
    }

    public static void main(String[] args) {
        System.out.println("Generating random automation tools:");

        for (int i = 0; i < 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Tool " + (i + 1) + ": " + tool);
        }
    }
}
```

Output:
```
Generating random automation tools:
Tool 1: Jenkins
Tool 2: Selenium WebDriver
Tool 3: Appium
Tool 4: Postman
Tool 5: Robot Framework
```