from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create circuit
qc = QuantumCircuit(2, 1)

# Prepare target qubit in |1>
qc.x(1)

# Apply Hadamard gates
qc.h(0)
qc.h(1)

# Balanced oracle f(x) = x
qc.cx(0, 1)

# Final Hadamard on control qubit
qc.h(0)

# Measure control qubit
qc.measure(0, 0)

print("Phase Kickback Demonstration")
print(qc.draw())

# Simulate
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement result:", counts)

if counts.get("0", 0) > counts.get("1", 0):
    print("Function behaves as CONSTANT")
else:
    print("Function behaves as BALANCED")