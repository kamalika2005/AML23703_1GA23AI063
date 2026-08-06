from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# List of gates to test
gates = ["X", "Y", "Z"]

for gate in gates:
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1)

    # Apply the selected gate
    if gate == "X":
        qc.x(0)
    elif gate == "Y":
        qc.y(0)
    elif gate == "Z":
        qc.z(0)

    # Get the statevector
    state = Statevector.from_instruction(qc)

    # Display the results
    print("\n==============================")
    print(f"{gate} Gate")
    print("==============================")
    print(qc.draw())
    print("Statevector:")
    print(state)