from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import itertools

secret = "1101"
n = len(secret)

# Create n input qubits + n output qubits
qc = QuantumCircuit(2 * n, n)

# Step 1: Superposition
for i in range(n):
    qc.h(i)

# Step 2: Simon oracle
# Copy each input bit to its corresponding output bit
for i in range(n):
    qc.cx(i, n + i)

# Extra connections for secret = 1101
qc.cx(0, 7)
qc.cx(1, 7)
qc.cx(3, 7)

# Step 3: Hadamard on input qubits
for i in range(n):
    qc.h(i)

# Step 4: Measure input qubits
for i in range(n):
    qc.measure(i, i)

print("Simon's Algorithm - 4 Bit")
print("Secret string:", secret)

print("\nCircuit:")
print(qc.draw())

# Run simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

# --------------------------------
# Solve equations over GF(2)
# --------------------------------

def dot_product(a, b):
    return sum(int(x) * int(y) for x, y in zip(a, b)) % 2


print("\nMeasurement Equations:")

equations = []

for y in counts:
    if y != "0000":
        equations.append(y)
        print(y, "· s = 0 (mod 2)")


# Find possible secret strings
solutions = []

for candidate in itertools.product("01", repeat=n):

    candidate = "".join(candidate)

    valid = True

    for y in equations:
        if dot_product(y, candidate) != 0:
            valid = False
            break

    if valid:
        solutions.append(candidate)


print("\nPossible solutions:")
print(solutions)

print("\nActual secret:")
print(secret)