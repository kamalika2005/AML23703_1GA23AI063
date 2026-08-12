from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Create a 2-qubit circuit
qc = QuantumCircuit(2)

# Create an arbitrary entangled state
# |ψ> = sqrt(3)/2 |00> + 1/2 |11>

# Apply a rotation to qubit 0
import math

theta = math.pi / 3
qc.ry(theta, 0)

# Entangle qubit 0 and qubit 1
qc.cx(0, 1)

# Get the final statevector
state = Statevector.from_instruction(qc)

# Display the circuit
print("Arbitrary 2-Qubit Entangled State Circuit:")
print(qc.draw())

# Display the statevector
print("\nStatevector:")
print(state)

# Display probabilities
print("\nProbabilities:")
print(state.probabilities())