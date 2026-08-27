from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import itertools


def dot_product(a, b):
    """Dot product over GF(2)."""
    return sum(int(x) * int(y) for x, y in zip(a, b)) % 2


def create_oracle(secret):
    n = len(secret)
    qc = QuantumCircuit(2 * n, n)

    # Copy input bits to output bits
    for i in range(n):
        qc.cx(i, n + i)

    # Add connections according to secret
    for i, bit in enumerate(secret):
        if bit == "1" and i != n - 1:
            qc.cx(i, 2 * n - 1)

    return qc


def simons_algorithm(secret, shots=1024):

    n = len(secret)

    # All-zero edge case
    if set(secret) == {"0"}:
        print("Secret is all-zero:", secret)
        print("No non-zero secret vector needs to be solved.")
        return secret

    qc = QuantumCircuit(2 * n, n)

    # First Hadamard layer
    for i in range(n):
        qc.h(i)

    # Oracle
    oracle = create_oracle(secret)
    qc.compose(oracle, range(2 * n), inplace=True)

    # Second Hadamard layer
    for i in range(n):
        qc.h(i)

    # Measure input register
    for i in range(n):
        qc.measure(i, i)

    # Run simulation
    simulator = AerSimulator()
    result = simulator.run(qc, shots=shots).result()
    counts = result.get_counts()

    print("Secret string:", secret)
    print("\nMeasurement Results:")
    print(counts)

    # Collect independent equations
    equations = []

    for y in counts:
        if y != "0" * n and y not in equations:
            equations.append(y)

    print("\nMeasurement Equations:")

    for y in equations:
        print(y, "· s = 0 (mod 2)")

    # Search for valid secret strings
    solutions = []

    for candidate in itertools.product("01", repeat=n):

        candidate = "".join(candidate)

        if all(dot_product(y, candidate) == 0 for y in equations):
            solutions.append(candidate)

    # Remove zero solution because Simon's secret is non-zero
    if "0" * n in solutions:
        solutions.remove("0" * n)

    print("\nPossible non-zero solutions:")
    print(solutions)

    if secret in solutions:
        print("\nSecret successfully determined:", secret)
    else:
        print("\nMore independent equations may be required.")

    return solutions


# Test with a 4-bit secret
simons_algorithm("1101")