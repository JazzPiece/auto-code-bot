#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number within a specified range
int generateRandomNumber(int min, int max) {
    return min + rand() % (max - min + 1);
}

// Function to generate a random automation tool
void generateAutomationTool() {
    char *tools[] = {"Script to automate file backup process",
                     "Automated testing tool for software applications",
                     "Script to automate data extraction from databases",
                     "Automated email sender for marketing campaigns",
                     "Tool to automate server monitoring and alerts"};

    int numTools = sizeof(tools) / sizeof(tools[0]);
    int randomIndex = generateRandomNumber(0, numTools - 1);

    printf("Generated Automation Tool: %s\n", tools[randomIndex]);
}

int main() {
    // Seed the random number generator
    srand(time(NULL));

    // Generate a random automation tool
    generateAutomationTool();

    return 0;
}

// Sample Output:
// Generated Automation Tool: Script to automate file backup process