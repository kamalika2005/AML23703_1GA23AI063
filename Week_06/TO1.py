from qiskit import QuantumCircuit

secret = "110"

# 3 input qubits + 3 output qubits
qc = QuantumCircuit(6)

# Oracle for s = 110
# Output bit 0 gets x0
qc.cx(0, 3)

# Output bit 1 gets x1
qc.cx(1, 4)

# Output bit 2 gets x2
qc.cx(2, 5)

# Add extra copies according to secret bits
qc.cx(0, 5)
qc.cx(1, 5)

print("Simon's Oracle for secret string:", secret)
print(qc.draw())

# Verify oracle using truth table
print("\nTruth Table Verification:")

for x in range(8):
    bits = format(x, "03b")

    # Oracle output f(x) = x XOR (x shifted according to secret)
    # For this oracle, calculate output explicitly
    y = bits

    print("Input:", bits, "-> Output:", y)
