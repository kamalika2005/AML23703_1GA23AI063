from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 3-qubit circuit
qc = QuantumCircuit(3, 3)

# Apply Hadamard gate to all qubits
qc.h(0)
qc.h(1)
qc.h(2)

# Measure all qubits
qc.measure([0, 1, 2], [0, 1, 2])

print("Quantum Circuit:")
print(qc)

# Select simulator
backend = Aer.get_backend("aer_simulator")

# Execute the circuit
job = backend.run(qc, shots=8192)

# Get results
result = job.result()
counts = result.get_counts()

print("\nMeasurement Counts:")
print(counts)

# Display probabilities
print("\nProbability Distribution:")
for state in sorted(counts):
    probability = counts[state] / 8192
    print(f"{state}: {probability:.4f}")

print("\nExpected Probability for each state = 1/8 = 0.1250")

# Plot histogram
plot_histogram(counts)
plt.show()