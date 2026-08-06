from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Start from |0>
# Apply X gate to get |1>
qc.x(0)

# Apply Hadamard gate
qc.h(0)

# Apply Z gate to create the |- > state
qc.z(0)

# Get the statevector
state = Statevector.from_instruction(qc)

# Display the circuit
print("Quantum Circuit:")
print(qc.draw())

# Display the final statevector
print("\nFinal Statevector:")
print(state)