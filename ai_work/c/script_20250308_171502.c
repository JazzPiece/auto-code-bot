```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number between a given range
int generateRandomNumber(int min, int max) {
    return min + rand() % (max - min + 1);
}

// Function to generate a random automation tool
void generateAutomationTool() {
    char* tools[] = {
        "Automated Testing Tool",
        "CI/CD Pipeline Tool",
        "Infrastructure as Code Tool",
        "Logging and Monitoring Tool",
        "Scripting Language Tool"
    };

    int numTools = sizeof(tools) / sizeof(tools[0]);
    
    // Generate a random index to choose a tool from the array
    int randomIndex = generateRandomNumber(0, numTools - 1);
    
    printf("Random Automation Tool Generated: %s\n", tools[randomIndex]);
}

// Function to display the available automation tools
void displayAvailableTools() {
    printf("\nAvailable Automation Tools:\n");
    printf("1. Automated Testing Tool\n");
    printf("2. CI/CD Pipeline Tool\n");
    printf("3. Infrastructure as Code Tool\n");
    printf("4. Logging and Monitoring Tool\n");
    printf("5. Scripting Language Tool\n");
}

int main() {
    // Seed the random number generator
    srand(time(0));

    printf("Welcome to the Random Automation Tool Generator\n");
    
    char userInput;
    
    do {
        displayAvailableTools();
        generateAutomationTool();

        printf("\nDo you want to generate another random automation tool? (y/n): ");
        scanf(" %c", &userInput);
    } while(userInput == 'y' || userInput == 'Y');
    
    printf("Thank you for using the Random Automation Tool Generator!\n");

    return 0;
}
```