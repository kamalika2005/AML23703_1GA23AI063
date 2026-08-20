from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 2-qubit Bell pair
qc = QuantumCircuit(2, 1)

# Create entanglement
qc.h(0)
qc.cx(0, 1)

# Measure only qubit 0
qc.measure(0, 0)

# Display circuit
print("Bell Pair with Partial Measurement:")
print(qc.draw())

# Run the circuit
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()

# Get measurement results
counts = result.get_counts()

print("\nMeasurement of Qubit 0:")
print(counts)

print("\nInterpretation:")
print("If qubit 0 = 0, qubit 1 collapses to |0>.")
print("If qubit 0 = 1, qubit 1 collapses to |1>.")