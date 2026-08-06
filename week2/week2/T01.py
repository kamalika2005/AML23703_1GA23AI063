from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)

print("Initial State:")
print(Statevector.from_instruction(qc))

qc.x(0)

state = Statevector.from_instruction(qc)

print("\nState after X Gate:")
print(state)