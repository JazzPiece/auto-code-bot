```java
// Importing required libraries
import java.util.Random;
import java.util.Scanner;

public class RandomAutomationToolGenerator {
    // An array to store the name of different automation tools
    private String[] automationTools = {
            "Selenium", "TestComplete", "Watir", "Appium", "Ranorex", "Katalon Studio", "JMeter", "SoapUI", "Cucumber", "Postman"
    };

    // Main function
    public static void main(String[] args) {
        RandomAutomationToolGenerator generator = new RandomAutomationToolGenerator();
        System.out.println("Do you want a specific type of tool? y/n");
        Scanner scanner = new Scanner(System.in);
        String response = scanner.nextLine();
        if (response.toLowerCase().equals("y")) {
            System.out.println("Please enter the type: ");
            String type = scanner.nextLine();
            generator.generateToolByType(type);
        } else {
            generator.generateTool();
        }
    }

    /**
     * This function generates a random automation tool from the array
     */
    public void generateTool() {
        Random random = new Random();
        String randomTool = automationTools[random.nextInt(automationTools.length)];
        System.out.println("Suggested automation tool is: " + randomTool);
    }

    /**
     * This function generates a random tool of a specific type from the array
     * @param type The type of tool the user wants
     */
    public void generateToolByType(String type) {
        Random random = new Random();
        String randomTool = "";
        for (String tool : automationTools) {
            if (tool.contains(type)) {
                randomTool = tool;
                break;
            }
        }
        if (randomTool.equals("")) {
            System.out.println("No tool of this type is found.");
        } else {
            System.out.println("Suggested automation tool is: " + randomTool);
        }
    }
}
``` 

This enhanced script now includes the ability to filter the automation tools by type, as provided by the user. A scanner is used to read the user's input and based on it, the appropriate method is called. If the user wants a specific type of tool, the 'generateToolByType()' method is used, else the 'generateTool()' method is used to suggest a tool randomly. Inline comments are provided for better understanding and it follows best practices for Java. The 'generateToolByType()' method takes in a type as a parameter and iteratively checks for the entered type in the automationTools array. If found, it suggests that tool, else it prints a message saying no tool of this type is found. This provides the user with more flexibility in choosing the tool they want.