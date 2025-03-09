#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number between a specified range
int generateRandomNumber(int min, int max) {
    return rand() % (max - min + 1) + min;
}

// Function to generate a random automation tool
void generateAutomationTool() {
    char* tools[] = {
        "Automated Testing Framework",
        "CI/CD Pipeline Automation Tool",
        "Configuration Management Tool",
        "Monitoring and Alerting Tool",
        "Infrastructure as Code Tool",
        "Deployment Automation Tool",
        "Security Compliance Automation Tool"
    };

    int numTools = sizeof(tools) / sizeof(tools[0]);

    // Generate a random index to select a tool
    int randomIndex = generateRandomNumber(0, numTools - 1);

    printf("Random Automation Tool: %s\n", tools[randomIndex]);
}

int main() {
    // Seed the random number generator
    srand(time(NULL));

    // Generate a random automation tool
    generateAutomationTool();

    return 0;
}

// Sample Output:
// Random Automation Tool: CI/CD Pipeline Automation Tool