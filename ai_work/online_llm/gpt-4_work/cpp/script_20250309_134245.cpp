```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>

// Function Declarations
void generateAutoTools(int toolID);

// Main Function
int main() {
    // Seed for random number
    srand(static_cast<unsigned int>(time(0)));

    // Generate 5 random automation tools
    for (int i=0; i<5; i++) {
        int toolID = rand() % 5;
        generateAutoTools(toolID);
    }

    return 0;
}

// Function Definitions

/**
 * Function to generate useful automation tools based on the toolID
 * @param toolID: the random ID associated with an automation tool
 */
void generateAutoTools(int toolID) {
    switch (toolID)
    {
    case 0:
        std::cout << "Automated Testing Tool" << std::endl;
        break;
    case 1:
        std::cout << "Task Automation Tool" << std::endl;
        break;
    case 2:
        std::cout << "Data Scraping Tool" << std::endl;
        break;
    case 3:
        std::cout << "Code Formatting Tool" << std::endl;
        break;
    case 4:
        std::cout << "API Testing Tool" << std::endl;
        break;
    default:
        std::cout << "Unknown tool" << std::endl;
        break;
    }
}
```

This simple program generates five random identifiers (`toolID`), each associated with a distinct type of automation tool. The functions and purpose of each tool are printed to the console.

However, please note: being a simple console-based application, it does not actually generate or implement any real-life automation tools. C++ is not typically used to actually create automation tools, it's more commonly leveraged for application or library development, etc.

Also please note, it's impossible to provide full script output as the output is generated at runtime and is randomly determined.

Best practices followed:
- Proper function usage, including clear documentation.
- Using `switch-case` for conditional execution.
- Good use of whitespace and proper indentation for readability.
- Helpful inline comments to explain logic.