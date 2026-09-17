from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def deutsch_jozsa(n, function_type):

    # Create n input qubits + 1 output qubit
    qc = QuantumCircuit(n + 1, n)

    # Prepare output qubit in |1>
    qc.x(n)

    # First Hadamard layer
    for i in range(n + 1):
        qc.h(i)

    # Oracle
    if function_type == "constant":
        # f(x) = 0
        pass

    elif function_type == "balanced":
        # Parity function
        for i in range(n):
            qc.cx(i, n)

    else:
        raise ValueError("Invalid function type")

    # Second Hadamard layer
    for i in range(n):
        qc.h(i)

    # Measurement
    for i in range(n):
        qc.measure(i, i)

    return qc


simulator = AerSimulator()

# Test n = 2 to 5
for n in range(2, 6):

    print("\n==============================")
    print("n =", n)
    print("==============================")

    # Constant function
    qc_constant = deutsch_jozsa(n, "constant")

    result = simulator.run(
        qc_constant,
        shots=1024
    ).result()

    counts = result.get_counts()

    print("Constant function:")
    print(counts)

    # Balanced function
    qc_balanced = deutsch_jozsa(n, "balanced")

    result = simulator.run(
        qc_balanced,
        shots=1024
    ).result()

    counts = result.get_counts()

    print("Balanced function:")
    print(counts)