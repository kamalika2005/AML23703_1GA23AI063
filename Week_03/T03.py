from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply a sequence of five single-qubit gates
qc.h(0)
qc.x(0)
qc.s(0)
qc.y(0)
qc.t(0)

# Get the final statevector
state = Statevector.from_instruction(qc)

# Display the circuit
print("Quantum Circuit:")
print(qc.draw())

# Display the final statevector
print("\nFinal Statevector:")
print(state)