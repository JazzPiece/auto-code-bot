#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random automation tool
void generateAutomationTool() {
    char* tools[] = {"Script to automate file backups", "Tool to schedule system maintenance tasks", 
                      "Script for monitoring server performance", "Automation tool for deploying software updates",
                      "Script to automate data migration tasks"};

    int numTools = sizeof(tools) / sizeof(tools[0]);
    int randomIndex = rand() % numTools;

    printf("Random Automation Tool: %s\n", tools[randomIndex]);
}

int main() {
    // Seed for generating random numbers
    srand(time(0));

    printf("Generating Random Useful Automation Tools...\n");

    // Generate 5 random automation tools
    for (int i = 0; i < 5; i++) {
        generateAutomationTool();
    }

    return 0;
}

// Sample Output:
// Generating Random Useful Automation Tools...
// Random Automation Tool: Script to automate file backups
// Random Automation Tool: Tool to schedule system maintenance tasks
// Random Automation Tool: Automation tool for deploying software updates
// Random Automation Tool: Script for monitoring server performance
// Random Automation Tool: Script to automate data migration tasks