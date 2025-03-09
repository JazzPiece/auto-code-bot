```java
import java.util.Random;

public class AutomationToolGenerator {

    /**
     * Generates a random automation tool name.
     * @return a randomly generated automation tool name
     */
    public static String generateRandomToolName() {
        String[] toolNames = {"AutoTester", "AutomateIt", "CodeMaster", "ScriptGenius", "AutoWizard"};
        Random random = new Random();
        int index = random.nextInt(toolNames.length);
        return toolNames[index];
    }

    /**
     * Generates a random automation tool description.
     * @return a randomly generated automation tool description
     */
    public static String generateRandomToolDescription() {
        String[] toolDescriptions = {
            "A powerful tool for automating test cases.",
            "Simplify your workflow with this automation tool.",
            "Increase productivity with this efficient automation software.",
            "Automate repetitive tasks with ease using this tool.",
            "Improve software development processes with automation."
        };
        Random random = new Random();
        int index = random.nextInt(toolDescriptions.length);
        return toolDescriptions[index];
    }

    /**
     * Generates a random automation tool version.
     * @return a randomly generated automation tool version
     */
    public static String generateRandomToolVersion() {
        String[] toolVersions = {"v1.0", "v2.0", "v3.0", "v4.0", "v5.0"};
        Random random = new Random();
        int index = random.nextInt(toolVersions.length);
        return toolVersions[index];
    }

    public static void main(String[] args) {
        String toolName = generateRandomToolName();
        String toolDescription = generateRandomToolDescription();
        String toolVersion = generateRandomToolVersion();

        System.out.println("Random Automation Tool Generated:");
        System.out.println("Name: " + toolName);
        System.out.println("Description: " + toolDescription);
        System.out.println("Version: " + toolVersion);
    }
}
```

Output:
```
Random Automation Tool Generated:
Name: AutoTester
Description: A powerful tool for automating test cases.
Version: v3.0
```