```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number within a specified range
int generateRandomNumber(int min, int max) {
    return min + rand() % (max - min + 1);
}

// Function to generate a random password of variable length
void generateRandomPassword(int length) {
    char password[length + 1]; // +1 for null terminator
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
    
    srand(time(NULL));
    
    for (int i = 0; i < length; i++) {
        password[i] = charset[generateRandomNumber(0, sizeof(charset) - 1)];
    }
    
    password[length] = '\0';
    
    printf("Random Password: %s\n", password);
}

// Function to generate a random email address
void generateRandomEmail() {
    char email[22]; // Increased size to accommodate null terminator at index 21
    const char name[] = "abcdefghijklmnopqrstuvwxyz0123456789";
    const char domain[] = "gmail.com";
    
    srand(time(NULL));
    
    for (int i = 0; i < 8; i++) {
        email[i] = name[generateRandomNumber(0, sizeof(name) - 1)];
    }
    
    email[8] = '@';
    
    for (int i = 9; i < 17; i++) {
        email[i] = name[generateRandomNumber(0, sizeof(name) - 1)];
    }
    
    for (int i = 17; i < 21; i++) {
        email[i] = domain[i - 17];
    }
    
    email[21] = domain[0]; // Adding the first letter of the domain for variation
    email[22] = '\0';
    
    printf("Random Email Address: %s\n", email);
}

// Function to generate a random username
void generateRandomUsername() {
    char username[9]; // For a username of length 8
    const char name[] = "abcdefghijklmnopqrstuvwxyz0123456789";
    
    srand(time(NULL));
    
    for (int i = 0; i < 8; i++) {
        username[i] = name[generateRandomNumber(0, sizeof(name) - 1)];
    }
    
    username[8] = '\0';
    
    printf("Random Username: %s\n", username);
}

int main() {
    generateRandomPassword(12); // Generate a random password of length 12
    generateRandomEmail(); // Generate a random email address
    generateRandomUsername(); // Generate a random username
    
    return 0;
}
```