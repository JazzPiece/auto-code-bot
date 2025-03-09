```java
import java.util.Random;

public class AutomationToolsGenerator {
    
    // Function to generate a random automation tool
    public static String generateAutomationTool() {
        String[] tools = {
            "Selenium WebDriver",
            "Appium",
            "Jenkins",
            "Postman",
            "JIRA",
            "Robot Framework"
        };
        
        Random random = new Random();
        int index = random.nextInt(tools.length);
        
        return tools[index];
    }
    
    public static void main(String[] args) {
        // Generate 5 random automation tools
        for (int i = 1; i <= 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Automation Tool " + i + ": " + tool);
        }
    }
}
```

Output:
```
Automation Tool 1: Selenium WebDriver
Automation Tool 2: Jenkins
Automation Tool 3: Robot Framework
Automation Tool 4: JIRA
Automation Tool 5: Appium
```