from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

secret = "110"
n = len(secret)

# n input qubits + n output qubits
qc = QuantumCircuit(2 * n, n)

# Create superposition on input qubits
for i in range(n):
    qc.h(i)

# Simon oracle for secret 110
# f(x) = x XOR shifted copy according to secret
for i in range(n):
    qc.cx(i, n + i)

# Additional connections for secret bits 1
qc.cx(0, n + 2)
qc.cx(1, n + 2)

# Apply Hadamard again
for i in range(n):
    qc.h(i)

# Measure input qubits
for i in range(n):
    qc.measure(i, i)

print("Simon's Algorithm")
print("Secret string:", secret)
print("\nCircuit:")
print(qc.draw())

# Run simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

print("\nMeasurement Equations:")
for y in counts:
    print(y, "·", secret, "= 0 (mod 2)")