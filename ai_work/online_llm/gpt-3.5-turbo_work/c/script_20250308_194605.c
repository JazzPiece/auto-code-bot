```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random automation tool
void generateAutomationTool() {
    char* tools[] = {"Script to automate file backups",
                     "Tool to automate database backups",
                     "Script to automate system updates",
                     "Automation tool for monitoring server performance",
                     "Tool to automate software deployment"};

    int numTools = sizeof(tools) / sizeof(tools[0]);

    // Generate a random index to select a tool
    int randomIndex = rand() % numTools;

    printf("Generated Automation Tool: %s\n", tools[randomIndex]);
}

int main() {
    // Seed the random number generator
    srand(time(0));

    // Generate a random automation tool
    generateAutomationTool();

    return 0;
}
```

Output:
```
Generated Automation Tool: Automation tool for monitoring server performance
```