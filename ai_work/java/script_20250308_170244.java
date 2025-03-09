```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random automation tool
    public static String generateTool() {
        String[] tools = {"Selenium", "Appium", "Jenkins", "Postman", "Robot Framework"};
        Random random = new Random();
        int index = random.nextInt(tools.length);
        return tools[index];
    }

    // Function to check if a specific tool is valid
    public static boolean isValidTool(String toolName) {
        String[] validTools = {"Selenium", "Appium", "Jenkins", "Postman", "Robot Framework"};
        for (String tool : validTools) {
            if (tool.equalsIgnoreCase(toolName)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Generating random and validating useful automation tools:");

        // Generate and validate 5 random automation tools
        for (int i = 1; i <= 5; i++) {
            String tool = generateTool();
            System.out.println(i + ". " + tool);
            // Validate the generated tool
            if (isValidTool(tool)) {
                System.out.println("   Valid tool!");
            } else {
                System.out.println("   Invalid tool!");
            }
        }
    }
}
```

Output:
```
Generating random and validating useful automation tools:
1. Jenkins
   Valid tool!
2. Selenium
   Valid tool!
3. Appium
   Valid tool!
4. Postman
   Valid tool!
5. Robot Framework
   Valid tool!
```