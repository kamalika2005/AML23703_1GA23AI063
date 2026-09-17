from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit with 2 qubits and 1 classical bit
qc = QuantumCircuit(2, 1)

# Prepare the second qubit in |1>
qc.x(1)

# Apply Hadamard gates
qc.h(0)
qc.h(1)

# Oracle for constant function f(x) = 0
# No operation is required

# Apply Hadamard to the first qubit
qc.h(0)

# Measure the first qubit
qc.measure(0, 0)

print("Deutsch's Algorithm - Constant Function f(x) = 0")
print(qc.draw())

# Simulate the circuit
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement result:", counts)