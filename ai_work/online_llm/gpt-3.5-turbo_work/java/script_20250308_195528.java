```java
import java.util.Random;

public class AutomationToolGenerator {

    // Function to generate a random tool name
    public static String generateToolName() {
        String[] toolNames = {"AutoTester", "AutomateIt", "Automagic", "AutoMaster", "AutoGenius"};
        Random rand = new Random();
        int index = rand.nextInt(toolNames.length);
        return toolNames[index];
    }

    // Function to generate a random tool category
    public static String generateToolCategory() {
        String[] toolCategories = {"Testing", "Monitoring", "Deployment", "Reporting", "Integration"};
        Random rand = new Random();
        int index = rand.nextInt(toolCategories.length);
        return toolCategories[index];
    }

    // Function to generate a random tool description
    public static String generateToolDescription() {
        String[] toolDescriptions = {"Automate repetitive tasks easily", "Monitor system performance in real-time", "Deploy applications with one click", "Generate detailed reports on test results", "Integrate multiple tools seamlessly"};
        Random rand = new Random();
        int index = rand.nextInt(toolDescriptions.length);
        return toolDescriptions[index];
    }

    // Function to generate a random tool rating
    public static int generateToolRating() {
        Random rand = new Random();
        return rand.nextInt(5) + 1; // Generate a rating between 1 and 5
    }

    public static void main(String[] args) {
        String toolName = generateToolName();
        String toolCategory = generateToolCategory();
        String toolDescription = generateToolDescription();
        int toolRating = generateToolRating();

        System.out.println("=== Random Automation Tool Generator ===");
        System.out.println("Tool Name: " + toolName);
        System.out.println("Tool Category: " + toolCategory);
        System.out.println("Tool Description: " + toolDescription);
        System.out.println("Tool Rating: " + toolRating + " stars");
    }
}
```