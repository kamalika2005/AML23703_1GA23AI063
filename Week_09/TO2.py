from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()


def create_bell_state(name):
    qc = QuantumCircuit(2, 2)

    # Create Phi+ = (|00> + |11>) / sqrt(2)
    qc.h(0)
    qc.cx(0, 1)

    # Convert Phi+ into the other Bell states
    if name == "Phi-":
        qc.z(0)

    elif name == "Psi+":
        qc.x(0)

    elif name == "Psi-":
        qc.x(0)
        qc.z(0)

    qc.measure([0, 1], [0, 1])

    return qc


bell_states = ["Phi+", "Phi-", "Psi+", "Psi-"]

print("FOUR BELL STATES")
print("================")

for state in bell_states:

    circuit = create_bell_state(state)

    result = simulator.run(
        circuit,
        shots=1024
    ).result()

    counts = result.get_counts()

    print("\n" + state)
    print(counts)
