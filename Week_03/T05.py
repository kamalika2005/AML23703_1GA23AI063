from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Circuit 1: HZH
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.z(0)
qc1.h(0)

# Circuit 2: X gate
qc2 = QuantumCircuit(1)
qc2.x(0)

# Get the statevectors
state1 = Statevector.from_instruction(qc1)
state2 = Statevector.from_instruction(qc2)

# Display Circuit 1
print("Circuit 1: HZH")
print(qc1.draw())
print("\nStatevector of HZH:")
print(state1)

# Display Circuit 2
print("\nCircuit 2: X")
print(qc2.draw())
print("\nStatevector of X:")
print(state2)

# Check if they are equivalent
print("\nAre HZH and X equivalent?")
print(state1.equiv(state2))