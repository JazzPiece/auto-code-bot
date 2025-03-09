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

    public static void main(String[] args) {
        System.out.println("Generating random useful automation tools:");

        // Generate 5 random automation tools
        for (int i = 1; i <= 5; i++) {
            String tool = generateTool();
            System.out.println(i + ". " + tool);
        }
    }
}
```

Output:
```
Generating random useful automation tools:
1. Jenkins
2. Selenium
3. Appium
4. Postman
5. Robot Framework
```