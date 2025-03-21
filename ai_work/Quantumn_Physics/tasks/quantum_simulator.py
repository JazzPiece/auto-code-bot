# Import necessary libraries
import numpy as np

# Define quantum simulator class
class QuantumSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits)
        self.state[0] = 1

    def hadamard_gate(self, target_qubit):
        hadamard_matrix = 1/np.sqrt(2) * np.array([[1, 1], [1, -1]])
        operator = np.eye(2)
        for i in range(self.num_qubits):
            if i == target_qubit:
                operator = np.kron(operator, hadamard_matrix)
            else:
                operator = np.kron(operator, np.eye(2))

        self.state = np.dot(operator, self.state)

# Example usage
if __name__ == "__main__":
    qs = QuantumSimulator(2)
    print("Initial state:")
    print(qs.state)
    
    qs.hadamard_gate(0)
    print("State after applying Hadamard gate to qubit 0:")
    print(qs.state)
    
    qs.hadamard_gate(1)
    print("State after applying Hadamard gate to qubit 1:")
    print(qs.state)
    <python script>