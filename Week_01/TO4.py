from qiskit import QuantumCircuit
from qiskit_aer import Aer
import random

# Quantum simulator
backend = Aer.get_backend("aer_simulator")

quantum_bits = []

print("Generating Quantum Random Bits...")

# Generate 20 quantum random bits
for i in range(20):

    qc = QuantumCircuit(1, 1)

    qc.h(0)          # Put qubit into superposition

    qc.measure(0, 0)

    job = backend.run(qc, shots=1)

    result = job.result()

    counts = result.get_counts()

    bit = list(counts.keys())[0]

    quantum_bits.append(bit)

# Generate 20 Python random bits
python_bits = []

print("\nGenerating Python Random Bits...")

for i in range(20):
    python_bits.append(str(random.randint(0, 1)))

# Display Results
print("\nQuantum Random Bits:")
print(" ".join(quantum_bits))

print("\nPython Random Bits:")
print(" ".join(python_bits))