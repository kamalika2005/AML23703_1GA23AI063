from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)

for qubit in range(2):
    qc.h(qubit)

state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

print("\nProbabilities:")
print(state.probabilities_dict())