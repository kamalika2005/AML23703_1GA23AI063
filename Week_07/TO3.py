from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def deutsch_oracle(function_type):
    """
    Creates an oracle for one of the four possible
    one-bit Boolean functions.
    """

    oracle = QuantumCircuit(2)

    if function_type == "constant_0":
        # f(x) = 0
        pass

    elif function_type == "constant_1":
        # f(x) = 1
        oracle.x(1)

    elif function_type == "balanced_x":
        # f(x) = x
        oracle.cx(0, 1)

    elif function_type == "balanced_not_x":
        # f(x) = 1 - x
        oracle.x(1)
        oracle.cx(0, 1)

    else:
        raise ValueError("Invalid function type")

    return oracle


# Select the function
function_type = "balanced_x"

# Create the oracle
oracle = deutsch_oracle(function_type)

print("Selected function:", function_type)
print("\nOracle circuit:")
print(oracle.draw())


# Complete Deutsch circuit
qc = QuantumCircuit(2, 1)

# Prepare second qubit in |1>
qc.x(1)

# Create superposition
qc.h(0)
qc.h(1)

# Add selected oracle
qc.compose(oracle, inplace=True)

# Final Hadamard
qc.h(0)

# Measure first qubit
qc.measure(0, 0)

print("\nComplete Deutsch Circuit:")
print(qc.draw())


# Simulate
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement result:", counts)

# Interpret result
if counts.get("0", 0) > counts.get("1", 0):
    print("Function is CONSTANT")
else:
    print("Function is BALANCED")