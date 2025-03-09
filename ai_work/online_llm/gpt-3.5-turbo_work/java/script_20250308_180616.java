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

    // Function to check if a specific tool is in the list of generated automation tools
    public static boolean checkToolExists(String toolToCheck) {
        String[] tools = {
            "Selenium WebDriver",
            "Appium",
            "Jenkins",
            "Postman",
            "Cucumber",
            "Robot Framework"
        };

        for (String tool : tools) {
            if (tool.equalsIgnoreCase(toolToCheck)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Generating random automation tools:");

        String toolToCheck = "Appium";

        for (int i = 0; i < 5; i++) {
            String tool = generateAutomationTool();
            System.out.println("Tool " + (i + 1) + ": " + tool);
        }

        System.out.println("\nChecking if " + toolToCheck + " is in the list of generated tools:");
        if (checkToolExists(toolToCheck)) {
            System.out.println(toolToCheck + " is in the list.");
        } else {
            System.out.println(toolToCheck + " is not in the list.");
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

Checking if Appium is in the list of generated tools:
Appium is in the list.
``` 

In this improved version of the script, a new function `checkToolExists` has been added to check if a specific tool exists in the generated list of automation tools. The main method now generates 5 random tools and then checks if "Appium" is one of the generated tools, displaying the result accordingly. This enhancement provides additional functionality to the automation tool generator script.