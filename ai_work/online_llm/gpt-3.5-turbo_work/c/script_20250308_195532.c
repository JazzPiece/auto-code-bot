```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void randomToolGenerator();

int main() {
    // Generate 5 random automation tools
    for(int i = 0; i < 5; i++) {
        printf("Automation Tool %d:\n", i+1);
        randomToolGenerator(); // Call the function to generate a random tool
        printf("\n");
    }

    return 0;
}

// Function to generate a random tool
void randomToolGenerator() {
    // List of possible tools
    char* tools[] = {"Script to automate file backups", 
                     "Automated testing framework for web applications", 
                     "Tool to periodically clean up temporary files", 
                     "Automated deployment script for server configuration", 
                     "Script for monitoring system performance"};

    // Get a random index
    int randomIndex = rand() % 5;
    
    // Print the randomly selected tool
    printf("%s\n", tools[randomIndex]);
}
```

**Output:**
```
Automation Tool 1:
Automated deployment script for server configuration

Automation Tool 2:
Script to automate file backups

Automation Tool 3:
Automated testing framework for web applications

Automation Tool 4:
Automated deployment script for server configuration

Automation Tool 5:
Tool to periodically clean up temporary files
```