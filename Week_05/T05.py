from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random

# Number of measurements
shots = 10000

# -----------------------------
# Quantum Random Generator
# -----------------------------

qc = QuantumCircuit(1, 1)

# Create quantum superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Run simulator
simulator = AerSimulator()
result = simulator.run(qc, shots=shots).result()

quantum_counts = result.get_counts()


# -----------------------------
# Biased Classical Generator
# -----------------------------

classical_zeros = 0
classical_ones = 0

for i in range(shots):

    # Deliberately biased: 70% probability of 0
    if random.random() < 0.70:
        classical_zeros += 1
    else:
        classical_ones += 1

classical_counts = {
    "0": classical_zeros,
    "1": classical_ones
}


# -----------------------------
# Display Results
# -----------------------------

print("Quantum Random Generator:")
print(quantum_counts)

print("\nBiased Classical Generator:")
print(classical_counts)


# -----------------------------
# Calculate Probabilities
# -----------------------------

quantum_p0 = quantum_counts.get("0", 0) / shots
quantum_p1 = quantum_counts.get("1", 0) / shots

classical_p0 = classical_counts["0"] / shots
classical_p1 = classical_counts["1"] / shots

print("\nQuantum probabilities:")
print("P(0) =", quantum_p0)
print("P(1) =", quantum_p1)

print("\nClassical probabilities:")
print("P(0) =", classical_p0)
print("P(1) =", classical_p1)


# -----------------------------
# Chi-Square Test Statistic
# -----------------------------

expected = shots / 2

quantum_chi_square = (
    ((quantum_counts.get("0", 0) - expected) ** 2) / expected
    +
    ((quantum_counts.get("1", 0) - expected) ** 2) / expected
)

classical_chi_square = (
    ((classical_counts["0"] - expected) ** 2) / expected
    +
    ((classical_counts["1"] - expected) ** 2) / expected
)

print("\nQuantum chi-square statistic:",
      quantum_chi_square)

print("Classical chi-square statistic:",
      classical_chi_square)

print("\nInterpretation:")
print("A smaller chi-square value indicates")
print("better agreement with a 50-50 distribution.")