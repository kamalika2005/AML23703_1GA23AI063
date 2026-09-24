from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 2-qubit circuit
qc = QuantumCircuit(2, 2)

# Create Phi+ Bell state
qc.h(0)
qc.cx(0, 1)

# Change to Hadamard basis
qc.h(0)
qc.h(1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

print("Phi+ Bell State - Hadamard Basis")
print("================================")
print(qc)

# Run 1024 shots
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)
