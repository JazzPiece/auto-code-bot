# Import necessary libraries
import numpy as np
from qiskit import QuantumCircuit, Aer, execute

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply Hadamard gate on qubit 0
qc.h(0)

# Apply CNOT gate with control qubit 0 and target qubit 1
qc.cx(0, 1)

# Measure qubits
qc.measure_all()

# Simulate the quantum circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()

# Get the counts of the measurement outcomes
counts = result.get_counts(qc)
print(counts)