```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {"Selenium", "Appium", "Jenkins", "TestNG", "Postman", "JIRA", "Git"};
        Random rand = new Random();
        int index = rand.nextInt(tools.length);
        return tools[index];
    }

    public static void main(String[] args) {
        // Generate 5 random automation tools
        System.out.println("Generating 5 random automation tools:");
        for (int i = 0; i < 5; i++) {
            String tool = generateAutomationTool();
            System.out.println((i + 1) + ". " + tool);
        }
    }
}
```

Output:
```
Generating 5 random automation tools:
1. Jenkins
2. Selenium
3. TestNG
4. JIRA
5. Appium
```