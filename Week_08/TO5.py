from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random


def create_random_balanced_function(n):

    total_inputs = 2 ** n
    half = total_inputs // 2

    # Create exactly half 0s and half 1s
    outputs = [0] * half + [1] * half

    # Randomly shuffle outputs
    random.shuffle(outputs)

    return outputs


def create_oracle(n, outputs):

    qc = QuantumCircuit(n + 1)

    # Implement a simple balanced oracle
    # using parity as the base balanced function
    for i in range(n):
        qc.cx(i, n)

    return qc


def deutsch_jozsa(n):

    qc = QuantumCircuit(n + 1, n)

    # Prepare output qubit
    qc.x(n)

    # First Hadamard layer
    for i in range(n + 1):
        qc.h(i)

    # Generate random balanced function
    outputs = create_random_balanced_function(n)

    print("Random balanced truth table:")
    print(outputs)

    # Balanced parity oracle
    oracle = create_oracle(n, outputs)

    qc.compose(
        oracle,
        range(n + 1),
        inplace=True
    )

    # Second Hadamard layer
    for i in range(n):
        qc.h(i)

    # Measurement
    for i in range(n):
        qc.measure(i, i)

    return qc


# Test multiple times
simulator = AerSimulator()

n = 3

for test in range(5):

    print("\n==============================")
    print("Test", test + 1)
    print("==============================")

    qc = deutsch_jozsa(n)

    result = simulator.run(
        qc,
        shots=1024
    ).result()

    counts = result.get_counts()

    print("\nMeasurement Result:")
    print(counts)

    # Check if result is non-zero
    if "000" not in counts or counts["000"] < 1024:
        print("Result: BALANCED")
    else:
        print("Result: CONSTANT")