from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 1-qubit circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

print("Quantum Circuit:")
print(qc)

# Run on ideal simulator
backend = Aer.get_backend("aer_simulator")

job = backend.run(qc, shots=1024)

result = job.result()

counts = result.get_counts()

print("\nIdeal Simulator Results:")
print(counts)

# Display histogram
plot_histogram(counts)
plt.show()

print("\nTo run on a real IBM Quantum computer:")
print("1. Create a free IBM Quantum account.")
print("2. Copy your API token.")
print("3. Save the token using Qiskit Runtime.")
print("4. Choose an available backend.")
print("5. Submit the circuit.")