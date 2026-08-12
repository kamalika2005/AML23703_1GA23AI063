from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2, 2)

# Create superposition on qubit 0
qc.h(0)

# Entangle qubit 0 and qubit 1
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Display the circuit
print("Bell State Circuit:")
print(qc.draw())

# Create simulator
simulator = AerSimulator()

# Run the circuit for 1024 shots
job = simulator.run(qc, shots=1024)

# Get measurement results
result = job.result()
counts = result.get_counts()

# Display results
print("\nMeasurement Results:")
print(counts)