from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create 3 qubits and 2 classical bits
qc = QuantumCircuit(3, 2)

# Inputs:
# q0 = A
# q1 = B
# q2 = Carry-in (Cin)

# Set example input: A=1, B=1, Cin=0
qc.x(0)
qc.x(1)

# Calculate Sum = A XOR B XOR Cin
qc.cx(0, 2)
qc.cx(1, 2)

# Calculate Carry using Toffoli
qc.ccx(0, 1, 2)

# Measure
qc.measure(2, 0)   # Sum
qc.measure(1, 1)   # Carry

# Display circuit
print("Full Adder Circuit:")
print(qc.draw())

# Simulate
simulator = AerSimulator()

job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)