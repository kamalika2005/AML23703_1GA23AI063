from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Get the statevector
state = Statevector.from_instruction(qc)

# Calculate probabilities
probabilities = state.probabilities()

# Display the circuit
print("Quantum Circuit:")
print(qc.draw())

# Display the statevector
print("\nStatevector:")
print(state)

# Display probabilities
print("\nProbability of Heads (|0>):", probabilities[0])
print("Probability of Tails (|1>):", probabilities[1])