from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 3-qubit circuit with 3 classical bits
qc = QuantumCircuit(3, 3)

# Put the first qubit into superposition
qc.h(0)

# Entangle qubit 0 with qubit 1
qc.cx(0, 1)

# Entangle qubit 0 with qubit 2
qc.cx(0, 2)

# Measure all three qubits
qc.measure([0, 1, 2], [0, 1, 2])

# Display the circuit
print("3-Qubit GHZ Circuit:")
print(qc.draw())

# Create simulator
simulator = AerSimulator()

# Run the circuit for 1024 shots
job = simulator.run(qc, shots=1024)

# Get results
result = job.result()
counts = result.get_counts()

# Display measurement results
print("\nMeasurement Results:")
print(counts)