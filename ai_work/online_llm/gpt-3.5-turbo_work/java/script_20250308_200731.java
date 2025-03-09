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
    
    public static void main(String[] args) {
        // Generate a random automation tool
        String automationTool = generateAutomationTool();
        
        // Output the generated automation tool
        System.out.println("Random Automation Tool Generated: " + automationTool);
    }
}
```

Output:
```
Random Automation Tool Generated: Selenium
```