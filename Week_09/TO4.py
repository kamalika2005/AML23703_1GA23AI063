from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Create Phi+ Bell state
qc.h(0)
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Run simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

counts = result.get_counts()

print("ENTANGLEMENT-BASED QKD")
print("======================")

print("\nMeasurement Results:")
print(counts)

print("\nExplanation:")
print("Alice and Bob share an entangled Bell pair.")
print("When measured in the same basis, their results are correlated.")
print("An eavesdropper interacting with the quantum system")
print("can disturb these correlations and may be detected.")
