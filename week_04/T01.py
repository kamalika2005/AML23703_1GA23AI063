from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a 2-qubit circuit
qc = QuantumCircuit(2)

# Put control qubit in |1>
qc.x(0)

# Apply CNOT: qubit 0 = control, qubit 1 = target
qc.cx(0, 1)

# Get the final statevector
state = Statevector.from_instruction(qc)

# Display circuit
print("CNOT Gate Circuit:")
print(qc.draw())

# Display final state
print("\nFinal Statevector:")
print(state)