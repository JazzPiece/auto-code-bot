Here is an improved version of the script:

```c
// Including necessary libraries
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Defining maximum number of tools and their names
#define MAX_TOOLS 6
const char* tools[MAX_TOOLS] = {"File Organizer", "Auto Emailer", "Data Scraper", "Task Scheduler", "System Monitor", "Network Analyzer"};

// Function to generate a random tool
const char* getRandomTool() {
    // Initialize random number generator
    srand(time(NULL));
    
    // Generate a random index for tools
    int randomIndex = rand() % MAX_TOOLS;
    
    return tools[randomIndex];
}

// Function to give a brief description about the randomly chosen tool
void descriptionTool(const char* tool) {
    if (strcmp(tool, "File Organizer") == 0) {
        printf("It is a tool used for arranging and managing files digital data.\n");
    } else if (strcmp(tool, "Auto Emailer") == 0) {
        printf("It is a tool used to send email automatically at a scheduled time.\n");
    } else if (strcmp(tool, "Data Scraper") == 0) {
        printf("It is a tool to extract data from websites.\n");
    } else if (strcmp(tool, "Task Scheduler") == 0) {
        printf("It is a tool used to schedule and automate tasks.\n");
    } else if (strcmp(tool, "System Monitor") == 0) {
        printf("It is a tool that reports the system's current state.\n");
    } else if (strcmp(tool, "Network Analyzer") == 0) {
        printf("It is a tool used to analysis network performance and find issues.\n");
    } else {
        printf("No description available.\n");
    }
}

int main() {
    // Generate a random tool
    const char* tool = getRandomTool();
    // print the random tool and its description
    printf("The generated automation tool is: %s\n", tool);
    printf("Description: \n");
    descriptionTool(tool);
    
    return 0;
}
```
This improved version includes a new function `descriptionTool()`, which gives a brief overview of the randomly chosen tool, and also adds "Network Analyzer" to the existing tools. This can provide the user with a better understanding of the tools and their uses.