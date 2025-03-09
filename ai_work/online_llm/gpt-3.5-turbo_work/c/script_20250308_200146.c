```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number between a specified range
int generateRandomNumber(int min, int max) {
    return min + rand() % (max - min + 1);
}

// Function to generate a random automation tool
void generateAutomationTool() {
    // Array of possible automation tools
    char *tools[] = {"Script to automate file backups",
                     "Tool to automate software updates",
                     "Script for automated testing of web applications",
                     "Automation tool for server maintenance",
                     "Script for scheduling automated tasks"};

    // Calculate the number of tools in the array
    int numTools = sizeof(tools) / sizeof(tools[0]);

    // Generate a random index to select a tool from the array
    int randomIndex = generateRandomNumber(0, numTools - 1);

    // Output the randomly selected automation tool
    printf("Random Automation Tool: %s\n", tools[randomIndex]);
}

int main() {
    // Seed the random number generator
    srand(time(0));

    // Generate a random automation tool
    generateAutomationTool();

    return 0;
}
```

**Sample Output**:
```
Random Automation Tool: Script for automated testing of web applications
```