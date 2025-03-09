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

    public static void main(String[] args) {
        System.out.println("Generating random useful automation tools:");

        for (int i = 0; i < 5; i++) {
            String tool = generateAutomationTool();
            System.out.println((i + 1) + ". " + tool);
        }
    }
}
```

Output:
```
Generating random useful automation tools:
1. Jenkins
2. Selenium
3. Git
4. Postman
5. Appium
```