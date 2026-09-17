from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create circuit
qc = QuantumCircuit(2, 1)

# Prepare second qubit in |1>
qc.x(1)

# First Hadamard
qc.h(0)
qc.h(1)

# Introduce a small gate error
qc.ry(0.1, 0)

# Balanced oracle f(x) = x
qc.cx(0, 1)

# Final Hadamard
qc.h(0)

# Introduce another small error
qc.ry(0.1, 0)

# Measure
qc.measure(0, 0)

print("Deutsch's Algorithm with Imperfect Hadamard")
print(qc.draw())

# Simulate
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement result:", counts)

zero_count = counts.get("0", 0)
one_count = counts.get("1", 0)

print("Number of 0 outcomes:", zero_count)
print("Number of 1 outcomes:", one_count)

print("Probability of 0:", zero_count / 1024)
print("Probability of 1:", one_count / 1024)