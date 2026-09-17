from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Number of input qubits
n = 3

# Create n input qubits + 1 output qubit
qc = QuantumCircuit(n + 1, n)

# Prepare output qubit in |1>
qc.x(n)

# Step 1: Apply Hadamard gates
for i in range(n + 1):
    qc.h(i)

# Step 2: Balanced parity oracle
qc.cx(0, n)
qc.cx(1, n)
qc.cx(2, n)

# Step 3: Apply Hadamard to input qubits
for i in range(n):
    qc.h(i)

# Step 4: Measure input qubits
for i in range(n):
    qc.measure(i, i)

print("Deutsch-Jozsa Algorithm")
print("Function: Balanced parity function")
print("f(x) = x0 XOR x1 XOR x2")

print("\nCircuit:")
print(qc.draw())

# Simulate
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)