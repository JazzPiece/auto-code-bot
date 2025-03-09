#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number within a specified range
int generateRandomNumber(int min, int max) {
    return rand() % (max - min + 1) + min;
}

// Function to generate a random string of given length
char* generateRandomString(int length) {
    char* randomString = (char*)malloc((length + 1) * sizeof(char));
    for(int i = 0; i < length; i++) {
        randomString[i] = 'a' + rand() % 26; // Generate a random lowercase letter
    }
    randomString[length] = '\0'; // Add null terminator at the end
    return randomString;
}

int main() {
    srand(time(NULL)); // Seed for random number generation

    // Generate a random automation tool name
    char* toolName = generateRandomString(8);

    // Generate a random version number
    int majorVersion = generateRandomNumber(1, 10);
    int minorVersion = generateRandomNumber(0, 99);
    int patchVersion = generateRandomNumber(0, 99);

    // Display the generated automation tool details
    printf("Generated Automation Tool:\n");
    printf("Name: %s\n", toolName);
    printf("Version: %d.%d.%d\n", majorVersion, minorVersion, patchVersion);

    // Free the dynamically allocated memory for the random string
    free(toolName);

    return 0;
}

/*
Output:
Generated Automation Tool:
Name: jvzlwqet
Version: 4.23.75
*/