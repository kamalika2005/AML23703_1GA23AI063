from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math

# Unknown rotation angle
true_angle = math.pi / 3

# Create a 1-qubit circuit
qc = QuantumCircuit(1, 1)

# Apply the unknown rotation
qc.ry(true_angle, 0)

# Measure the qubit
qc.measure(0, 0)

# Create simulator
simulator = AerSimulator()

# Run with 10000 shots
shots = 10000
result = simulator.run(qc, shots=shots).result()

# Get measurement results
counts = result.get_counts()

# Calculate probability of measuring 1
p1 = counts.get("1", 0) / shots

# Estimate angle
estimated_angle = 2 * math.asin(math.sqrt(p1))

print("True angle:", true_angle)
print("True angle in degrees:", math.degrees(true_angle))

print("\nMeasurement counts:")
print(counts)

print("\nEstimated probability of 1:", p1)

print("\nEstimated angle in radians:", estimated_angle)
print("Estimated angle in degrees:",
      math.degrees(estimated_angle))