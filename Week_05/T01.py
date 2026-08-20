from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Different numbers of shots
shots_list = [100, 1000, 10000]

# Create simulator
simulator = AerSimulator()

for shots in shots_list:

    # Create a one-qubit circuit
    qc = QuantumCircuit(1, 1)

    # Apply Hadamard gate
    qc.h(0)

    # Measure the qubit
    qc.measure(0, 0)

    # Run the circuit
    result = simulator.run(qc, shots=shots).result()

    # Get measurement results
    counts = result.get_counts()

    # Calculate probabilities
    p0 = counts.get("0", 0) / shots
    p1 = counts.get("1", 0) / shots

    print("\n-------------------------")
    print("Shots:", shots)
    print("Counts:", counts)
    print("Probability of 0:", p0)
    print("Probability of 1:", p1)