```Go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

// List of random automation tools
var automationTools = []string{"Puppet", "Ansible", "Chef", "SaltStack", "CFEngine", "Fabric", "Juju", "Docker"}

// Function to generate a random number within the length of automationTools
func randomTool() int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn(len(automationTools))
}

// Function to return a random automation tool
func generateRandomTool() string {
	return automationTools[randomTool()]
}

// main function to print a random automation tool
func main() {
	fmt.Println("Randomly Selected Automation Tool: ", generateRandomTool())
}
```

This script basically generates random tools from a predefined list. When you run the script, it picks a random tool from the list and prints it out. 

Note that you'll need to have Golang installed on your system to run the above script. You can do this by simply typing `go run filename.go` replacing 'filename.go' with the name of your file.

`go run randomTool.go` might return:
```
Randomly Selected Automation Tool:  Docker
```
Depending on the randomness, it may not always print 'Docker'. It can print any tool name from the list defined in `automationTools`.
Do note that on running the program multiple times in quick succession, you may find the same name being printed. This is because `rand.Seed(time.Now().UnixNano())` actually seeds the random number generator based on the current time, and computers are fast enough that it can run the program multiple times within the same nanosecond. This will seed the random number generator with the same value, and hence produce the same "random" number. Waiting even one second between runs will be enough to see different output.